from __future__ import unicode_literals
import discord
from discord.ext import commands
from pybooru import Danbooru
from operator import itemgetter
from danb import *
import re
import PARAMETERS

no_dupe = []
server = discord.Client()
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='?', intents=intents)
cli = Danbooru('danbooru', username=PARAMETERS.DANBOORU_USER, api_key=PARAMETERS.DANBOORU_TOKEN)


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command(aliases=['h'])
async def user_help(ctx):
    e = discord.Embed(title='Helper', color=0x0e0de6)
    helper(e)
    await ctx.send(embed=e)


@client.command(aliases=['tag', 't'])
async def tagged(ctx, *, tags='hololive'):
    try:
        posts = cli.post_list(tags=f'{tags}', limit=2)
        for n in range(0, 2):
            if posts[n]['id'] not in no_dupe[-10:]:
                e = discord.Embed(title='Tagged', color=0x0e0de6)
                image_embed_multiple(e, posts, n)
                no_dupe.append(posts[n]['id'])

                await ctx.send(embed=e)
                break
    except IndexError:
        w = discord.Embed(title='InaDisappoint', color=0x2ae20c)
        ina_embed(w)
        await ctx.send(embed=w)
    except KeyError:
        w = discord.Embed(title='KeyError: I know how to fix but it\'s aids', color=0x2ae20c)
        ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)
        ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['rt', 'rts'])
async def ran_tag_saf(ctx, *, tags='-boys_only', rating='s'):
    posts = cli.post_list(tags=f'{tags}', limit=40, random=True)
    for n in range(0, 40):
        try:
            if banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-10:]:
                e = discord.Embed(title='Tagged Safe', color=0x2ae20c)
                image_embed_multiple(e, posts, n)
                no_dupe.append(posts[n]['id'])

                await ctx.send(embed=e)
                break
        except KeyError:
            pass
        except IndexError:
            w = discord.Embed(title='IndexError: Input a usable tag, retard', color=0x2ae20c)
            ina_embed(w)
            await ctx.send(embed=w)
            break


@client.command(aliases=['rtq'])
async def ran_tag_que(ctx, *, tags='-boys_only', rating='q'):
    posts = cli.post_list(tags=f'{tags}', limit=100, random=True)
    for n in range(0, 100):
        try:
            if banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-10:]:
                e = discord.Embed(title='Tagged Questionable', color=0xee8f10)
                image_embed_multiple(e, posts, n)
                no_dupe.append(posts[n]['id'])

                await ctx.send(embed=e)
                break
        except KeyError:
            pass
        except IndexError:
            w = discord.Embed(title='IndexError: Input a usable tag, retard', color=0x2ae20c)
            ina_embed(w)
            await ctx.send(embed=w)
            break


@client.command(aliases=['rte'])
async def ran_tag_ex(ctx, *, tags='-boys_only', rating='e'):
    posts = cli.post_list(tags=f'{tags}', limit=40, random=True)
    for n in range(0, 40):
        try:
            if banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-10:]:
                e = discord.Embed(title='Tagged Explicit', color=0xe20c0c)
                image_embed_multiple(e, posts, n)
                no_dupe.append(posts[n]['id'])

                await ctx.send(embed=e)
                break
        except KeyError:
            pass
        except IndexError:
            w = discord.Embed(title='IndexError: Input a usable tag, retard', color=0x2ae20c)
            ina_embed(w)
            await ctx.send(embed=w)
            break


@client.command(aliases=['r', 'random'])
async def pure_random(ctx):
    posts = cli.post_list(limit=1, tags='-boys_only', random=True)
    e = discord.Embed(title='Random', color=0x0b0b0c)
    image_embed_multiple(e, posts, 0)

    await ctx.send(embed=e)


@client.command(aliases=['pop', 'popular'])
async def popular_post(ctx, *, page='1'):
    try:
        page = int(page)
        post = cli.post_list(limit=2, tags='order:rank', page={page})
        for n in range(0, 2):
            e = discord.Embed(title='Popular Post', color=0xFF00FF)
            image_embed_multiple(e, post, n)

            await ctx.send(embed=e)
            break
    except KeyError:
        w = discord.Embed(title='KeyError: lole go somewhere else', color=0x2ae20c)
        ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError: Enter a number, retard', color=0x2ae20c)
        ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['tbig', 'tpop'])
async def tagged_popular(ctx, *, tags='-boys_only'):
    try:
        posts = cli.post_list(tags=f'{tags}', limit=100)
        updoot = []
        for n in range(0, 100):
            updoot.append(posts[n]['up_score'])
        tied = tuple(zip(posts, updoot))
        s_u = sorted(tied, key=itemgetter(1))
        s_u.reverse()
        for n in range(0, 100):
            try:
                if re.search(accepted_file_types, s_u[n][0]['file_url'][-3:]) \
                        and s_u[n][0]['id'] not in no_dupe[-10:]:
                    post = s_u[n]
                    e = discord.Embed(title='Most Popular Tagged', color=0x2ae20c)
                    image_embed_multiple(e, post, 0)
                    no_dupe.append(s_u[n][0]['id'])

                    await ctx.send(embed=e)
                    break
            except KeyError:
                pass
            except IndexError:
                break
    except IndexError:
        w = discord.Embed(title='IndexError', color=0x2ae20c)
        ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)
        ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['tebig', 'tepop'])
async def tagged_popular_explicit(ctx, *, tags='-boys_only', rating='e'):
    try:
        posts = cli.post_list(tags=f'{tags}', limit=100)
        updoot = []
        for n in range(0, 100):
            updoot.append(posts[n]['up_score'])
        tied = tuple(zip(posts, updoot))
        s_u = sorted(tied, key=itemgetter(1))
        s_u.reverse()
        for n in range(0, 100):
            try:
                if re.search(accepted_file_types, s_u[n][0]['file_url'][-3:]) and \
                        s_u[n][0]['rating'] in rating and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-10:]:
                    post = s_u[n]
                    e = discord.Embed(title='Most Popular Tagged', color=0x2ae20c)
                    image_embed_multiple(e, post, 0)
                    no_dupe.append(s_u[n][0]['id'])

                    await ctx.send(embed=e)
                    break
            except KeyError:
                print(f'KeyError: ?tepop {tags}')
                pass
            except IndexError:
                print(f'IndexError: ?tepop {tags}')
                pass
    except IndexError:
        w = discord.Embed(title='IndexError', color=0x2ae20c)
        ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)
        ina_embed(w)
        await ctx.send(embed=w)


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author.bot:
        return
    if re.search(feet_pattern, message.content):
        if not message.content.startswith('?'):
            await message.channel.send(feet())
    if re.search(cumb_pattern, message.content):
        await message.channel.send(cum())


client.run(PARAMETERS.BOT_TOKEN)

from __future__ import unicode_literals
import discord
from discord.ext import commands
from pybooru import Danbooru
from operator import itemgetter
import DanbooruBot.embeder
import re
import PARAMETERS
from loghelp import opener

no_dupe = []
server = discord.Client()
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='?', intents=intents)
cli = Danbooru('danbooru', username=PARAMETERS.DANBOORU_USER, api_key=PARAMETERS.DANBOORU_TOKEN)
banned_tags = 'male_focus'
feet_pattern = '[fF].{2}[eE]*.{0,1}[tT]'
c_t_pattern = '[cC].{0,1}[uUoO]*.{0,1}[mM]'


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command(aliases=['h'])
async def user_help(ctx):
    e = discord.Embed(title='Helper', color=0x0e0de6)  # none
    DanbooruBot.embeder.helper(e)
    await ctx.send(embed=e)


@client.command(aliases=['tag', 't'])  # saved to no dupe
async def tagged(ctx, *, tags='hololive'):
    try:
        posts = cli.post_list(tags=f'{tags}', limit=2)
        for n in range(0, 2):
            if posts[n]['id'] not in no_dupe[-15:] and \
                    re.search(DanbooruBot.embeder.accepted_file_types, posts['file_ext']):
                e = discord.Embed(title='Tagged', color=0x0e0de6)  # saver
                DanbooruBot.embeder.image_embed_multiple(e, posts, n)
                no_dupe.append(posts[n]['id'])

                await ctx.send(embed=e)
                break
    except IndexError:
        w = discord.Embed(title='IndexError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)
    except KeyError:
        w = discord.Embed(title='KeyError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['rt', 'rts'])  # saved to no dupe
async def ran_tag_saf(ctx, *, tags='-boys_only', rating='s'):
    posts = cli.post_list(tags=f'{tags}', limit=40, random=True)
    for n in range(0, 40):
        try:
            if banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = discord.Embed(title='Tagged Safe', color=0x2ae20c)  # saver
                DanbooruBot.embeder.image_embed_multiple(e, posts, n)
                no_dupe.append(posts[n]['id'])

                await ctx.send(embed=e)
                break
        except KeyError:
            pass
        except IndexError:
            w = discord.Embed(title='IndexError: Input a usable tag', color=0x2ae20c)  # logg
            DanbooruBot.embeder.ina_embed(w)
            await ctx.send(embed=w)
            break


@client.command(aliases=['rtq'])  # saved to no dupe
async def ran_tag_que(ctx, *, tags='-boys_only', rating='q'):
    posts = cli.post_list(tags=f'{tags}', limit=100, random=True)
    for n in range(0, 100):
        try:
            if banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = discord.Embed(title='Tagged Questionable', color=0xee8f10)  # saver
                DanbooruBot.embeder.image_embed_multiple(e, posts, n)
                no_dupe.append(posts[n]['id'])

                await ctx.send(embed=e)
                break
        except KeyError:
            pass
        except IndexError:
            w = discord.Embed(title='IndexError: Input a usable tag', color=0x2ae20c)  # logg
            DanbooruBot.embeder.ina_embed(w)
            await ctx.send(embed=w)
            break


@client.command(aliases=['rte'])  # saved to no dupe
async def ran_tag_ex(ctx, *, tags='-boys_only', rating='e'):
    posts = cli.post_list(tags=f'{tags}', limit=40, random=True)
    for n in range(0, 40):
        try:
            if banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = discord.Embed(title='Tagged Explicit', color=0xe20c0c)  # saver
                DanbooruBot.embeder.image_embed_multiple(e, posts, n)
                no_dupe.append(posts[n]['id'])

                await ctx.send(embed=e)
                break
        except KeyError:
            pass
        except IndexError:
            w = discord.Embed(title='IndexError: Input a usable tag', color=0x2ae20c)  # logg
            DanbooruBot.embeder.ina_embed(w)
            await ctx.send(embed=w)
            break


@client.command(aliases=['r', 'random'])  # not saved to no_dupe
async def pure_random(ctx):
    posts = cli.post_list(limit=1, tags='-boys_only', random=True)
    try:
        if re.search(DanbooruBot.embeder.accepted_file_types, posts['file_ext']):
            e = discord.Embed(title='Random', color=0x0b0b0c)  # saver
            DanbooruBot.embeder.image_embed_multiple(e, posts, 0)
        
            await ctx.send(embed=e)
    except KeyError:
        w = discord.Embed(title='KeyError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['pop', 'popular'])  # not saved to no_dupe
async def popular_post(ctx, *, page='1'):
    try:
        page = int(page)
        post = cli.post_list(limit=2, tags='order:rank', page={page})
        for n in range(0, 2):
            if re.search(DanbooruBot.embeder.accepted_file_types, post[n]['file_ext']):
                e = discord.Embed(title='Popular Post', color=0xFF00FF)  # saver
                DanbooruBot.embeder.image_embed_multiple(e, post, n)
    
                await ctx.send(embed=e)
                break
    except KeyError:
        w = discord.Embed(title='KeyError: Go somewhere else', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError: Enter a number, not a tag', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['tbig', 'tpop'])  # saved to no_dupe
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
                if re.search(DanbooruBot.embeder.accepted_file_types, s_u[n][0]['file_ext']) \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    post = s_u[n]
                    e = discord.Embed(title='Most Popular Tagged', color=0x2ae20c)  # saver
                    DanbooruBot.embeder.image_embed_multiple(e, post, 0)
                    no_dupe.append(s_u[n][0]['id'])

                    await ctx.send(embed=e)
                    break
            except KeyError:
                pass
            except IndexError:
                break
    except IndexError:
        w = discord.Embed(title='IndexError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['tebig', 'tepop'])  # saved to no_dupe
async def tagged_popular_explicit(ctx, *, tags='-boys_only', rating='e'):
    try:
        posts = cli.post_list(tags=f'{tags}', limit=100)
        updoot = []
        try:
            for n in range(0, 100):
                updoot.append(posts[n]['up_score'])
        except IndexError:
            pass
        tied = tuple(zip(posts, updoot))
        s_u = sorted(tied, key=itemgetter(1))
        s_u.reverse()
        for n in range(0, 100):
            try:
                if re.search(DanbooruBot.embeder.accepted_file_types, s_u[n][0]['file_ext']) and \
                        s_u[n][0]['rating'] in rating and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    post = s_u[n]
                    e = discord.Embed(title='Most Popular Explicit Tagged', color=0x2ae20c)  # saver
                    DanbooruBot.embeder.image_embed_multiple(e, post, 0)
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
        w = discord.Embed(title='IndexError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['tqbig', 'tqpop'])  # saved to no_dupe
async def tagged_popular_questionable(ctx, *, tags='-boys_only', rating='q'):
    try:
        posts = cli.post_list(tags=f'{tags}', limit=100)
        updoot = []
        try:
            for n in range(0, 100):
                updoot.append(posts[n]['up_score'])
        except IndexError:
            pass
        tied = tuple(zip(posts, updoot))
        s_u = sorted(tied, key=itemgetter(1))
        s_u.reverse()
        for n in range(0, 100):
            try:
                if re.search(DanbooruBot.embeder.accepted_file_types, s_u[n][0]['file_ext']) and \
                        s_u[n][0]['rating'] in rating and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    post = s_u[n]
                    e = discord.Embed(title='Most Popular Questionable Tagged', color=0x2ae20c)  # saver
                    DanbooruBot.embeder.image_embed_multiple(e, post, 0)
                    no_dupe.append(s_u[n][0]['id'])

                    await ctx.send(embed=e)
                    break
            except KeyError:
                print(f'KeyError: ?tqpop {tags}')
                pass
            except IndexError:
                print(f'IndexError: ?tqpop {tags}')
                pass
    except IndexError:
        w = discord.Embed(title='IndexError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['tsbig', 'tspop'])  # saved to no_dupe
async def tagged_popular_safe(ctx, *, tags='-boys_only', rating='s'):
    try:
        posts = cli.post_list(tags=f'{tags}', limit=100)
        updoot = []
        try:
            for n in range(0, 100):
                updoot.append(posts[n]['up_score'])
        except IndexError:
            pass
        tied = tuple(zip(posts, updoot))
        s_u = sorted(tied, key=itemgetter(1))
        s_u.reverse()
        for n in range(0, 100):
            try:
                if re.search(DanbooruBot.embeder.accepted_file_types, s_u[n][0]['file_ext']) and \
                        s_u[n][0]['rating'] in rating and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    post = s_u[n]
                    e = discord.Embed(title='Most Popular Safe Tagged', color=0x2ae20c)  # saver
                    DanbooruBot.embeder.image_embed_multiple(e, post, 0)
                    no_dupe.append(s_u[n][0]['id'])

                    await ctx.send(embed=e)
                    break
            except KeyError:
                print(f'KeyError: ?tspop {tags}')
                pass
            except IndexError:
                print(f'IndexError: ?tspop {tags}')
                pass
    except IndexError:
        w = discord.Embed(title='IndexError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['hist'])  # not saved to no_dupe
async def historical_character(ctx, *, character='keqing_(genshin_impact)'):
    try:
        post = opener(character)
        w = discord.Embed(title='Historical Tagged', color=0x2ae20c)  # none
        DanbooruBot.embeder.hist_embed(w, post)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        DanbooruBot.embeder.ina_embed(w)
        await ctx.send(embed=w)


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author.bot:
        return
    if re.search(feet_pattern, message.content):
        if not message.content.startswith('?'):
            await message.channel.send(PARAMETERS.F_COPY_PASTA)
    if re.search(c_t_pattern, message.content):
        if not message.content.startswith('?'):
            await message.channel.send(PARAMETERS.T_COPY_PASTA)


client.run(PARAMETERS.BOT_TOKEN)

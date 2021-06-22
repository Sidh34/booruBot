from __future__ import unicode_literals
from pybooru.exceptions import PybooruHTTPError
from danhelp import *
from discordhelp import *
from saucenaohelper import *
import time

banned_tags = 'male_focus'
feet_pattern = '[fF].{2}[eE]*.{0,1}[tT]'
c_t_pattern = '[cC]+[uUoO]+[uUoOmM]+[mMbB]*'


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command(aliases=['h'])
async def user_help(ctx):
    e = discord.Embed(title='Helper', color=0x0e0de6)  # none
    helper(e)
    await ctx.send(embed=e)


@client.command(aliases=['tag', 't'])  # saved to no dupe
async def tagged(ctx, *, tags='hololive'):
    start_time = time.time()
    try:
        posts = small_post_getter(tags)
        for n in range(0, 2):
            if posts[n]['id'] not in no_dupe[-15:] and \
                    re.search(accepted_file_types, posts[n]['file_ext']):
                e = tagged_disc_embed(posts, n)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                break
            elif posts[n]['id'] not in no_dupe[-15:] and \
                    re.search(partially_accepted, posts[n]['file_ext']):
                e = tagged_disc_embed(posts, n)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                break
            elif posts[n]['id'] not in no_dupe[-15:] and \
                    re.search(zip_replace, posts[n]['large_file_url'][-4:]):
                e = tagged_disc_embed(posts, n)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                break
    except IndexError:
        w = discord.Embed(title='IndexError', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)
    except KeyError:
        w = discord.Embed(title='KeyError', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['rt', 'rts'])  # saved to no dupe
async def ran_tag_saf(ctx, *, tags='-boys_only', rating='s'):
    start_time = time.time()
    posts = random_post_getter(tags)
    for n in range(0, 100):
        try:
            if re.search(accepted_file_types, posts[n]['file_ext']) and \
                    banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = ran_tagged_discord_embed(posts, n, rating)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                break
            elif re.search(partially_accepted, posts[n]['file_ext']) and \
                    banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = ran_tagged_discord_embed(posts, n, rating)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                await ctx.send(f"{posts[n]['file_url']}")
                break
            elif re.search(zip_replace, posts[n]['large_file_url'][-4:]) and \
                    banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = ran_tagged_discord_embed(posts, n, rating)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                await ctx.send(f"{posts[n]['large_file_url']}")
                break
        except KeyError:
            pass
        except IndexError:
            w = discord.Embed(title='IndexError: Input a usable tag', color=0x2ae20c)  # logg
            ina_embed(w)
            await ctx.send(embed=w)
            break


@client.command(aliases=['rtq'])  # saved to no dupe
async def ran_tag_que(ctx, *, tags='-boys_only', rating='q'):
    start_time = time.time()
    posts = random_post_getter(tags)
    for n in range(0, 100):
        try:
            if re.search(accepted_file_types, posts[n]['file_ext']) and \
                    banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = ran_tagged_discord_embed(posts, n, rating)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                break
            elif re.search(partially_accepted, posts[n]['file_ext']) and \
                    banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = ran_tagged_discord_embed(posts, n, rating)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                await ctx.send(f"{posts[n]['file_url']}")
                break
            elif re.search(zip_replace, posts[n]['large_file_url'][-4:]) and \
                    banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = ran_tagged_discord_embed(posts, n, rating)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                await ctx.send(f"{posts[n]['large_file_url']}")
                break
        except KeyError:
            pass
        except IndexError:
            w = discord.Embed(title='IndexError: Input a usable tag', color=0x2ae20c)  # logg
            ina_embed(w)
            await ctx.send(embed=w)
            break


@client.command(aliases=['rte'])  # saved to no dupe
async def ran_tag_exp(ctx, *, tags='-boys_only', rating='e'):
    start_time = time.time()
    posts = random_post_getter(tags)
    for n in range(0, 100):
        try:
            if re.search(accepted_file_types, posts[n]['file_ext']) and \
                    banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = ran_tagged_discord_embed(posts, n, rating)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                break
            elif re.search(partially_accepted, posts[n]['file_ext']) and \
                    banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = ran_tagged_discord_embed(posts, n, rating)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                await ctx.send(f"{posts[n]['file_url']}")
                break
            elif re.search(zip_replace, posts[n]['large_file_url'][-4:]) and \
                    banned_tags not in posts[n]['tag_string_general'] and posts[n]['rating'] in rating \
                    and posts[n]['id'] not in no_dupe[-15:]:
                e = ran_tagged_discord_embed(posts, n, rating)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                await ctx.send(f"{posts[n]['large_file_url']}")
                break
        except KeyError:
            pass
        except IndexError:
            w = discord.Embed(title='IndexError: Input a usable tag', color=0x2ae20c)  # logg
            ina_embed(w)
            await ctx.send(embed=w)
            break


@client.command(aliases=['r', 'random'])  # not saved to no_dupe
async def pure_random(ctx):
    start_time = time.time()
    posts = small_random_post_getter()
    try:
        if re.search(accepted_file_types, posts[0]['file_ext']):
            e = discord.Embed(title='Random', color=0x0b0b0c)  # saver
            image_embed_multiple(e, posts, 0)
            e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

            await ctx.send(embed=e)
        elif re.search(partially_accepted, posts[0]['file_ext']):
            e = discord.Embed(title='Random', color=0x0b0b0c)  # saver
            image_embed_multiple(e, posts, 0)
            e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

            await ctx.send(embed=e)
            await ctx.send(f"{posts[0]['file_url']}")
        elif re.search(zip_replace, posts[0]['large_file_url'][-4:]):
            e = discord.Embed(title='Random', color=0x0b0b0c)  # saver
            image_embed_multiple(e, posts, 0)
            e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

            await ctx.send(embed=e)
            await ctx.send(f"{posts[0]['large_file_url']}")
    except KeyError:
        w = discord.Embed(title='KeyError', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['pop', 'popular'])  # not saved to no_dupe
async def popular_post(ctx, *, page='1'):
    start_time = time.time()
    try:
        page = int(page)
        post = popular_post_getter(page)
        for n in range(0, 2):
            if re.search(accepted_file_types, post[n]['file_ext']):
                e = order_rank_discord_embed(post, n)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                break
            elif re.search(partially_accepted, post[n]['file_ext']):
                e = order_rank_discord_embed(post, n)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                await ctx.send(f"{post[n]['file_url']}")
                break
            elif re.search(zip_replace, post[n]['large_file_url'][-4:]):
                e = order_rank_discord_embed(post, n)
                e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                await ctx.send(embed=e)
                await ctx.send(f"{post[n]['large_file_url']}")
                break
    except KeyError:
        w = discord.Embed(title='KeyError: Go somewhere else', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError: Enter a number, not a tag', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['tbig', 'tpop'])  # saved to no_dupe
async def tagged_popular(ctx, *, tags='-boys_only'):
    start_time = time.time()
    try:
        posts = large_post_getter(tags)
        s_u = sun(posts)
        for n in range(0, 100):
            try:
                if re.search(accepted_file_types, s_u[n][0]['file_ext']) \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_popular_discord_embed(s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    break
                elif re.search(partially_accepted, s_u[n][0]['file_ext']) \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_popular_discord_embed(s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    await ctx.send(f"{s_u[n][0]['file_url']}")
                    break
                elif re.search(zip_replace, s_u[n][0]['large_file_url'][-4:]) \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_popular_discord_embed(s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    await ctx.send(f"{s_u[n][0]['large_file_url']}")
                    break
            except KeyError:
                pass
            except IndexError:
                break
    except IndexError:
        w = discord.Embed(title='IndexError', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['tebig', 'tepop'])  # saved to no_dupe
async def tagged_popular_explicit(ctx, *, tags='-boys_only', rating='e'):
    start_time = time.time()
    try:
        posts = large_post_getter(tags)
        s_u = sun(posts)
        for n in range(0, 100):
            try:
                if re.search(accepted_file_types, s_u[n][0]['file_ext']) \
                        and s_u[n][0]['rating'] in rating and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_pop_rate_discord_embed(rating, s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    break
                elif re.search(partially_accepted, s_u[n][0]['file_ext']) and s_u[n][0]['rating'] in rating \
                        and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_pop_rate_discord_embed(rating, s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    await ctx.send(f"{s_u[n][0]['file_url']}")
                    break
                elif re.search(zip_replace, s_u[n][0]['large_file_url'][-4:]) and s_u[n][0]['rating'] in rating \
                        and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_pop_rate_discord_embed(rating, s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    await ctx.send(f"{s_u[n][0]['large_file_url']}")
                    break
            except KeyError:
                print(f'KeyError: ?tepop {tags}')
                pass
            except IndexError:
                w = discord.Embed(title='IndexError', color=0x2ae20c)  # logg
                ina_embed(w)
                await ctx.send(embed=w)
                break
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['tqbig', 'tqpop'])  # saved to no_dupe
async def tagged_popular_questionable(ctx, *, tags='-boys_only', rating='q'):
    start_time = time.time()
    try:
        posts = large_post_getter(tags)
        s_u = sun(posts)
        for n in range(0, 100):
            try:
                if re.search(accepted_file_types, s_u[n][0]['file_ext']) and \
                        s_u[n][0]['rating'] in rating and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_pop_rate_discord_embed(rating, s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    break
                elif re.search(partially_accepted, s_u[n][0]['file_ext']) and s_u[n][0]['rating'] in rating \
                        and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_pop_rate_discord_embed(rating, s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    await ctx.send(f"{s_u[n][0]['file_url']}")
                    break
                elif re.search(zip_replace, s_u[n][0]['large_file_url'][-4:]) and s_u[n][0]['rating'] in rating \
                        and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_pop_rate_discord_embed(rating, s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    await ctx.send(f"{s_u[n][0]['large_file_url']}")
                    break
            except KeyError:
                print(f'KeyError: ?tqpop {tags}')
                pass
            except IndexError:
                w = discord.Embed(title='IndexError', color=0x2ae20c)  # logg
                ina_embed(w)
                await ctx.send(embed=w)
                break
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['tsbig', 'tspop'])  # saved to no_dupe
async def tagged_popular_safe(ctx, *, tags='-boys_only', rating='s'):
    start_time = time.time()
    try:
        posts = large_post_getter(tags)
        s_u = sun(posts)
        for n in range(0, 100):
            try:
                if re.search(accepted_file_types, s_u[n][0]['file_ext']) and s_u[n][0]['rating'] in rating \
                        and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_pop_rate_discord_embed(rating, s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    break
                elif re.search(partially_accepted, s_u[n][0]['file_ext']) and s_u[n][0]['rating'] in rating \
                        and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_pop_rate_discord_embed(rating, s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    await ctx.send(f"{s_u[n][0]['file_url']}")
                    break
                elif re.search(zip_replace, s_u[n][0]['large_file_url'][-4:]) and s_u[n][0]['rating'] in rating \
                        and banned_tags not in s_u[n][0]['tag_string_general'] \
                        and s_u[n][0]['id'] not in no_dupe[-15:]:
                    e = tagged_pop_rate_discord_embed(rating, s_u, n)
                    e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

                    await ctx.send(embed=e)
                    await ctx.send(f"{s_u[n][0]['large_file_url']}")
                    break
            except KeyError:
                print(f'KeyError: ?tspop {tags}')
                pass
            except IndexError:
                w = discord.Embed(title='IndexError', color=0x2ae20c)  # logg
                ina_embed(w)
                await ctx.send(embed=w)
                break
    except ValueError:
        w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)


# @client.command(aliases=['hist'])  # not saved to no_dupe
# async def historical_character(ctx, *, character='keqing_(genshin_impact)'):
#     try:
#         post = opener(character)
#         e = discord.Embed(title='Historical Tagged', color=0x2ae20c)  # none
#         hist_embed(e, post)
#         await ctx.send(embed=e)
#     except ValueError:
#         w = discord.Embed(title='ValueError', color=0x2ae20c)  # logg
#         ina_embed(w)
#         await ctx.send(embed=w)


@client.command(aliases=['id'])
async def id_find_info(ctx, *, identity):
    start_time = time.time()
    try:
        post = id_post_getter(identity)
        if re.search(accepted_file_types, post['file_ext']) and banned_tags not in post['tag_string_general']:
            e = discord.Embed(title='ID Grab', color=0x2ae20c)  # not logg or saver
            individual_embed(e, post)
            e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

            await ctx.send(embed=e)
        elif re.search(partially_accepted, post['file_ext']) and banned_tags not in post['tag_string_general']:
            e = discord.Embed(title='ID Grab', color=0x2ae20c)  # not logg or saver
            individual_embed(e, post)
            e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

            await ctx.send(embed=e)
            await ctx.send(f"{post['file_url']}")
        elif re.search(zip_replace, post['large_file_url'][-4:]) and banned_tags not in post['tag_string_general']:
            e = discord.Embed(title='ID Grab', color=0x2ae20c)  # not logg or saver
            individual_embed(e, post)
            e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))

            await ctx.send(embed=e)
            await ctx.send(f"{post['large_file_url']}")
        else:
            w = discord.Embed(title='oof', color=0x2ae20c)  # logg
            ina_embed(w)
            await ctx.send(embed=w)
    except PybooruHTTPError:
        w = discord.Embed(title='INPUT ID', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['search'])
async def sauce_find(ctx, *, img):
    start_time = time.time()
    try:
        result = find_sauce(img)
        e = discord.Embed(title="SauceNao", color=0x2ae20c)
        sauce_embed(e, result)
        e.set_footer(text="--- {0:.8f} seconds ---".format(time.time() - start_time))
        await ctx.send(embed=e)
    except:
        w = discord.Embed(title='oof', color=0x2ae20c)  # logg
        ina_embed(w)
        await ctx.send(embed=w)


@client.command(aliases=['wtf'])
async def extension_finder(ctx, *, identity):
    post = id_post_getter(identity)
    await ctx.send(f"{post['file_ext']}")


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

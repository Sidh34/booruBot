import logging
import PARAMETERS

bot_url = PARAMETERS.BOT_URL
ina_url = PARAMETERS.INA_URL
megumin_url = PARAMETERS.MEGUMIN_URL
aqua_url = PARAMETERS.AQUA_URL
darkness_url = PARAMETERS.DARKNESS_URL

banned_tags = 'male_focus'
feet_pattern = '[fF].{2}[eE]*.{0,1}[tT]'
accepted_file_types = '(png|jpg|gif)'
c_t_pattern = '[cC].{0,1}[uUoO]*.{0,1}[mM]'


def logg():
    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S',
                        level=logging.DEBUG,
                        filename='logs.txt')


def helper(embed):  # needs finishing
    embed.set_image(url=bot_url)
    embed.add_field(name='?t (tag)', value='Used to find post of specific tag', inline=True)
    embed.add_field(name='?rts (tag)', value='Used to find a random, tagged, safe post', inline=True)
    embed.add_field(name='?rtq (tag)', value='Used to find a random, tagged, questionable post', inline=True)
    embed.add_field(name='?rte (tag)', value='Used to find a random, tagged, explicit post', inline=True)
    embed.add_field(name='?r', value='Used to find a random post, independent of tag(Always not dudes)', inline=True)
    embed.add_field(name='?pop #', value='Used to find popular/hot posts', inline=True)
    embed.add_field(name='?tpop (tag)', value='Used to find most upvoted post of given tag', inline=True)
    embed.add_field(name='?h', value='Help', inline=True)
    logg()


def c_t():
    return PARAMETERS.T_COPY_PASTA


def f_t():
    return PARAMETERS.F_COPY_PASTA


def ina_embed(embed):
    embed.set_image(url=ina_url)
    embed.add_field(name='You idiot', value='Stop screwing it up')
    logg()


def image_embed_multiple(embed, post, n):
    if 'jpg' in post[n]['file_url'][-3:] or 'png' in post[n]['file_url'][-3:] or 'gif' in post[n]['file_url'][-3:]:
        embed.set_image(url=post[n]['file_url'])
    else:
        embed.set_image(url=ina_url)
    embed.add_field(name='Post ID', value=post[n]['id'], inline=True)
    if post[n]['rating'] == 's':
        rating = 'Safe'
        embed.set_thumbnail(url=megumin_url)
    elif post[n]['rating'] == 'q':
        rating = 'Questionable'
        embed.set_thumbnail(url=aqua_url)
    elif post[n]['rating'] == 'e':
        rating = 'Explicit'
        embed.set_thumbnail(url=darkness_url)
    else:
        rating = 'Unknown'
    if post[n]['tag_string_character']:
        embed.add_field(name='Character', value=post[n]['tag_string_character'].split(' ')[0], inline=True)
    else:
        embed.add_field(name='Character', value='Original', inline=True)
    embed.add_field(name='Rating', value=rating, inline=True)
    embed.add_field(name='Upvotes', value=post[n]['up_score'], inline=True)
    embed.add_field(name='Downvotes', value=post[n]['down_score'], inline=True)
    logg()

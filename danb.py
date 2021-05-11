import logging
import PARAMETERS
import re

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
    embed.set_image(url=PARAMETERS.BOT_URL)
    embed.add_field(name='?t (tag)', value='Used to find post of specific tag', inline=True)
    embed.add_field(name='?rts (tag)', value='Used to find a random, tagged, safe post', inline=True)
    embed.add_field(name='?rtq (tag)', value='Used to find a random, tagged, questionable post', inline=True)
    embed.add_field(name='?rte (tag)', value='Used to find a random, tagged, explicit post', inline=True)
    embed.add_field(name='?r', value='Used to find a random post, independent of tag(Always not dudes)', inline=True)
    embed.add_field(name='?pop #', value='Used to find popular/hot posts', inline=True)
    embed.add_field(name='?tpop (tag)', value='Used to find most upvoted post of given tag', inline=True)
    embed.add_field(name='?h', value='Help', inline=True)
    logg()


def ina_embed(embed):
    embed.set_image(url=PARAMETERS.INA_URL)
    embed.add_field(name='You idiot', value='Stop screwing it up')
    logg()


def image_embed_multiple(embed, post, n):
    if re.search(accepted_file_types, post[n]['file_url'][-3:]):
        embed.set_image(url=post[n]['file_url'])
    else:
        embed.set_image(url=PARAMETERS.INA_URL)
    embed.add_field(name='Post ID', value=post[n]['id'], inline=True)
    if post[n]['rating'] == 's':
        rating = 'Safe'
        embed.set_thumbnail(url=PARAMETERS.MEGUMIN_URL)
    elif post[n]['rating'] == 'q':
        rating = 'Questionable'
        embed.set_thumbnail(url=PARAMETERS.AQUA_URL)
    elif post[n]['rating'] == 'e':
        rating = 'Explicit'
        embed.set_thumbnail(url=PARAMETERS.DARKNESS_URL)
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

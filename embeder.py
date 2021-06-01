import PARAMETERS
import re
from loghelp import *


accepted_file_types = '(png|jpg|gif)'
partially_accepted = 'mp4'
zip_replace = 'webm'


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


def ina_embed(embed):
    # For errors
    embed.set_image(url=PARAMETERS.INA_URL)
    embed.add_field(name='You idiot', value='Stop screwing it up')
    logg()


def image_embed_multiple(embed, post, n):
    # Pulled from Danbooru API post
    # useful dict tags for post[n]['tags']
    # ['file_url'], ['id'], ['rating'], ['tag_string_character'].split(' ')[0],
    # ['tag_string_artist'], ['up_score'], ['down_score'], ['file_ext']
    if re.search(accepted_file_types, post[n]['file_ext']):
        embed.set_image(url=post[n]['file_url'])
    elif re.search(partially_accepted, post[n]['file_ext']) or re.search(zip_replace, post[n]['large_file_url'][-4:]):
        pass
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
    saver(post, n)


def hist_embed(embed, post):
    # Pulled from saving.json
    # ["Character"], ["Rating"], ["ImageUrl"], ["Upvotes"], ["id"]
    embed.add_field(name='Post ID', value=post['id'], inline=True)
    embed.add_field(name='Character', value=post['Character'], inline=True)
    if post['Rating'] == 's':
        rating = 'Safe'
        embed.set_thumbnail(url=PARAMETERS.MEGUMIN_URL)
    elif post['Rating'] == 'q':
        rating = 'Questionable'
        embed.set_thumbnail(url=PARAMETERS.AQUA_URL)
    elif post['Rating'] == 'e':
        rating = 'Explicit'
        embed.set_thumbnail(url=PARAMETERS.DARKNESS_URL)
    else:
        rating = 'Unknown'
    embed.add_field(name='Rating', value=rating, inline=False)
    embed.add_field(name='Upvotes', value=post['Upvotes'], inline=False)
    embed.set_image(url=post['ImageUrl'])


def individual_embed(embed, post):
    # Pulled from Danbooru API post
    if re.search(accepted_file_types, post['file_ext']):
        embed.set_image(url=post['file_url'])
    elif re.search(partially_accepted, post['file_ext']) or re.search(zip_replace, post['large_file_url'][-4:]):
        pass
    else:
        embed.set_image(url=PARAMETERS.INA_URL)
    embed.add_field(name='Post ID', value=post['id'], inline=True)
    if post['rating'] == 's':
        rating = 'Safe'
        embed.set_thumbnail(url=PARAMETERS.MEGUMIN_URL)
    elif post['rating'] == 'q':
        rating = 'Questionable'
        embed.set_thumbnail(url=PARAMETERS.AQUA_URL)
    elif post['rating'] == 'e':
        rating = 'Explicit'
        embed.set_thumbnail(url=PARAMETERS.DARKNESS_URL)
    else:
        rating = 'Unknown'
    if post['tag_string_character']:
        embed.add_field(name='Character', value=post['tag_string_character'].split(' ')[0], inline=True)
    else:
        embed.add_field(name='Character', value='Original', inline=True)
    embed.add_field(name='Rating', value=rating, inline=False)
    embed.add_field(name='Upvotes', value=post['up_score'], inline=True)
    embed.add_field(name='Downvotes', value=post['down_score'], inline=True)
    embed.add_field(name='Favorites', value=post['fav_count'], inline=True)
    embed.add_field(name='Artist', value=post['tag_string_artist'], inline=True)
    embed.add_field(name='Pixiv ID', value=post['pixiv_id'], inline=True)
    embed.add_field(name='Post Date', value=f"{post['created_at'].split('T')[0]} at {post['created_at'].split('T')[1]}", inline=False)
    embed.add_field(name='Size', value=f'{post["image_width"]} x {post["image_height"]}', inline=False)

import logging
import re

bot_url = 'https://i.redd.it/74tcw6iq1k161.jpg'
ina_url = 'https://preview.redd.it/307b6pt6tfx61.jpg?width=232&format=pjpg&auto=webp&s' \
          '=ef88bc0611dc25cbf388b5717b3ab4801401a614 '
megumin_url = 'https://static.wikia.nocookie.net/rehero/images/4/44/Megumin.jpg/revision/latest/scale-to-width-down' \
              '/310?cb=20180330001646 '
aqua_url = 'https://danbooru.donmai.us/data/sample/bb/9d' \
           '//__aqua_kono_subarashii_sekai_ni_shukufuku_wo_drawn_by_kuro_mushi__sample' \
           '-bb9d727bf996c86554dce5c2cb9198e7.jpg '
darkness_url = "https://danbooru.donmai.us/data/original/98/29" \
               "/__darkness_kono_subarashii_sekai_ni_shukufuku_wo_drawn_by_lambda_kusowarota__9829baa99fcbf3b61ac2552ecdb34824.jpg "

banned_tags = 'male_focus'
feet_pattern = '[fF].{2}[eE]*.{0,1}[tT]'
accepted_file_types = '(png|jpg|gif)'
cumb_pattern = '[cC].{0,1}[uUoO]*.{0,1}[mM]'


def logg():
    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S',
                        level=logging.DEBUG,
                        filename='logs.txt')


def helper(embed):
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


def cum():
    borpa = "<:Borpa:838413361603018792>"
    f = (f"{borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM \n"
         f"{borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM \n"
         f"{borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM \n"
         f"{borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM {borpa} CUM ")
    return f


def feet():
    f = ("***SNIFFFFFFFFFFFFFFFFFFFFFFFFFFF***\n"
         "***...breathing heavily...***\n"
         "***I LOVE FEET***")
    return f


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
    if post[n]['tag_string_character']:
        embed.add_field(name='Character', value=post[n]['tag_string_character'].split(' ')[0], inline=True)
    else:
        embed.add_field(name='Character', value='Original', inline=True)
    embed.add_field(name='Rating', value=rating, inline=True)
    embed.add_field(name='Upvotes', value=post[n]['up_score'], inline=True)
    embed.add_field(name='Downvotes', value=post[n]['down_score'], inline=True)
    logg()

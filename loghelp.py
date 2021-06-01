# import logging
# import json
# import random


# def logg():
#     logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#                         datefmt='%d-%m-%Y:%H:%M:%S',
#                         level=logging.DEBUG,
#                         filename='logs.txt')
#
#
# def saver(post, n):
#     with open('saving.json', 'r') as f:
#         data = json.load(f)
#         char = dict(Character=post[n]["tag_string_character"].split(" ")[0], Rating=post[n]["rating"],
#                     ImageUrl=post[n]["file_url"], Upvotes=post[n]['up_score'], id=post[n]['id'])
#         data['Tags'].append(char)
#     with open('saving.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# def opener(character='keqing_(genshin_impact)'):
#     rat = []
#     with open('saving.json', 'r') as f:
#         data = json.load(f)
#         w = len(data['Tags'])
#     for p in range(0, w):
#         res = data['Tags'][p]
#         if res['Character'] in character:
#             rat.append(res)
#     elem = random.randint(0, len(rat)-1)
#     return rat[elem]

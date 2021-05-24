import logging
import ast
import random


def logg():
    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S',
                        level=logging.DEBUG,
                        filename='logs.txt')


def saver(post, n):
    try:
        data = dict(Character=post[n]["tag_string_character"].split(" ")[0], Rating=post[n]["rating"],
                    ImageUrl=post[n]["file_url"], Upvotes=post[n]['up_score'])
        with open('saving.txt', 'a+') as f:
            f.write(f'{data}\n')
    except ValueError:
        pass


def opener(character='keqing_(genshin_impact)'):
    w = len(open('saving.txt').readlines())
    rat = []
    with open('saving.txt', 'r+') as f:
        lines = [line[:-1] for line in f]
        for p in range(0, w):
            res = ast.literal_eval(lines[p])
            if res['Character'] in character:
                rat.append(res)
    elem = random.randint(0, len(rat)-1)
    return rat[elem]



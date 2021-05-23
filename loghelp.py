import logging


def logg():
    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%d-%m-%Y:%H:%M:%S',
                        level=logging.DEBUG,
                        filename='logs.txt')


def saver(post, n):
    try:
        data = dict(Character=post[n]["tag_string_character"].split(" ")[0], Rating=post[n]["rating"],
                    ImageUrl=post[n]["file_url"])
        with open('saving.txt', 'a+') as f:
            f.write(f'{data}\n')
    except ValueError:
        pass


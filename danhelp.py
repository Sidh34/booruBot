from pybooru import Danbooru
import PARAMETERS
from functools import lru_cache

cli = Danbooru('danbooru', username=PARAMETERS.DANBOORU_USER, api_key=PARAMETERS.DANBOORU_TOKEN)


@lru_cache(maxsize=20)
def small_post_getter(tags):
    posts = cli.post_list(tags=f'{tags}', limit=2)
    return posts


@lru_cache(maxsize=250)
def large_post_getter(tags):
    posts = cli.post_list(tags=f'{tags}', limit=100)
    return posts


@lru_cache(maxsize=250)
def random_post_getter(tags):
    posts = cli.post_list(tags=f'{tags}', limit=100, random=True)
    return posts


@lru_cache(maxsize=100)
def id_post_getter(identity):
    posts = cli.post_show(identity)
    return posts


def small_random_post_getter():
    posts = cli.post_list(limit=1, tags='-boys_only', random=True)
    return posts


def popular_post_getter(page):
    posts = cli.post_list(limit=2, tags='order:rank', page={page})
    return posts

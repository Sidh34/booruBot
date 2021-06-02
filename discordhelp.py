import discord
from discord.ext import commands
from embeder import *
from operator import itemgetter

server = discord.Client()
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='?', intents=intents)
no_dupe = []


def tagged_disc_embed(posts, n):
    e = discord.Embed(title='Tagged', color=0x0e0de6)  # saver
    image_embed_multiple(e, posts, n)
    no_dupe.append(posts[n]['id'])
    if len(no_dupe) > 15:
        no_dupe.pop(0)
    return e


def ran_tagged_discord_embed(posts, n, rating):
    if rating == 's':
        e = discord.Embed(title='Tagged Safe', color=0x2ae20c)  # saver
        image_embed_multiple(e, posts, n)
        no_dupe.append(posts[n]['id'])
        if len(no_dupe) > 15:
            no_dupe.pop(0)
    elif rating == 'q':
        e = discord.Embed(title='Tagged Questionable', color=0x2ae20c)  # saver
        image_embed_multiple(e, posts, n)
        no_dupe.append(posts[n]['id'])
        if len(no_dupe) > 15:
            no_dupe.pop(0)
    elif rating == 'e':
        e = discord.Embed(title='Tagged Explicit', color=0x2ae20c)  # saver
        image_embed_multiple(e, posts, n)
        no_dupe.append(posts[n]['id'])
        if len(no_dupe) > 15:
            no_dupe.pop(0)
    return e


def order_rank_discord_embed(post, n):
    e = discord.Embed(title='Popular Post', color=0xFF00FF)  # saver
    image_embed_multiple(e, post, n)
    return e


def tagged_popular_discord_embed(s_u, n):
    e = discord.Embed(title='Popular Tagged', color=0x2ae20c)  # saver
    image_embed_multiple(e, s_u[n], 0)
    no_dupe.append(s_u[n][0]['id'])
    if len(no_dupe) > 15:
        no_dupe.pop(0)
    return e


def tagged_pop_rate_discord_embed(rating, s_u, n):
    if rating == 's':
        e = discord.Embed(title='Most Popular Safe Tagged', color=0x2ae20c)  # saver
        image_embed_multiple(e, s_u[n], 0)
        no_dupe.append(s_u[n][0]['id'])
        if len(no_dupe) > 15:
            no_dupe.pop(0)
    elif rating == 'q':
        e = discord.Embed(title='Most Popular Questionable Tagged', color=0x2ae20c)  # saver
        image_embed_multiple(e, s_u[n], 0)
        no_dupe.append(s_u[n][0]['id'])
        if len(no_dupe) > 15:
            no_dupe.pop(0)
    elif rating == 'e':
        e = discord.Embed(title='Most Popular Explicit Tagged', color=0x2ae20c)  # saver
        image_embed_multiple(e, s_u[n], 0)
        no_dupe.append(s_u[n][0]['id'])
        if len(no_dupe) > 15:
            no_dupe.pop(0)
    return e


def sun(posts):
    updoot = []
    try:
        for n in range(0, 100):
            updoot.append(posts[n]['up_score'])
    except IndexError:
        pass
    tied = tuple(zip(posts, updoot))
    s_u = sorted(tied, key=itemgetter(1))
    s_u.reverse()
    return s_u

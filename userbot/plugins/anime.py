"""
Get information about anime, manga or characters from [MyAnimeList](https://myanimelist.net).
──「 **Anime** 」──
-> `sanime <anime>`
returns information about the anime.
__Original Module by @Zero_cooll7870__
──「 **Character** 」──
-> `scharacter <character>`
returns information about the character.
──「 **Manga** 」──
-> `manga <manga>`
returns information about the manga.
──「 **Upcoming Anime** 」──
-> `upcoming`
returns a list of new anime in the upcoming seasons.

"""
from telethon import events
import asyncio
import os
import sys
import random
from userbot.utils import admin_cmd
from jikanpy import Jikan
from jikanpy.exceptions import APIException
import requests
import json

jikan = Jikan()


async def anime_call_api(search_str):
    query = '''
    query ($id: Int,$search: String) {
      Media (id: $id, type: ANIME,search: $search) {
        id
        title {
          romaji
          english
        }
        description (asHtml: false)
        startDate{
            year
          }
          episodes
          chapters
          volumes
          season
          type
          format
          status
          duration
          averageScore
          genres
          bannerImage
      }
    }
    '''
    variables = {
        'search' : search_str
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})
    return response.text


async def formatJSON(outData):
    msg = ""
    jsonData = json.loads(outData)
    res = list(jsonData.keys())
    if "errors" in res:
        msg += f"**Error** : `{jsonData['errors'][0]['message']}`"
        return msg
    else:
        jsonData = jsonData['data']['Media']
        if "bannerImage" in jsonData.keys():
            msg += f"[💮]({jsonData['bannerImage']})"
        else:
            msg += "💮"
        title = jsonData['title']['romaji']
        link = f"https://anilist.co/anime/{jsonData['id']}"
        msg += f"[{title}]({link})"
        msg += f"\n\n**Type** : {jsonData['format']}"
        msg += f"\n**Genres** : "
        for g in jsonData['genres']:
            msg += g+" "
        msg += f"\n**Status** : {jsonData['status']}"
        msg += f"\n**Episode** : {jsonData['episodes']}"
        msg += f"\n**Year** : {jsonData['startDate']['year']}"
        msg += f"\n**Score** : {jsonData['averageScore']}"
        msg += f"\n**Duration** : {jsonData['duration']} min"
        msg += f"\n\n __{jsonData['description']}__"
        return msg


@borg.on(admin_cmd(pattern=r"sanime"))
async def anime(_client, message):
    cmd = message.command
    query = ""
    if len(cmd) > 1:
        query = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        query = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit("`cant find anime.`")
        await asyncio.sleep(2)
        await message.delete()
        return
    result = await anime_call_api(query)
    msg = await formatJSON(result)
    await message.edit(msg, disable_web_page_preview=False)



@borg.on(admin_cmd(pattern=r"scharacter"))
async def character(_client, message):
    res = ""
    cmd = message.command
    query = ""
    if len(cmd) > 1:
        query = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        query = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit("`cant find character.`")
        await asyncio.sleep(2)
        await message.delete()
        return
    try:
        search = jikan.search("character", query).get("results")[0].get("mal_id")
    except APIException:
        message.edit("No results found!")
        return ""
    if search:
        try:
            res = jikan.character(search)
        except APIException:
            message.edit("Error connecting to the API. Please try again!")
            return ""
    if res:
        name = res.get("name")
        kanji = res.get("name_kanji")
        about = res.get("about")
        if len(about) > 4096:
            about = about[:4000] + "..."
        image = res.get("image_url")
        url = res.get("url")
        rep = f"<b>{name} ({kanji})</b>\n\n"
        rep += f"<a href='{image}'>\u200c</a>"
        rep += f"<i>{about}</i>\n"
        rep += f'Read More: <a href="{url}">MyAnimeList</a>'
        await message.edit(replace_text(rep))

@borg.on(admin_cmd(pattern=r"manga"))
async def manga(_client, message):
    cmd = message.command
    query = ""
    if len(cmd) > 1:
        query = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        query = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit("`cant find manga.`")
        await asyncio.sleep(2)
        await message.delete()
        return
    res = ""
    manga = ""
    try:
        res = jikan.search("manga", query).get("results")[0].get("mal_id")
    except APIException:
        await message.edit("Error connecting to the API. Please try again!")
        return ""
    if res:
        try:
            manga = jikan.manga(res)
        except APIException:
            message.edit("Error connecting to the API. Please try again!")
            return ""
        title = manga.get("title")
        japanese = manga.get("title_japanese")
        type = manga.get("type")
        status = manga.get("status")
        score = manga.get("score")
        volumes = manga.get("volumes")
        chapters = manga.get("chapters")
        genre_lst = manga.get("genres")
        genres = ""
        for genre in genre_lst:
            genres += genre.get("name") + ", "
        genres = genres[:-2]
        synopsis = manga.get("synopsis")
        image = manga.get("image_url")
        url = manga.get("url")
        rep = f"<b>{title} ({japanese})</b>\n"
        rep += f"<b>Type:</b> <code>{type}</code>\n"
        rep += f"<b>Status:</b> <code>{status}</code>\n"
        rep += f"<b>Genres:</b> <code>{genres}</code>\n"
        rep += f"<b>Score:</b> <code>{score}</code>\n"
        rep += f"<b>Volumes:</b> <code>{volumes}</code>\n"
        rep += f"<b>Chapters:</b> <code>{chapters}</code>\n\n"
        rep += f"<a href='{image}'>\u200c</a>"
        rep += f"<i>{synopsis}</i>"
        rep += f'Read More: {url}'
        await message.edit(rep)

@borg.on(admin_cmd(pattern=r"upcoming"))
async def upcoming(_client, message):
    rep = "<b>Upcoming anime</b>\n"
    later = jikan.season_later()
    anime = later.get("anime")
    for new in anime:
        name = new.get("title")
        url = new.get("url")
        rep += f"• <a href='{url}'>{name}</a>\n"
        if len(rep) > 1000:
            break
    await message.edit(rep, parse_mode='html')

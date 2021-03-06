import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("β‘")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>π πΏπΎπ½πΆ</b> `{delta_ping * 1000:.3f} ms` \n<b>β³ π°π²ππΈππ΄</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**β α΄sα΄ΚΚα΄α΄ Κα΄sα΄α΄Κα΄α΄α΄**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>β€οΈ Κα΄ΚΚα΄ {m.from_user.mention}!

π   Hα΄Κα΄ Mα΄Ι΄α΄

Β» α΄α΄α΄α΄α΄Ι΄α΄s ?α΄Κ α΄α΄ α΄ΚΚα΄Ι΄α΄

β’ {HNDLR}α΄Κα΄Κ [sα΄Ι΄Ι’ α΄Ιͺα΄α΄Κ|Κα΄α΄α΄α΄Κα΄ ΚΙͺΙ΄α΄| Κα΄α΄ΚΚ α΄α΄α΄Ιͺα΄-?ΙͺΚα΄] - Tα΄ α΄Κα΄Κ α΄Κα΄ sα΄Ι΄Ι’
β’ {HNDLR}α΄ α΄Κα΄Κ [α΄ Ιͺα΄α΄α΄ α΄Ιͺα΄Κα΄| Κα΄α΄α΄α΄Κα΄ ΚΙͺΙ΄α΄ | Κα΄α΄ΚΚ α΄ Ιͺα΄α΄α΄ ?ΙͺΚα΄] - α΄α΄ α΄Κα΄Κ α΄ Ιͺα΄α΄α΄ 
β’ {HNDLR}α΄Κα΄ΚΚΙͺsα΄ α΄α΄ α΄ Ιͺα΄α΄‘ α΄ Ιͺα΄α΄α΄ 
β’ {HNDLR}α΄ΙͺΙ΄Ι’ - α΄α΄ α΄Κα΄α΄α΄ sα΄α΄α΄α΄s
β’ {HNDLR}Κα΄Κα΄ - α΄α΄ α΄ Ιͺα΄α΄‘ α΄ ΚΙͺsα΄ α΄? α΄α΄α΄α΄α΄Ι΄α΄

Β»α΄α΄α΄α΄α΄Ι΄α΄s α΄α΄Κ α΄ΚΚ α΄α΄α΄ΙͺΙ΄s

β’ {HNDLR}Κα΄sα΄α΄α΄ - α΄α΄ α΄α΄Ι΄α΄ΙͺΙ΄α΄α΄ α΄Κα΄ΚΙͺΙ΄Ι’ α΄Κα΄ sα΄Ι΄Ι’ α΄Κ α΄ Ιͺα΄α΄α΄ 
β’ {HNDLR}α΄α΄α΄sα΄ - α΄α΄ α΄α΄α΄sα΄ α΄Κα΄ α΄Κα΄ΚΚα΄α΄α΄ α΄? α΄ sα΄Ι΄Ι’ α΄Κ α΄ Ιͺα΄α΄α΄ 
β’ {HNDLR}sα΄Ιͺα΄ - α΄α΄ sα΄Ιͺα΄ α΄ sα΄Ι΄Ι’ α΄Κ α΄ Ιͺα΄α΄α΄ 
β’ {HNDLR}α΄Ι΄α΄ - α΄α΄ α΄Ι΄α΄ α΄Κα΄ΚΚα΄α΄α΄ </b>
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["repo", "sumit", "openbaby"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>β€οΈ Κα΄ΚΚα΄ {m.from_user.mention}!
      βͺ MusicMeliodasV1 βͺ

 α΄α΄Κα΄Ι’Κα΄α΄ Usα΄ΚΚα΄α΄ α΄α΄ α΄Κα΄Κ sα΄Ι΄Ι’s α΄Ι΄α΄ α΄ Ιͺα΄α΄α΄s ΙͺΙ΄ α΄α΄Κα΄Ι’Κα΄α΄ α΄ α΄Ιͺα΄α΄ α΄Κα΄α΄ α΄α΄α΄ α΄Κα΄α΄α΄α΄.

Β» α΄ΚΙͺα΄α΄ Κα΄α΄ α΄Κ sα΄Κsα΄ΚΙͺΚα΄ α΄Κα΄Ι΄Ι΄α΄Κ
β’ [α΄α΄Ι΄α΄Ι’α΄ Κα΄α΄](https://t.me/Knoxzx)
β’ [α΄Κα΄Ι΄Ι΄α΄Κ](https://t.me/OfficiallMeliodas)


Β»  βͺ α΄α΄ΙͺΙ΄ sα΄α΄α΄α΄Κα΄ Ι’Κα΄α΄α΄ βͺ
 β’ ?ΙͺΚsα΄ α΄α΄ΙͺΙ΄ sα΄α΄α΄α΄Κα΄ Ι’Κα΄α΄α΄ α΄Ι΄α΄ α΄Κα΄Ι΄ α΄Κα΄α΄ #Meliodas-Music-Userbot
Β» sα΄α΄α΄α΄Κα΄ Ι’Κα΄α΄α΄ || [sα΄α΄α΄α΄Κα΄](https://t.me/+2zyDnYSSA844MzE1) 
 
 </b>
"""
    await m.reply(REPO, disable_web_page_preview=True)

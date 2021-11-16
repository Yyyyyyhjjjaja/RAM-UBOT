from userbot.utils import command, remove_plugin, load_module
from pathlib import Path
import asyncio
import os
from datetime import datetime

DELETE_TIMEOUT = 5


@command(pattern="^.install", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "userbot/modules/"  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit("Installed Plugin `{}`".format(os.path.basename(downloaded_file_name)))
            else:
                os.remove(downloaded_file_name)
                await event.edit("Errors! This plugin is already installed/pre-installed.")
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@command(pattern=r"^.send (?P<shortname>\w+)$", outgoing=True)
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./userbot/modules/{}.py".format(input_str)
    start = datetime.now()
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        force_document=True,
        allow_cache=False,
        reply_to=message_id
    )
    end = datetime.now()
    time_taken_in_ms = (end - start).seconds
    await event.edit("Uploaded {} in {} seconds".format(input_str, time_taken_in_ms))
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@command(pattern=r"^.unload (?P<shortname>\w+)$", outgoing=True)
async def unload(event):
 CHAT TO CALZ ANGELS
Tiaraa ᥴꪖ ༊:
Pey ngambek anjj

Lu siii ngajak tmoan

icaaa ᥴꪖ ༊:
tolol

yagahahaha

lo juga ikut bae

Tiaraa ᥴꪖ ༊:
Dia bilng

"udh lu gausa ganggu gua dulu"

Gtuuu😭

Nyampe skrng ga cht cht

Hel ᥴꪖ ༊:
Anjort

Crtanya lgi break nih?

glo ᥴꪖ ༊:
hii gess

icaaa ᥴꪖ ༊:
YAHSHAHA

glo ᥴꪖ ༊:
oit

icaaa ᥴꪖ ༊:
kliling yu

Tiaraa ᥴꪖ ༊:
Naik publik

icaaa ᥴꪖ ༊:
@joinsinitodd

𝐁𝐎𝐓 𝐀𝐍𝐆𝐄𝐋𝐒:
Welkaaamm Cantik Farida

Lalaapoooo:
Hayuuuu

icaaa ᥴꪖ ༊:
.

Lalaapoooo:
Buruu

Hel ᥴꪖ ༊:
Ntar gw silah dulu

Lalaapoooo:
Lahhh tmonya di udahi

n

icaaa ᥴꪖ ༊:
ayo naik

buru

angkat ketek😭

koo dipilih tod😭😭

Lalaapoooo:
Hahaha ngakak anj di pilih

Hhahaahha

icaaa ᥴꪖ ༊:
je pilih jaki

Lalaapoooo:
Yang mnaa

icaaa ᥴꪖ ༊:
jakipan

Lalaapoooo:
Mnaaa naikin mknyaaa anj ko ga naik naik

icaaa ᥴꪖ ༊:
sabarr tod

Lalaapoooo:
Hhaahah ngakak

icaaa ᥴꪖ ༊:
ntr gua pasti roast di call sm jaki😭😭

TOLOL NGENTOD

nama siapa asal dimana umur berapa

malah nanya ngntf

Lalaapoooo:
Hahaha ngakak anj😭😭😭😭😭

icaaa ᥴꪖ ༊:
ganti akun yu😭

milih lagi😭

TOLOL MINTA Mute😭

Lalaapoooo:
Ywdaa gassssssss

Hahaha

icaaa ᥴꪖ ༊:
gua pake tell. akun ini gbsa gnti pp lg ajg delay

hayuu je

Tiaraa ᥴꪖ ༊:
Lemott guaaa

Waitt

icaaa ᥴꪖ ༊:
yu angkat

ngentod lagi nanya☺️

Tiaraa ᥴꪖ ༊:
Di taekin langsung anj

Anj di skip sama yng jlk

icaaa ᥴꪖ ༊:
HAHAHAHAGAHA

wibu skip gua☺️

Tiaraa ᥴꪖ ༊:
Ngentodddd

Hahahahahaha

icaaa ᥴꪖ ༊:
@algeriozleader

jamet dl

Tiaraa ᥴꪖ ༊:
Udhh naik

Eh salah akun

icaaa ᥴꪖ ༊:
tolol

mau pilih log rush ah

Lalaapoooo:
Naik ga ni

icaaa ᥴꪖ ༊:
naik dong

Lalaapoooo:
Gua pilih sape annnj

icaaa ᥴꪖ ༊:
ntr gua cariin

rzor tuu

eh turun

host nya

Lalaapoooo:
Ada ada

Orgnya jelek kalo dia skip gua katain

Hahahaha

icaaa ᥴꪖ ༊:
ngntd😭😭

Lalaapoooo:
Naikin yang ga angkat tangan babi

icaaa ᥴꪖ ༊:
kntl emg

gua pc ah adminnya

Lalaapoooo:
Lamaaa ah babiii

icaaa ᥴꪖ ༊:
gua pc

Lalaapoooo:
Mentang mentang gua jele

icaaa ᥴꪖ ༊:
iyaa ajg

mending pc☺️

najisss nadanya kek males😱

Lalaapoooo:
Haahahaha

Ngakka

Mampusss

icaaa ᥴꪖ ༊:
pc dlu emm

Lalaapoooo:
Males anjj

icaaa ᥴꪖ ༊:
di bles ajg😭

Lalaapoooo:
Hah seriuss

Bhaks

Maless ah anjjj gua pake akun pinjol wait

icaaa ᥴꪖ ༊:
udah gua pc in ajg

sabar

katanya abis ini lo

Tiaraa ᥴꪖ ༊:
Hhaaahah 😭😭

Ngebugg hp gua

Anjinggggg dahla

Kesel
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Unloaded {shortname} successfully")
    except Exception as e:
        await event.edit("Successfully unload {shortname}\n{}".format(shortname, str(e)))


@command(pattern=r"^.load (?P<shortname>\w+)$", outgoing=True)
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded {shortname}")
    except Exception as e:
        await event.edit(f"Could not load {shortname} because of the following error.\n{str(e)}")

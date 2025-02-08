# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from __future__ import unicode_literals

import os, requests, asyncio, math, time, wget
from pyrogram import filters, Client
from pyrogram.types import Message
from info import CHNL_LNK
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL


@Client.on_message(filters.command(['song', 'mp3']) & filters.private)
async def song(client, message):
    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = await message.reply(f"**ѕєαrchíng чσur ѕσng...!\n {query}**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        performer = f"[NETWORKS™]" 
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
    except Exception as e:
        print(str(e))
        return await m.edit("Example: /song vaa vaathi song")
                
    await m.edit("**dσwnlσαdíng чσur ѕσng...!**")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        cap = f"**BY›› [UPDATE]({CHNL_LNK})**"
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        await message.reply_audio(
            audio_file,
            caption=cap,            
            quote=False,
            title=title,
            duration=dur,
            performer=performer,
            thumb=thumb_name
        )            
        await m.delete()
    except Exception as e:
        await m.edit("**🚫 𝙴𝚁𝚁𝙾𝚁 🚫**")
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

def get_text(message: Message) -> [None,str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None


@Client.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    urlissed = get_text(message)
    pablo = await client.send_message(message.chat.id, f"**𝙵𝙸𝙽𝙳𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚅𝙸𝙳𝙴𝙾** `{urlissed}`")
    if not urlissed:
        return await pablo.edit("Example: /video Your video link")     
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        return await pablo.edit_text(f"**𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙵𝚊𝚒𝚕𝚎𝚍 𝙿𝚕𝚎𝚊𝚜𝚎 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗..♥️** \n**Error :** `{str(e)}`")       
    
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"""**𝚃𝙸𝚃𝙻𝙴 :** [{thum}]({mo})\n**𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :** {message.from_user.mention}"""

    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,        
        reply_to_message_id=message.id 
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)

# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.youtube.com	TRUE	/	TRUE	1773592431	PREF	f6=40000000&tz=Asia.Calcutta&f7=100&f5=30000
.youtube.com	TRUE	/	TRUE	1770567308	__Secure-1PSIDTS	sidts-CjIBmiPuTUYc7bmDcZv3SuJ1rKsM-l3gfhLsViBwpjNQezDSdl8ecyJFEG63t86egO5BIRAA
.youtube.com	TRUE	/	TRUE	1770567308	__Secure-3PSIDTS	sidts-CjIBmiPuTUYc7bmDcZv3SuJ1rKsM-l3gfhLsViBwpjNQezDSdl8ecyJFEG63t86egO5BIRAA
.youtube.com	TRUE	/	FALSE	1773591308	HSID	AXH6E613L3_KSTr7_
.youtube.com	TRUE	/	TRUE	1773591308	SSID	AFqvQ6M2OJVsDjcdY
.youtube.com	TRUE	/	FALSE	1773591308	APISID	wOVLl-s8_H47UQTW/Adjva-n5LZ5wsZt7j
.youtube.com	TRUE	/	TRUE	1773591308	SAPISID	0iBM2JAoqpYmytP8/AtxVBF3JpyCrHYLuJ
.youtube.com	TRUE	/	TRUE	1773591308	__Secure-1PAPISID	0iBM2JAoqpYmytP8/AtxVBF3JpyCrHYLuJ
.youtube.com	TRUE	/	TRUE	1773591308	__Secure-3PAPISID	0iBM2JAoqpYmytP8/AtxVBF3JpyCrHYLuJ
.youtube.com	TRUE	/	FALSE	1773591308	SID	g.a000tQjlj7ChRVM2SSKjE07B3G7OC8ZnVE-ZqKyEVo6YA65ucsLsZCADkY75ug7EErh0W9WAGgACgYKAfUSARQSFQHGX2Mi3u-OBALvLlJz2lqCXj0TZBoVAUF8yKoNhPf-mvFJ88c7NwcU89xI0076
.youtube.com	TRUE	/	TRUE	1773591308	__Secure-1PSID	g.a000tQjlj7ChRVM2SSKjE07B3G7OC8ZnVE-ZqKyEVo6YA65ucsLsB3lErZArs_uf65D6CXh7pAACgYKAZESARQSFQHGX2MikSifl9nEK-GJxHlDMVlSXxoVAUF8yKrQbHZR6ljt99-OpjR9ykUe0076
.youtube.com	TRUE	/	TRUE	1773591308	__Secure-3PSID	g.a000tQjlj7ChRVM2SSKjE07B3G7OC8ZnVE-ZqKyEVo6YA65ucsLsqO8wFjQdpD6KWtLDvwIUWgACgYKAZcSARQSFQHGX2MiQdxtlBPLIAo3oClge3sWJxoVAUF8yKoJn4uWlD5-R6Bz3_sDvi6z0076
.youtube.com	TRUE	/	TRUE	1773591329	LOGIN_INFO	AFmmF2swRQIgC4wzFaDA7bGVTiw7p9tSFQlWQ9g9IDjTeI9-4oa6jhsCIQDRBKJhHF_eqd-JagikvgFdouSyeZ2Lmw_8wYCrCv8ArA:QUQ3MjNmeVJVdHkyNFQySnprLURTLTB6bmFkRDNnaHR6dDBsYll5SHZXTDVsYjZxc3V1VjVBRS1Sek9KTC1lTzFNOHFUN3JrR3QtTGFNSEZjUms5OGx4eFZLcGRYMGtpeHJpSWt2SUVLenBqQko5OHp2UkFRYmlic21zTGI3c2hZX1hCb19BSWMzWGR1UlF2a2NleElBc3VPN3dGcXFDcDFB
.youtube.com	TRUE	/	TRUE	1739032561	CONSISTENCY	AKreu9uA5bGQ41gCKtH_F4xJI5O7-nG5TIZSEorHAbJJ8zDePqio9dVCy9oILQijFgd6ReDB7rDgw6PwZI0fPd5Lt_NDXCGOM64hgouEO0fPPo3ePYzfa2dXwr0
.youtube.com	TRUE	/	FALSE	1770568435	SIDCC	AKEyXzWrPez2YuXICWf6ZVxJZnK20CPOd45SN6G1AkQVEkfHzHcd6Mvj3MxmFkJm0qFE1RC9
.youtube.com	TRUE	/	TRUE	1770568435	__Secure-1PSIDCC	AKEyXzVkk9GzVkFrbwjI8NLn-OyCGBtHMKylVKenx01nMCurrYSB3xEK_5BJ-NL5YKi78M-6
.youtube.com	TRUE	/	TRUE	1770568435	__Secure-3PSIDCC	AKEyXzVYESSWs1tyX_fQnwMbdSm2FK7pWd_teVhTRuh8uwUffzZEwpELvJ-os4q6TIoRMOHF

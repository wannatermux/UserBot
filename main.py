#!/usr/bin/python
# -*- coding: utf-8 -*-
import pip

# Проверка библиотек
try:
    import time, random, datetime, asyncio, sys, wikipedia, logging, aiohttp, pyrogram, os, wget, bs4, requests, gtts, colorama, youtube_dl, db0mb3r, configparser
except ModuleNotFoundError:
    print("Установка дополнений...\n")
    pip.main(['install', 'tgcrypto'])
    pip.main(['install', 'pyrogram'])
    pip.main(['install', 'aiohttp'])
    pip.main(['install', 'wikipedia'])
    pip.main(['install', 'logging'])
    pip.main(['install', 'wget'])
    pip.main(['install', 'bs4'])
    pip.main(['install', 'requests'])
    pip.main(['install', 'gtts'])
    pip.main(['install', 'colorama'])
    pip.main(['install', 'youtube_dl'])
    pip.main(['install', 'db0mb3r'])
    pip.main(['install', 'configparser'])
    import os
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

# Проверка конфига
config = os.path.exists('config.ini')
if config == True:
    print("work")
else:
    with open("config.ini", "w+") as f:
        rep = """[pyrogram]
api_id = 2860432
api_hash = 2fde6ca0f8ae7bb58844457a239c7214
device_model = subscribe t.me/privatesoft0|

"""
        repo = str(rep)
        f.write(repo)
        f.close()

from pyrogram import Client, filters
from pyrogram.errors import FloodWait, ChatSendMediaForbidden
from pyrogram.types import Message, ChatPermissions
from pyrogram.handlers import MessageHandler
from pyrogram.methods.chats.get_chat_members import Filters as ChatMemberFilters
from time import sleep, perf_counter, time
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import time, random, datetime, asyncio, sys, wikipedia, requests, json, colorama, requests, youtube_dl, subprocess, configparser
from gtts import gTTS

start = os.path.exists('start.ogg')
if start == True:
    print("work...")
else:
    url = 'https://github.com/A9FM/filesUB/blob/main/start.ogg?raw=true'
    wget.download(url, '')

stop = os.path.exists('stop.ogg')
if stop == True:
    print("work...")
else:
    url = 'https://github.com/A9FM/filesUB/blob/main/stop.ogg?raw=true'
    wget.download(url, '')

update = os.path.exists('update.ogg')
if update == True:
    print("work...")
else:
    url = 'https://github.com/A9FM/filesUB/blob/main/update.ogg?raw=true'
    wget.download(url, '')

# Проверка файла репутации
rep = os.path.exists('rep.txt')
if rep == True:
    print("work...")
else:
    with open("rep.txt", "w+") as f:
        rep = "0"
        repo = str(rep)
        f.write(repo)
        f.close()

# Префиксы доп
config_path = os.path.join(sys.path[0], 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)

def get_prefix():
    prefix = config.get("prefix", "prefix")
    return prefix

try:
    prefix = get_prefix()

except Exception as e:
    config.add_section("prefix")
    config.set('prefix', 'prefix', '.')
    with open(config_path, "w") as config_file:
        config.write(config_file)
    prefix = '.'

# Очистка терминала
os.system('cls' if os.name == 'nt' else 'clear')

logo = """\033[31m
  ____ _     ___ _____
 / ___| |   |_ _|  _  |
| |   | |    | || |_) |
| |___| |___ | ||  ___|
 \____|_____|___|_|

\033[34m
Telegram Канал - @privatesoft0
Помощь - @wannatermux
Версия 1.9.1 [РЕЛИЗ]

Логи:"""
print(logo)

# Логи + Вход
app = Client("my_account")
import logging

logi = "╭ Логи\n┃ "

# Вход в группу [Обновления]
with app:
         app.join_chat('privatesoft0') # Прошу, не убирайте эту строку

# Доп код перезагрузка
with app:
         app.unblock_user("ClipUSERBOT_LOGGERbot")
         nowe = datetime.datetime.now()
         timnowe = nowe.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
         startlog = logi + timnowe + "\n╰ Юзербот был запущен"
         app.send_message("ClipUSERBOT_LOGGERbot", startlog)


         if len(sys.argv) == 4:
             try:
                 restart_type = sys.argv[3]
                 if restart_type == '1':
                    app.send_audio(sys.argv[1], "update.ogg", '<code>Обновление завершенно!</code>')
                 else:
                    app.send_audio(sys.argv[1], "start.ogg", '<code>Перезагрузка завершенна!</code>')
             except:
                pass



# Помощь | Инфа про Юзербота
@app.on_message(filters.command("help", prefix) & filters.me)
async def help(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Список комманд"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    await message.edit("""<b><a href="https://t.me/privatesoft0">🤖 UserBot 1.9.1 [РЕЛИЗ] 🤖</a></b>
<b><a href="https://t.me/TransNibber">👨‍💻 Создатель 👨‍💻</a></b>

『Основные』
⇛ <code>help</code> - Помощь | Информация | Проверка версии
⇛ <code>ping</code> - Проверка Пинга Юзербота [Качество полключения]
⇛ <code>restart</code> - Перезагрузка [Ошибка, Баг в Юзерботе]
⇛ <code>update</code> - Обновить
⇛ <code>beta</code> - Обновиться на [РЕЛИЗ]
⇛ <code>sp</code> [Символ] - Смена префикса (знака в начале для комманд)

『Мало временни』
⇛ <code>afk</code> [Причина] - Ввойти в АФК [Не в сети]
⇛ <code>unafk</code> - Выйти из АФК
⇛ <code>wiki</code> [Слово] - Поиск в Википедии
⇛ <code>weather</code> [Город] - Погода

『Троллинг』
⇛ <code>hack</code> - Взлом Пентагонна
⇛ <code>jopa</code> - Взлом жопы
⇛ <code>mum</code> - Поиск матери
⇛ <code>drugs</code> - Принять 3aПрEщEHHblE BещECTBа
⇛ <code>bomber</code> - Запуск Бомбера (Сайт)
⇛ <code>bbomber</code> [Номер без знака +] - Запуск бомбера (боты)
⇛ <code>sbomber</code> - Завершение роботы бомбера

『Плюшки』
⇛ <code>type</code> - Эффект Печати
⇛ <code>hide</code> - Сообщения с Авто-удалением
⇛ <code>sw</code> - Переключение расскладки [Если написали по типу ghbdtn]
⇛ <code>short</code> [Ссылка] - сократитель ссылок
⇛ <code>tagall</code> [Задержка в секундах] - Призыв всех участников
⇛ <code>id</code> - Айди
⇛ <code>info</code> - Информация
⇛ <code>infofull</code> - Полная информация
⇛ <code>qr</code> [Текст] - Создание QR-Кода с вашим текстом
⇛ <code>time</code> - Текущее время
⇛ <code>ladder</code> - текст лесенкой (п пр при прив привет)
⇛ <code>webshot</code> [Ссылка] - Скриншот сайта
⇛ <code>autoread</code> - Авто-чтение (нет уведомлений с этого чата)
⇛ <code>spam</code> [Кол-во смс] [Время между сообщениями в секундах] [Текст сообщения] - Спам
⇛ <code>yt</code> [ссылка] - Скачивание и отправка видео (ютуб, тикток, лайк, инста)
⇛ <code>myt</code> [ссылка] - Скачивание и отправа звука с видео (ютуб, тикток, лайк, инста)
⇛ <code>q</code> [Ответ] - Сделать цитату (Стикер с текстом пользователя)
⇛ <code>spamban</code> [Ответ] - Проверка ограничений
⇛ <code>voice</code> [Текст] - Текст в голосовое
⇛ <code>text</code> [Ответ на голосовое] - Голосовое сообщение в текст
⇛ <code>cl</code> [Текст] - Шифровка текста [Только пользователи CLIP]

『Администрация』
⇛ <code>ban</code> - Бан
⇛ <code>unban</code> - Разбан
⇛ <code>kick</code> - Кик
⇛ <code>mute</code> - Мут
⇛ <code>unmute</code> - Размут
⇛ <code>admin</code> - Выдача прав админа
⇛ <code>unadmin</code> - Разжалование Админа
⇛ <code>invite</code> (Юзейрнейм - @) - Пригласить в чат
⇛ <code>kickall</code> - Удаление всех с чата
⇛ <code>kickall hide</code> - Удаление всех (скрыто)
⇛ <code>leave</code> - Выйти с чата
⇛ <code>pin</code> - Закрепить
⇛ <code>unpin</code> - Открепить

[Репутация, для повышения попросите 2 человека написать вам в ответ сообщение "+"]

Если нужна помощь, пиши @TransNibber""", disable_web_page_preview=True)

async def restart(message: Message, restart_type):
    if restart_type == 'update': text = '1'
    else: text = '2'
    try:
        await os.execvp("python3", ["python3", "bot.py", f"{message.chat.id}",  f" {message.message_id}", f"{text}"])
    except:
        await os.execvp("python", ["python", "bot.py", f"{message.chat.id}",  f" {message.message_id}", f"{text}"])

@app.on_message(filters.command('restart', prefix) & filters.me)
async def restartt(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Юзербот был выключен"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    await message.delete()
    await app.send_audio(message.chat.id, "stop.ogg", '<code>Перезагрузка...</code>')
    await restart(message, restart_type='restart')

@app.on_message(filters.command("update", prefix) & filters.me)
async def updatte(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Юзербот был обновлён"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    await message.edit('<code>Обновление...</code>')
    os.remove("bot.py")
    url = 'https://raw.githubusercontent.com/A9FM/ClipUserbot/main/bot.py'
    wget.download(url, '')
    await restart(message, restart_type='update')

@app.on_message(filters.command("beta", prefix) & filters.me)
async def beta(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Юзербот был обновлён [Бета]"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    await message.edit('<code>Обновление на бета версию...</code>')
    os.remove("bot.py")
    url = 'https://raw.githubusercontent.com/A9FM/ClipUserbot/beta/bot.py'
    wget.download(url, '')
    await restart(message, restart_type='update')

# Префикс
@app.on_message(filters.command("sp", prefix) & filters.me)
async def pref(client: Client, message: Message):
    if len(message.command) > 1:
        prefix = message.command[1]

        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Префикс был сменён на [ " + message.command[1] + " ]"
        await app.send_message("ClipUSERBOT_LOGGERbot", log)

        print(message.command)
        config.set('prefix', 'prefix', prefix)
        with open(config_path, "w") as config_file:
            config.write(config_file)
        await message.edit(f'<b>Префикс [ <code>{prefix}</code> ] установлен!</b>\nПожалуйста, подождите окончания перезагрузки')
        await restart(message, restart_type='restart')
    else:
        await message.edit('<b>Префикс не должен быть пустым!</b>')

# Репутация
@app.on_message(filters.text & filters.incoming & filters.regex('^\-$') & filters.reply)
async def repMinus(client: Client, message: Message):
    try:
        if message.reply_to_message.from_user.is_self:

            now = datetime.datetime.now()
            timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
            l0g = logi + timnow + "\n╰ Репутация была понижена\n\n"

            with open("rep.txt", "r+") as f:
                data = f.read()
                data = int(data)
                num = 1
                rep = data - num
                repo = str(rep)
                f.close()
            with open("rep.txt", "w+") as f:
                repo = str(rep)
                f.write(repo)
                f.close()
                text = "💔 Вы понизили мою репутацию 💔\n🔝 Репутация " + str(repo) + " 🔝"
                await message.reply_text(text)
            log = l0g + "💔 Вы понизили мою репутацию 💔\n🔝 Репутация " + str(repo) + " 🔝"
            await app.send_message("ClipUSERBOT_LOGGERbot", log)
    except:
        pass

@app.on_message(filters.text & filters.incoming & filters.regex('^\+$') & filters.reply)
async def repPlus(client: Client, message: Message):
    try:
        if message.reply_to_message.from_user.is_self:

            now = datetime.datetime.now()
            timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
            l0g = logi + timnow + "\n╰ Репутация была повышена\n\n"

            with open("rep.txt", "r+") as f:
                data = f.read()
                data = int(data)
                num = 1
                rep = data + num
                repo = str(rep)
                f.close()
            with open("rep.txt", "w+") as f:
                repo = str(rep)
                f.write(repo)
                f.close()
                text = "❤️ Вы повысили мою репутацию ❤️\n🔝 Репутация " + str(repo) + " 🔝"
                await message.reply_text(text)
            log = l0g + "❤️ Вы повысили мою репутацию ❤️\n🔝 Репутация " + str(repo) + " 🔝"
            await app.send_message("ClipUSERBOT_LOGGERbot", log)
    except:
        pass

# Айди
@app.on_message(filters.command('id', prefix) & filters.me)
async def id(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда id"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if message.reply_to_message is None:
        await message.edit(f"Айди: {message.chat.id}")
    else:
        id = f"Айди: {message.reply_to_message.from_user.id}\nАйди чата: {message.chat.id}"
        await message.edit(id)

# Бомбер
@app.on_message(filters.command('bomber', prefix) & filters.me)
async def b0mb3r(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запущен бомбер"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    await message.edit("Запускаем бомбер")
    global bombe
    print("""
 _____                 _               
|  _  |               | |              
| |_) | ___  _ __ ___ | |__   ___ _ __ 
|  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|
| |_) | (_) | | | | | | |_) |  __/ |   
|____/ \___/|_| |_| |_|_.__/ \___|_|   
""")

    bombe = subprocess.Popen(["bomber"], stdout=subprocess.PIPE)
    await asyncio.sleep(5)
    await message.edit("Бомбер запущен!\nСсылка: 127.0.0.1:8080")

@app.on_message(filters.command('sbomber', prefix) & filters.me)
async def sbomber(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Бомбер выключен"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    bombe.terminate()
    await message.edit("Бомбер завершил свою роботу...")

@app.on_message(filters.command('bbomber', prefix) & filters.me)
async def bbomber(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ bbomber включён"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    bomber = message.command[1]
    await app.send_message('BomberFree_bot', "/start")
    await app.send_message('couldboombot', "/start")
    await app.send_message('TNT_Robot', "/start")
    await message.edit("Запуск ботов")
    await asyncio.sleep(2)
    await app.send_message('couldboombot', "⚡️Запустить Spam")
    await app.send_message('TNT_Robot', "🧨 Бомбить")
    await asyncio.sleep(2)
    await app.send_message('BomberFree_bot', bomber)
    await app.send_message('couldboombot', bomber)
    await app.send_message('TNT_Robot', bomber + " 15")
    result = "Бомбер запущен на номер " + message.command[1]
    await message.edit(result)

# Время
@app.on_message(filters.command('time', prefix) & filters.me)
async def time(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("%d.%m.%Y\nВремя %H:%M:%S")
    timenow = "Текущая дата : " + timnow
    await message.edit(timenow)

# Читы репутация
@app.on_message(filters.command('rep', prefix) & filters.me)
async def repNakrutka(client: Client, message: Message):
    try:
        with open("rep.txt", "r+") as f:
            data = f.read()
            data = int(data)
            num = message.command[1]
            rep = num
            repo = str(rep)
            f.close()
        with open("rep.txt", "w+") as f:
            repo = str(rep)
            f.write(repo)
            f.close()
            text = "❤️ Репутация изменена ❤️\n🔝 Репутация " + str(repo) + " 🔝"
            await message.edit(text)

        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Накручена репутация\n\n❤️ Репутация изменена ❤️\n🔝 Репутация " + str(repo) + " 🔝"
        await app.send_message("ClipUSERBOT_LOGGERbot", log)
    except:
        pass

# Спам
@app.on_message(filters.command('spam', prefix) & filters.me)
async def spam(client: Client, message: Message):
        if not message.text.split(prefix + 'spam', maxsplit=1)[1]:
                await message.edit('<i>Комманда была введена неправильно</i>')
                return
        count = message.command[1]
        slep = message.command[2]
        text = ' '.join(message.command[3:])
        count = int(count)
        slep = int(slep)
        await message.delete()

        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Запущен спам"
        await app.send_message("ClipUSERBOT_LOGGERbot", log)

        for _ in range(count):
                await app.send_message(message.chat.id, text)
                await asyncio.sleep(slep)

# Скриншот сайта
@app.on_message(filters.command('webshot', prefix) & filters.me)
async def webshot(client, message):
    try:
        if len(message.text.split()) < 2:
            await message.edit('<i>Нету аргументов.</i>')
            return
        user_link = message.command[1]
        await message.delete()
        full_link = 'https://webshot.deam.io/{}/?width=1920&height=1080?type=png'.format(user_link)
        await client.send_photo(message.chat.id, full_link, caption=f'<b> Ссылка ⟶ {user_link}</b>')

        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Скриншот сайта"
        await app.send_message("ClipUSERBOT_LOGGERbot", log)

    except:
        await message.edit('<i>Неизвестный сайт.</i>')

# Видео с ютуб
@app.on_message(filters.command("yt", prefix) & filters.me)
async def yt(client, message):
    linked = message.command[1]

    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на скачивания видео"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    await message.edit("Скачивание видео...")
    ydl_opts = { 'outtmpl': 'video.mp4', }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([linked])
    await message.edit("Отправка видео...")
    await client.send_video(chat_id=message.chat.id, video='video.mp4', caption="Оригинал: " + message.command[1])
    await message.delete()
    os.remove('video.mp4')

@app.on_message(filters.command("myt", prefix) & filters.me)
async def myt(client, message):

    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на скачивание звука"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    myth = "youtube-dl -f 140 " + message.command[1] + " -o music.m4a"
    await message.edit("Скачивание аудиодорожки...")
    os.system(myth)
    await message.edit("Отправка аудиодорожки...")
    await client.send_audio(chat_id=message.chat.id, audio='music.m4a', caption="Звук с видео: " + message.command[1])
    await message.delete()
    os.remove("music.m4a")

# Призыв всех
@app.on_message(filters.command("tagall", prefix) & filters.me)
async def tagall(client, message):

    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Отмечены все участники"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    slep = message.command[1]
    slep = int(slep)
    slepe = str(slep)
    args = ' ! '
    if len(message.text.split()) >= 2:
        args = message.text.split(prefix + 'tagall ' + slepe, maxsplit=1)[1]
    await message.delete()
    chat_id = message.chat.id
    string = ""
    limit = 1
    members = client.iter_chat_members(chat_id)
    async for member in members:
        tag = member.user.username
        if limit <= 9:
            list = ['ᅠ', 'ᅠ']
            if tag != None:
                w = random.choice(list)
                string += f"<a href='https://t.me/{tag}'>{w}</a> "
            else:
                w = random.choice(list)
                string += f"<a href='tg://user?id={member.user.id}'>{w}</a> "
            limit += 1
        else:
            text = f"{args} | {string}"
            await client.send_message(chat_id, text, disable_web_page_preview=1)
            limit = 1
            string = ""
            await asyncio.sleep(slep)

# Удалить смс
@app.on_message(filters.command("del", prefix) & filters.me)
async def delete_messages(client: Client, message: Message):
    if message.reply_to_message:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Удалено сообщение"
        await app.send_message("ClipUSERBOT_LOGGERbot", log)

        message_id = message.reply_to_message.message_id
        await message.delete()
        await client.delete_messages(message.chat.id, message_id)

# Пурдж
@app.on_message(filters.command('purge', prefix) & filters.me)
async def purge(client: Client, message: Message):
        if message.reply_to_message:
                now = datetime.datetime.now()
                timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
                log = logi + timnow + "\n╰ Удаление всех сообщений"
                await app.send_message("ClipUSERBOT_LOGGERbot", log)

                r = message.reply_to_message.message_id
                m = message.message_id
                msgs = []
                await message.delete()
                v = m - r
                while r != m:
                        msgs.append(int(r))
                        r += 1
                await client.delete_messages(message.chat.id, msgs)
                r = message.reply_to_message.message_id
                msgs = []
                while r != m:
                        msgs.append(int(r))
                        r += 1
                await client.delete_messages(message.chat.id, msgs)
                await app.send_message(message.chat.id, f'<b>Удалено > {v} сообщений!</b>')
        else:
                await message.edit('<i>А где реплай?</i>')

# Команда type
@app.on_message(filters.command("type", prefix) & filters.me)
async def type(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Коммада type"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    orig_text = message.text.split(prefix + "type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    while(tbp != orig_text):
        try:
            joper = tbp + typing_symbol
            await message.edit(str(joper))
            await asyncio.sleep(0.10)
            tbp = tbp + text[0]
            text = text[1:]
            await message.edit(str(tbp))
            await asyncio.sleep(0.10)
        except FloodWait as e:
            await asyncio.sleep(e.x)

# Лестница
@app.on_message(filters.command("ladder", prefix) & filters.me)
async def ladder(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда ladder"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    orig_text = message.text.split(prefix + "ladder ", maxsplit=1)[1]
    text = orig_text
    output = []
    for i in range(len(text) + 1):
     output.append(text[:i])
    ot = "\n".join(output)
    await message.edit(ot)

# Quotes
@app.on_message(filters.command("q", prefix) & filters.me)
async def quotly(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit("Ответь на сообщение")
        return

    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Создана цитата"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    await message.edit("Создаю цитату....")
    await message.reply_to_message.forward("QuotLyBot")
    await asyncio.sleep(7)
    iii = await app.get_history("QuotLyBot")
    await message.delete()
    await app.forward_messages(message.chat.id, "QuotLyBot", iii[0].message_id)

# ГС в текст
@app.on_message(filters.command("text", prefix) & filters.me)
async def gstotext(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit("Ответь на сообщение")
        return

    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Переведено голосовое в текст"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    await message.edit("Пишу текстом...")
    await message.reply_to_message.forward("VoiceMsgBot")
    await asyncio.sleep(5)
    iii = await app.get_history("VoiceMsgBot")
    await message.edit("Отправка текста...")
    await app.forward_messages(message.chat.id, "VoiceMsgBot", iii[0].message_id)

# Ограничения
@app.on_message(filters.command("spamban", prefix) & filters.me)
async def spamban(client: Client, message: Message):

    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Проверка нарушений"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    await message.edit("Чекаю твой акк на наличие нарушений")
    await app.send_message('spambot', "/start")
    await asyncio.sleep(1)
    iii = await app.get_history("spambot")
    await message.delete()
    await app.forward_messages(message.chat.id, "spamBot", iii[0].message_id)

# Удаление всех с группы (200 уч лимит) !!! СКРЫТО
@app.on_message(filters.command('kickall hide', prefix) & filters.me)
def kickall(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Удалены участники"
    app.send_message("ClipUSERBOT_LOGGERbot", log)

    message.delete()
    num = 0
    for all in client.iter_chat_members(message.chat.id):
       try:
           num =+ 1
           client.kick_chat_member(message.chat.id, all.user.id, 0)
       except:
           pass

# Удаление всех с группы (200 уч лимит)
@app.on_message(filters.command('kickall', prefix) & filters.me)
def kickall(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Удалены участники"
    app.send_message("ClipUSERBOT_LOGGERbot", log)

    message.edit("Вашим участникам хана)")
    num = 0
    for all in client.iter_chat_members(message.chat.id):
       try:
           num =+ 1
           client.kick_chat_member(message.chat.id, all.user.id, 0)
       except:
           pass

@app.on_message(filters.command("infofull", prefix) & filters.me)
async def info(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Полная информация"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if message.reply_to_message:
        username = message.reply_to_message.from_user.username
        id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        user_link = message.reply_to_message.from_user.mention
        last_name = message.reply_to_message.from_user.last_name
        number = message.reply_to_message.from_user.phone_number
    else:
        username = message.from_user.username
        id = message.from_user.id
        first_name = message.from_user.first_name
        user_link = message.from_user.mention
        last_name = message.from_user.last_name
        number = message.from_user.phone_number

    text = f"""
╭ <b>Информация</b>:
┃ Айди: <code>{id}</code>
┃ Имя: {first_name}
┃ Фамилия: {last_name}
┃ Юзернейм: @{username}
┃ Номер телефонна: {number}
╰ Ссылка: {user_link}"""
    await message.edit(text, parse_mode="HTML")

@app.on_message(filters.command("info", prefix) & filters.me)
async def info(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Информация"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if message.reply_to_message:
        username = message.reply_to_message.from_user.username
        id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        user_link = message.reply_to_message.from_user.mention
    else:
        username = message.from_user.username
        id = message.from_user.id
        first_name = message.from_user.first_name
        user_link = message.from_user.mention

    text = f"""
╭ <b>Информация</b>:
┃ Айди: <code>{id}</code>
┃ Имя: {first_name}
┃ Юзернейм: @{username}
╰ Ссылка: {user_link}"""
    await message.edit(text, parse_mode="HTML")

# Пинг
@app.on_message(filters.command("ping", prefix) & filters.me)
async def ping(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Пинг"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    start = perf_counter()
    await message.edit('Pong')
    end = perf_counter()
    ping2 = end - start
    ping = ping2 * 1000

    if 0 <= ping <= 199:
        await message.edit(f'<b>🏓 Понг\n📶</b> {round(ping)} мс\n🟢Качество соединение: Стабильное🟢')
    if 199 <= ping <= 400:
        await message.edit(f'<b>🏓 Понг\n📶</b> {round(ping)} мс\n🟠Качество соединения: Хорошее🟠')
    if 400 <= ping <= 600:
        await message.edit(f'<b>🏓 Понг\n📶</b> {round(ping)} мс\n🔴Качество соединения: Не стабильное🔴')
    if 600 <= ping:
        await message.edit(f'<b>🏓 Понг\n📶</b> {round(ping)} мс\n⚠Качество соединения: Перепады связи⚠')

# Сократитель ссылок
linkToken = '6c2ac1846a1c1A2d5f88A3E5fbf0e14fcf96d7d0'
async def link_short(link: str):
    async with ClientSession(
        headers={
            'Authorization': f'API-Key {linkToken}'
        }
    ) as ses:
        async with ses.post(
            'https://api.waa.ai/v2/links',
            json={'url': link}
        ) as resp:
            return await resp.json()

@app.on_message(filters.command("short", prefix) & filters.me)
async def shorten_link_command(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Сокращенна ссылка"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if message.reply_to_message:
         link = message.reply_to_message.text
    else:
        try:
            link = message.command[1]
        except IndexError:
            return await message.delete()
    output = (await link_short(link))["data"]
    await message.edit(f'Сокращенная ссылка: {output["link"]}')

# QR-code
content_filter = filters.create(lambda _, __, msg: bool(get_cmd_content(msg)))

def get_cmd_content(message: Message):
    if message.reply_to_message:
        content = message.reply_to_message.text
    elif len(message.text.split(maxsplit=1)) == 2:
        content = message.text.split(maxsplit=1)[1]
    else:
        content = ''
    return content

@app.on_message(filters.command("qr", prefix) & filters.me & content_filter)
async def qr_cmd(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Создан qr-code"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    text = get_cmd_content(message)
    await message.delete()
    async with ClientSession() as session:
        async with session.head('https://api.qrserver.com/v1/create-qr-code/', params={'data': text}) as resp:
            await app.send_photo(
                chat_id=message.chat.id,
                photo=str(resp.url),
                caption=text,
                parse_mode=None,
            )

# Википедия
@app.on_message(filters.command("wiki", prefix) & filters.me)
async def wiki(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Поиск в википедии"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    lang = message.command[1]
    user_request = ' '.join(message.command[2:])
    await message.edit('<b>Ищем инфу</b>')
    if user_request == '':
        wikipedia.set_lang("ru")
        user_request = ' '.join(message.command[1:])
    try:
        if lang == 'en':
            wikipedia.set_lang("en")

        result = wikipedia.summary(user_request)
        await message.edit(f'''<b>Слово:</b>
<code>{user_request}</code>

<b>Значение:</b>
<code>{result}</code>''')
    except Exception as exc:
        await message.edit(f'''<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>''')

# Переклюяение раскладки
@app.on_message(filters.command("sw", prefix) & filters.me)
async def switch(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда sw"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    text = ' '.join(message.command[1:])
    ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
    en_keys = """`qwertyuiop[]asdfghjkl;'zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
    if text == '':
        if message.reply_to_message:
            reply_text = message.reply_to_message.text
            change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
            reply_text = str.translate(reply_text, change)
            await message.edit(reply_text)
        else:
            await message.edit('Текст отсутствует')
            await asyncio.sleep(3)
            await message.delete()
    else:
        change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
        text = str.translate(text, change)
        await message.edit(text)

# Шифровка сообщений
@app.on_message(filters.command("cl", prefix) & filters.me)
async def switch(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда cl"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    text = ' '.join(message.command[1:])
    ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
    en_keys = """異體字体♬♝♞♟γδεηθκλμνZXM∩SάằẫăǽẳßβЂ฿™đďÐðӘҾΣĤĦҤḦĥћҥḧŒœØỢ$śşŝšṧṩᵴﮐ§♌♍♎♏♐♑♒♓✵✶✷✸✹"""
    if text == '':
        if message.reply_to_message:
            reply_text = message.reply_to_message.text
            change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
            reply_text = str.translate(reply_text, change)
            await message.edit(reply_text)
        else:
            await message.edit('Текст отсутствует')
            await asyncio.sleep(3)
            await message.delete()
    else:
        change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
        text = str.translate(text, change)
        await message.edit(text)

# Погода
def get_pic(city):
    file_name = f'{city}.png'
    with open(file_name, 'wb') as pic:
        response = requests.get('http://wttr.in/{citys}_2&lang=ru.png', stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            pic.write(block)
        return file_name

# Погода
@app.on_message(filters.command("weather", prefix) & filters.me)
async def weather(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Погода"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    city = message.command[1]
    await message.edit("```Загрузка...```")
    r = requests.get(f"https://wttr.in/{city}?m?M?0?q?T&lang=ru")
    await message.edit(f"```City: {r.text}```")
    await client.send_photo(chat_id=message.chat.id, photo=get_pic(city), reply_to_message_id=message.message_id)
    os.remove(f'{city}.png')

# Поиск музыки
@app.on_message(filters.command("m", prefix) & filters.me)
async def send_music(client: Client, message: Message):
    try:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Поиск музыки"
        await app.send_message("ClipUSERBOT_LOGGERbot", log)

        cmd = message.command

        song_name = ""
        if len(cmd) > 1:
            song_name = " ".join(cmd[1:])
        elif message.reply_to_message and len(cmd) == 1:
            song_name = (
                message.reply_to_message.text or message.reply_to_message.caption
            )
        elif not message.reply_to_message and len(cmd) == 1:
            await message.edit("Дай мне название музыки")
            await asyncio.sleep(2)
            await message.delete()
            return

        song_results = await app.get_inline_bot_results("deezermusicbot", song_name)

        try:
            # send to Saved Messages because hide_via doesn't work sometimes
            saved = await app.send_inline_bot_result(
                chat_id="me",
                query_id=song_results.query_id,
                result_id=song_results.results[0].id,
                hide_via=True,
            )

            # forward as a new message from Saved Messages
            saved = await app.get_messages("me", int(saved.updates[1].message.id))
            reply_to = (
                message.reply_to_message.message_id
                if message.reply_to_message
                else None
            )
            await app.send_audio(
                chat_id=message.chat.id,
                audio=str(saved.audio.file_id),
                reply_to_message_id=reply_to,
            )

            # delete the message from Saved Messages
            await app.delete_messages("me", saved.message_id)
        except TimeoutError:
            await message.edit("That didn't work out")
            await asyncio.sleep(2)
        await message.delete()
    except Exception as e:
        print(e)
        await message.edit("`Музыка не найденна`")
        await asyncio.sleep(2)
        await message.delete()

# Текст в речь
lang_code = os.environ.get('lang_code', "ru")

@app.on_message(filters.command("voice", prefix) & filters.me)
async def voice(client, message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Текст в голосовое"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if len(message.text.split()) == 1:
        await message.edit(bantuan)
        return
    cust_lang = None
    await message.delete()
    await client.send_chat_action(message.chat.id, "record_audio")
    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang=lang_code)
    tts.save('voice.mp3')
    if message.reply_to_message:
        await client.send_voice(message.chat.id, voice="voice.mp3", reply_to_message_id=message.reply_to_message.message_id)
    else:
        await client.send_voice(message.chat.id, voice="voice.mp3")
    await client.send_chat_action(message.chat.id, action="cancel")
    os.remove("voice.mp3")

# AFK
async def afk_handler(client: Client, message: Message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = (end - start)
        if message.from_user.is_bot is False:
            await message.reply_text(f"<b>Я АФК уже {afk_time}</b>\n"
                                     f"<b>Причина:</b> <i>{reason}</i>")
    except NameError:
        pass

@app.on_message (filters.command("afk", prefix) & filters.me)
async def afk(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Вход в АФК режим"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    global start, end, handler, reason
    start = datetime.datetime.now().replace(microsecond=0)
    handler = client.add_handler(MessageHandler(afk_handler, (filters.private & ~filters.me)))
    if len(message.text.split()) >= 2:
        reason = message.text.split(" ", maxsplit=1)[1]
    else:
        reason = "Неизвестно"
    await message.edit(f"<b>Теперь я АФК</b>\n"
                       f"<b>Причина:</b> <i>{reason}</i>")

# No AFK
@app.on_message (filters.command("unafk", prefix) & filters.me)
async def unafk(client: Client, message: Message):
    try:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Выход с АФК режима"
        await app.send_message("ClipUSERBOT_LOGGERbot", log)

        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = (end - start)
        await message.edit(f"<b>Я теперь не АФК.\n<b>Почему был (-а) АФК:</b> <i>{reason}</i>\nБыл в афк {afk_time}</b>")
        client.remove_handler(*handler)
        await restart(message, restart_type='restart')
        
    except NameError:
        await message.edit("<b>Я не был в АФК</b>")
        await asyncio.sleep(3)
        await message.delete()

# Автоудаление сообщений
@app.on_message(filters.command("hide", prefix) & filters.me)
async def hide(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Скрытие текста"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    orig_text = message.text.split(prefix + "hide ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    while(tbp != orig_text):
        try:
            joper = tbp + typing_symbol
            await message.edit(str(joper))
            await asyncio.sleep(0.10)
            tbp = tbp + text[0]
            text = text[1:]
            await message.edit(str(tbp))
            await asyncio.sleep(0.10)
        except FloodWait as e:
            await asyncio.sleep(e.x)

    await asyncio.sleep(1.25)
    await message.delete()

# Авточтение
the_regex = r"^r\/([^\s\/])+"
f = filters.chat([])

@app.on_message(f)
async def auto_read(client: Client, message: Message):
    await app.read_history(message.chat.id)
    message.continue_propagation()

@app.on_message(filters.command("autoread", prefix) & filters.me)
async def add_to_auto_read(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Авточтение"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("Авточтение отключено")
    else:
        f.add(message.chat.id)
        await message.edit("Авточтение включено")

# Админ комманды
def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

def get_args(message):
    try:
        message = message.text
    except AttributeError:
        pass
    if not message:
        return False
    message = message.split(maxsplit=1)
    if len(message) <= 1:
        return []
    message = message[1]
    try:
        split = shlex.split(message)
    except ValueError:
        return message  # Cannot split, let's assume that it's just one long message
    return list(filter(lambda x: len(x) > 0, split))

async def CheckAdmin(message: Message):
    """Check if we are an admin."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await app.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__Я не админ!__")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin or SELF.can_restrict_members:
            return True
        else:
            await message.edit("__недостаточно прав__")
            await asyncio.sleep(2)
            await message.delete()

@app.on_message(filters.command("leave", prefix) & filters.me)
async def leave(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Выход с чата"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    m = await message.edit('<code>Всем пока... [Пользователь вышел с чата]</code>')
    await asyncio.sleep(2)
    await client.leave_chat(chat_id=message.chat.id)

@app.on_message(filters.command("ban", prefix) & filters.me)
async def ban_hammer(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на бан в беседе"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Я должен кого то забанить?**")
                return
        try:
            reply = message.reply_to_message
            await app.kick_chat_member(message.chat.id, reply.from_user.id, int(time.time() + 31536000))
            await message.edit(f'<b><a href="tg://user?id={reply.from_user.id}">{reply.from_user.first_name}</a> забанен!</b>')
        except:
            await message.edit("**Я не могу забанить этого пользователя.**")
    else:
        await message.edit("**Я админ?**")

@app.on_message(filters.command("unban", prefix) & filters.me)
async def unban(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на разбан в беседе"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Я должен кого то разбанить?**")
                return
        try:
            get_user = await app.get_users(user)
            await app.unban_chat_member(chat_id=message.chat.id, user_id=get_user.id)
            await message.edit(f"**Пользователь {get_user.first_name} был разбанен.**")
        except:
            await message.edit("**Я не могу разбанить.**")
    else:
        await message.edit("**Я админ?**")

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_stickers=False,
    can_send_animations=False,
    can_send_games=False,
    can_use_inline_bots=False,
    can_add_web_page_previews=False,
    can_send_polls=False,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

@app.on_message(filters.command("mute", prefix) & filters.me)
async def mute_hammer(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на мут"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Я должен кого то замутить?**")
                return
        try:
            get_user = await app.get_users(user)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
                permissions=mute_permission,
            )
            await message.edit(f"**{get_user.first_name} Был замучен.**")
        except:
            await message.edit("**Я не могу замутить.**")
    else:
        await message.edit("**Я админ?**")

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_stickers=True,
    can_send_animations=True,
    can_send_games=True,
    can_use_inline_bots=True,
    can_add_web_page_previews=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

@app.on_message(filters.command("unmute", prefix) & filters.me)
async def unmute(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на размут"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Я должен кого то размутить?**")
                return
        try:
            get_user = await app.get_users(user)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
                permissions=unmute_permissions,
            )
            await message.edit(f"**{get_user.first_name} Был размучен.**")
        except:
            await message.edit("**Я не могу размутить.**")
    else:
        await message.edit("**Я админ?**")

@app.on_message(filters.command("kick", prefix) & filters.me)
async def kick_user(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на кик участника"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("**Я должен кого то кикнуть?**")
                return
        try:
            get_user = await app.get_users(user)
            await app.kick_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
            )
            await message.edit(f"**Пользователь {get_user.first_name} был кикнут.**")
        except:
            await message.edit("**Я не могу кикать.**")
    else:
        await message.edit("**Я админ?**")

@app.on_message(filters.command("pin", prefix) & filters.me)
async def pin_message(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Запрос на закрепление сообщения"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if message.chat.type in ["group", "supergroup"]:
        admins = await app.get_chat_members(
            message.chat.id, filter=ChatMemberFilters.ADMINISTRATORS
        )
        admin_ids = [user.user.id for user in admins]
        me = await app.get_me()

        if me.id in admin_ids:
            if message.reply_to_message:
                disable_notification = True

                if len(message.command) >= 2 and message.command[1] in [
                    "alert",
                    "notify",
                    "loud",
                ]:
                    disable_notification = False

                await app.pin_chat_message(
                    message.chat.id,
                    message.reply_to_message.message_id,
                    disable_notification=disable_notification,
                )
                await message.edit("`Сообщение закрепленно!`")
            else:
                await message.edit(
                    "`Сделай ответ на сообщение`"
                )
        else:
            await message.edit("`Недостаточно прав`")
    else:
        await message.edit("`Я админ?`")
    await asyncio.sleep(3)
    await message.delete()

@app.on_message(filters.command("unpin", prefix) & filters.me)
async def pin(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Сообщение закрепленно"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    try:
        message_id = message.reply_to_message.message_id
        await client.unpin_chat_message(message.chat.id, message_id)
        await message.edit('<code>Открепленно! </code>')
    except:
        await message.edit('<b>Сделайте реплай сообщению</b>')

@app.on_message(filters.command("admin", prefix) & filters.me)
async def promote(client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Выдан статус админа одному из участников"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is False:
        await message.edit("**Я не админ.**")
        return
    title = "Admin"
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
        title = str(get_arg(message))
    else:
        args = get_args(message)
        if not args:
            await message.edit("**Я должен кого то повысить?**")
            return
        user = args[0]
        if len(args) > 1:
            title = " ".join(args[1:])
    get_user = await app.get_users(user)
    try:
        await app.promote_chat_member(message.chat.id, user, can_pin_messages=True)
        if title == "":
            title = "Админ"
        await message.edit(
            f"**{get_user.first_name} Стал админом с званием [{title}]**"
        )
    except Exception as e:
        await message.edit(f"{e}")
    if title:
        try:
            await app.set_administrator_title(message.chat.id, user, title)
        except:
            pass

@app.on_message(filters.command("unadmin", prefix) & filters.me)
async def demote(client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Отобран статус админа одному из участников"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    if await CheckAdmin(message) is False:
        await message.edit("**Я не админ**")
        return
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Я могу разжаловать админа?**")
            return
    get_user = await app.get_users(user)
    try:
        await app.promote_chat_member(
            message.chat.id,
            user,
            is_anonymous=False,
            can_change_info=False,
            can_delete_messages=False,
            can_edit_messages=False,
            can_invite_users=False,
            can_promote_members=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_post_messages=False,
        )
        await message.edit(
            f"**{get_user.first_name} Больше не админ!**"
        )
    except Exception as e:
        await message.edit(f"{e}")

@app.on_message(filters.command("invite", prefix) & filters.me)
async def invite(client, message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Участник приглашён"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Я должен кого то пригласить?**")
            return
    get_user = await app.get_users(user)
    try:
        await app.add_chat_members(message.chat.id, get_user.id)
        await message.edit(f"**Пользователь {get_user.first_name} Был приглашён в этот чат!**")
    except Exception as e:
        await message.edit(f"{e}")

# Команда взлома пентагона
@app.on_message(filters.command("hack", prefix) & filters.me)
async def hack(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда hack"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    perc = 0
    while(perc < 100):
        try:
            text = "👮 Взлом пентагона в процессе ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.1)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "✅ Пентагон успешно взломан!"
    await message.edit(str(text))
    await asyncio.sleep(3)
    perc = 0
    while(perc < 100):
        try:
            text = "⬇️ Скачивание данных ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.15)
        except FloodWait as e:
            await asyncio.sleep(e.x)

    await asyncio.sleep(1)
    text = "🐓Нашли файты что ты петух!"
    await message.edit(text)

# Команда Взлома жопы
@app.on_message(filters.command("jopa", prefix) & filters.me)
async def jopa(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда jopa"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    perc = 0
    while(perc < 100):
        try:
            text = "🍑 Взлом жопы в процессе ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.1)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "✅ Жопа взломана"
    await message.edit(str(text))
    await asyncio.sleep(3)
    text = "🔍 Поиск Сливов ..."
    await message.edit(str(text))
    perc = 0
    await asyncio.sleep(3)
    while(perc < 100):
        try:
            text = "⬇️ Скачивание сливов ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 4)
            await asyncio.sleep(0.15)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "✅ Сливы были найдены"
    await message.edit(str(text))
    perc = 0
    await asyncio.sleep(5)
    while(perc < 100):
        try:
            text = "⬆️ Продажа сливов барыге..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.15)
        except FloodWait as e:
            await asyncio.sleep(e.x)

    text = "✅ Проданно"
    await message.edit(str(text))
    await asyncio.sleep(2)
    rand =+ random.randint(100, 5000)
    bal = rand
    text = "💸 Вы заработали " + str(bal) + " ₽"
    await message.edit(text)

# Наркота
@app.on_message(filters.command("drugs", prefix) & filters.me)
async def drugs(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда drugs"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    perc = 0
    result = 0
    while(perc < 100):
        try:
            text = "🍁Поиск запрещённых препаратов " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.1)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "Найдено 3 кг шпекса🍪💨"
    await message.edit(str(text))
    await asyncio.sleep(3)
    text = "Оформляем вкид 🌿⚗️"
    await message.edit(str(text))
    await asyncio.sleep(5)
    result += random.randint(1, 4)

    if result == 1:
        text = "🔥😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты 😳🔥"
        await message.edit(str(text))
    if result == 2:
        text = "🥴Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид🥴"
        await message.edit(str(text))
    if result == 3:
        text = "😖Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз😖"
        await message.edit(str(text))
    if result == 4:
        text = "😌Вы оформили вкид, Вам понравилось)😌"
        await message.edit(str(text))

# Оскорбление мамки
@app.on_message(filters.command("mum", prefix) & filters.me)
async def mum(client: Client, message: Message):
    now = datetime.datetime.now()
    timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    log = logi + timnow + "\n╰ Комманда mum"
    await app.send_message("ClipUSERBOT_LOGGERbot", log)

    text = "🔍 Поиск твоей мамки начался..."
    await message.edit(str(text))
    await asyncio.sleep(3.0)
    perc = 0
    while(perc < 100):
        try:
            text = "🔍 Ищем твою мамашу на Авито... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.75)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "❌ Мамаша не найденна"
    await message.edit(str(text))
    await asyncio.sleep(3.0)

    perc = 0
    while(perc < 100):
        try:
            text = "🔍 Поиск твоей мамаши на свалке... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.75)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "❌ Мамаша не найденна"
    await message.edit(str(text))

    perc = 0
    while(perc < 100):
        try:
            text = "🔍 Поиск твоей мамки в канаве... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.75)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    text = "✅ Мамка найдена... Она в канаве"
    await message.edit(str(text))

app.run()

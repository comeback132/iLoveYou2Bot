import telebot
from flask import Flask
from flask import request
from flask import Response
import requests
import json

TOKEN = '6223995097:AAE2EFken-YQwJMVjMQvbmplelqP73rdAqk'
app = Flask(__name__)


def parse_message(message):
    print('message-->', message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print('chat_id-->', chat_id)
    print('txt-->', txt)
    return chat_id, txt


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r


def tel_send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg",
        'caption': "This is a sample image"
    }

    r = requests.post(url, json=payload)
    return r


def tel_send_image_love(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://www.yourtango.com/sites/default/files/styles/body_image_default/public/2020/love-meme-elmo.jpg",
        'caption': "I love you too, babe"
    }

    r = requests.post(url, json=payload)
    return r


def tel_send_audio(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'

    payload = {
        'chat_id': chat_id,
        "audio": "http://www.largesound.com/ashborytour/sound/brobob.mp3",

    }

    r = requests.post(url, json=payload)

    return r


def tel_send_audio_love(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'

    payload = {
        'chat_id': chat_id,
        "audio": "https://www.soundboard.com/track/download/174390",

    }

    r = requests.post(url, json=payload)

    return r


def tel_send_video(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendVideo'

    payload = {
        'chat_id': chat_id,
        "video": "https://www.appsloveworld.com/wp-content/uploads/2018/10/640.mp4",

    }

    r = requests.post(url, json=payload)

    return r


def tel_send_video_love(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendVideo'

    payload = {
        'chat_id': chat_id,
        "video": "https://media4.giphy.com/media/LuvsSH7vbGeKtZ238M/giphy.gif",

    }

    r = requests.post(url, json=payload)

    return r


def tel_send_poll(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    payload = {
        'chat_id': chat_id,
        "question": "How are you doing today?",
        "options": json.dumps(["Fine", "Happy", "Tired", "Sad"]),
        "is_anonymous": False,
        "type": "quiz",
        "correct_option_id": 2
    }

    r = requests.post(url, json=payload)

    return r


def tel_send_inlinebutton(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "What is this?",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "A",
                    "callback_data": "ic_A"
                },
                {
                    "text": "B",
                    "callback_data": "ic_B"
                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r


def tel_send_inlineurl(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "come back?",
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Instagram", "url": "https://www.instagram.com/comecomeback132/"},
                    {"text": "Soundcloud", "url": "https://soundcloud.com/comeback132"}
                ]
            ]
        }
    }

    r = requests.post(url, json=payload)

    return r


def tel_parse_get_message(message):
    print("message-->", message)

    try:
        g_chat_id = message['message']['chat']['id']
        g_file_id = message['message']['photo'][0]['file_id']
        print("g_chat_id-->", g_chat_id)
        print("g_image_id-->", g_file_id)

        return g_file_id
    except:
        print("NO file found found-->>")


def tel_upload_file(file_id):
    url = f'https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}'
    a = requests.post(url)
    json_resp = json.loads(a.content)
    print("a-->", a)
    print("json_resp-->", json_resp)
    file_pathh = json_resp['result']['file_path']
    print("file_path-->", file_pathh)

    url_1 = f'https://api.telegram.org/file/bot{TOKEN}/{file_pathh}'
    b = requests.get(url_1)
    file_content = b.content
    with open(file_pathh, "wb") as f:
        f.write(file_content)


# call methods here
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        chat_id, txt = parse_message(msg)
        if txt == 'hi':
            tel_send_message(chat_id, 'Hello!!')
        # kicya bot
        elif txt == 'I love you':
            tel_send_message(chat_id, 'бубу кіся піся')
            tel_send_image_love(chat_id)
            tel_send_audio_love(chat_id)
            tel_send_video_love(chat_id)
        elif txt == "image":
            tel_send_image(chat_id)
        elif txt == "audio":
            tel_send_audio(chat_id)
        elif txt == "video":
            tel_send_video(chat_id)
        elif txt == "poll":
            tel_send_poll(chat_id)
        elif txt == "inline":
            tel_send_inlinebutton(chat_id)
        elif txt == "come":
            tel_send_inlineurl(chat_id)
        else:
            tel_send_message(chat_id, 'ask me tomorrow')

        return Response('ok', status=200)
    else:
        return '<h1>Welcome!</h1>'


if __name__ == '__main__':
    app.run(debug=True)

# bot = telebot.TeleBot(TOKEN)

# bot.infinity_polling()

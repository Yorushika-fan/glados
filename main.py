import requests
import telebot
import os
def checkIn():
    url = 'https://glados.rocks/api/user/checkin'

    headers = {
        'cookie': os.environ.get('COOKIE'),
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    data = {
        'token': 'glados.one'
    }

    res = requests.post(url, headers=headers, data=data)
    return res.json().get('message')
def message():
    telebot.TeleBot(os.environ.get('BOT_TOKEN')).send_message(os.environ.get('CHAT_ID'), checkIn())
message()
 

import requests
import telebot
import time

bot_token = 'TOKEN'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message,'Welcome Traveller are you ready to see the stars!\n\n' +'\n\nType /stars to see the stars of the github of JBossOutreach')

@bot.message_handler(commands=['stars'])
def stars(message):
    api = requests.get('https://api.github.com/orgs/JBossOutreach/repos')
    res = api.json()
    out = ''
    for a in range(len(res)):
        out += '\n' + res[a]['name'] + ': ' + str(res[a]['stargazers_count'])
    bot.reply_to(message,'Here are JBoss Repositories & their Stars. \n\n' + out)

while True:
	try:
		bot.polling()
	except Exception:
		time.sleep(15)
	pass

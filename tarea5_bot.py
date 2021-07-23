import os
import telebot


TOKEN = '1923317621:AAGmxxiBEof5-TtsZeYNlKO4D5I3daDcpS4'

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['foto'])

def foto(m):
    cid=m.chat.id
    bot.send_photo(cid, open('imagen.png', 'rb'))

@bot.message_handler(commands=['video'])

def foto(m):
    cid=m.chat.id
    bot.send_photo(cid, open('video.mp4', 'rb'))

bot.polling()  



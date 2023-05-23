import telebot
import random
bot = telebot.TeleBot("5961374637:AAHVfx2e3AD0rlM8xpn6g2XzRN9gx_tEQm0", parse_mode='html')

@bot.message_handler(commands=["start"])
def hello(message):
    bot.send_message(message.chat.id, "<b>🖐Приветствую🖐\n\n🤖Я бот-генератор никнеймов🤖\n\n Чтобы сгенерировать никнейм или ознакомиться с информацией о боте используйте команды во вкладке меню.\n </b>")

@bot.message_handler(commands=["nick"]) 
def get_random_names(message):  
    names = ["sun","parrot","cat","fire","star","moon","sun","wolf","beast","flame","bunny","snake","sunshine","dragon","eagle","desert","spirit","crystal","banshee","bear","sweet","pie","cobra","owl","eye","tomato","fox","paw","beer","wine","vibe","cloud","heart","bird","onion","lemon","apple","coffee","tea","alien","mix","ice","tor","gamma","blood","color","world","chocolate","killer","phantom",] 
    printName = random.choice(names) 
    chislo = random.randint(1,999)
    bot.send_message(message.chat.id, f"✅Ваш никнейм: {printName}{chislo}✅")

@bot.message_handler(commands=["info"]) 
def info(message):
    bot.send_message(message.chat.id, "<b>Делал бота студент группы ПР-22.101 Бахтуров Артём😊\n\nИспользовал язык программирования Python.\nБот создан для упрощения жизни тех, кто не может придумать имя пользователя для соц-сетей или других интернет ресурсов.</b>")
    










bot.polling(non_stop=True, interval=0)



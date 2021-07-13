from dotenv import load_dotenv
load_dotenv()

import os
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


API_key = os.environ.get('API_KEY')
bot = telebot.TeleBot(API_key)

templateDict = {}


class Template:
    def __init__(self, camp):
        self.camp = camp
        self.qbooked = ""
        self.qchecked = ""
        self.qodd = ""
        self.qoddrmk  = "" #for remarks, make them a list of strings, and loop through and print all
        self.qoddrec = ""
        self.qus = ""
        self.qusrmk = "" #for remarks, make them a list of strings, and loop through and print alls
        self.qusout = ""



# Handle '/start' and '/help'
@bot.message_handler(commands=['FFF' and 'fff'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Hi there, I am FFF Template Bot. Which unit did you go to today?
""")
    bot.register_next_step_handler(msg, campStep)


def campStep(message):
    try:
        chat_id = message.chat.id
        camp = message.text
        template = Template(camp)
        templateDict[chat_id] = template
        msg = bot.reply_to(message, 'What is the quantity booked?')
        bot.register_next_step_handler(msg, bookedStep)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def bookedStep(message):
    try:
        chat_id = message.chat.id
        template = templateDict[chat_id]
        qbooked = message.text
        template.qbooked = qbooked
        msg = bot.reply_to(message, 'What is the quantity checked?')
        bot.register_next_step_handler(msg, checkedStep)

    except Exception as e:
        bot.reply_to(message, 'oooops')

def checkedStep(message):
    try:
        chat_id = message.chat.id
        template = templateDict[chat_id]
        qchecked = message.text
        template.qchecked = qchecked
        msg = bot.reply_to(message, 'What is the ODD quantity?')
        bot.register_next_step_handler(msg, oddqStep)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def oddqStep(message):
    try:
        chat_id = message.chat.id
        template = templateDict[chat_id]
        qodd = message.text
        template.qodd = qodd
        msg = bot.reply_to(message, 'How many ODD Rectified?')
        bot.register_next_step_handler(msg, oddRecStep)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def oddRecStep(message):
    try:
        chat_id = message.chat.id
        template = templateDict[chat_id]
        qoddrec = message.text
        template.qoddrec = qoddrec
        msg = bot.reply_to(message, 'How many US Weapons?')
        bot.register_next_step_handler(msg, qUsStep)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def qUsStep(message):
    try:
        chat_id = message.chat.id
        template = templateDict[chat_id]
        qus = message.text
        template.qus = qus

        if int(qus) > 0:
            msg = bot.reply_to(message, 'Do You Want to create a US Remark? (y/n)') #make this a button
            bot.register_next_step_handler(msg, usRemarkCheckStep)

        else:
            msg = bot.reply_to(message, 'How many US Weapons Outstanding?')
            bot.register_next_step_handler(msg, qUsOutStep)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def usRemarkCheckStep(message):
    try:
        if message.text == 'y': 
            msg = bot.reply_to(message, 'What is the US Remark?')
            bot.register_next_step_handler(msg, usRemarkStep)
        else:
            msg = bot.reply_to(message, 'How many US Weapons Outstanding?')
            bot.register_next_step_handler(msg, qUsOutStep)

    except Exception as e:
        bot.reply_to(message, 'oooops')

def usRemarkStep(message):
    try:
        chat_id = message.chat.id
        template = templateDict[chat_id]

        #next iter, make it so that it can ask for unlimited remarks
        template.qusrmk = message.text + "\n"
        print(template.qusrmk)
        msg = bot.reply_to(message, 'How many US Weapons Outstanding?')
        bot.register_next_step_handler(msg, qUsOutStep)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def qUsOutStep(message):
    try:
        chat_id = message.chat.id
        template = templateDict[chat_id]
        qusout = message.text
        template.qusout = qusout

        inspectionSummary = "*INSPECTION SUMMARY*" + "\n\n"
        camp = template.camp.upper() + "\n\n"
        quantityBooked = "QUANTITY BOOKED: " + "[" + template.qbooked + "]" + "\n"
        quantityChecked = "QUANTITY CHECKED: " + "[" + template.qchecked + "]" + "\n\n"
        oddQuantity = "ODD QUANTITY: " + "[" + template.qodd + "]" + "\n"
        oddRectified = "ODD QUANTITY: " + "[" + template.qoddrec + "]" + "\n\n"
        totalUS = "*NO OF US WEAPONS:" + "[" + template.qus + "]*" + "\n"
        usRemark = template.qusrmk
        outstandingUS = "*NO OF OUTSTANDING US WEAPONS:" + "[" + template.qusout + "]*" + "\n\n"
        remarks = "REMARKS: \nTools and gauges accounted for."

        returnStatement = inspectionSummary + camp + quantityBooked + quantityChecked + oddQuantity + oddRectified + totalUS + usRemark + outstandingUS + remarks
        bot.send_message(message.chat.id, returnStatement)
    except Exception as e:
        bot.reply_to(message, 'oooops')




bot.polling()
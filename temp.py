from dotenv import load_dotenv
load_dotenv()

from time import sleep
import os
import telebot
import geopy.distance
from telegram import Location, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton


"""
Issues to solve for
1. If for some reason the input is not one of the two buttons
    a. Static Map:
        1. input is not numeric (and between 1-11 if 11 camps)
    b. Nearest AED:
        2. 



"""








API_key = os.environ.get('aedAPI_KEY')
bot = telebot.TeleBot(API_key)


aedDict = {}


class AED:
    def __init__(self, location):
        self.latitude = location.latitude
        self.longitude = location.longitude
        self.aeds = {}
        
       

locations = {
    "nsdc": {
        1: (1.4055524, 103.8182829),
        2: (1.4067986, 103.8192924),
        3: (1.4091958,103.8186530),

    }

}

badURL = "https://lh3.googleusercontent.com/m61vTtkjihiwIJ_PEnVPEKfd8Yx1FsoGcCzcrx0A5SJjZtnpu7h61HB-viz0K4JpBnK2QAf0KRfN8AA-spL_C6SIf-tMu4o3x5W6RMuG37RXP4X4COk6QRrE0ylLQJYVPLJ3-G3wQC5MQkwCcksHJfTq2UCYxKdPlSdy5pzb6m5g7Z2pot_z8_uxssfM0FjPmQ9EpprG_g_3wZ1hwp1-iEr3_RYnZUt7YzfaDDFWMlElGVCwfJ6dbzqD2NCNTGlHn_webljEdtswpUQx-2H2EHxBtlU03_ey4fKz0rGCUhN2ryyauTfdTzfvsiw6WB2Bz5uency7qEqA8EiooqZwVgRvDFOpPp8tTEZLI7JnErd_dqwrDr-3nJLdTyEntpGSlKlKBdbl4o6R1-JysFom6VcjAPW9Y1o-ZKOwoWhvVkOFHLad87PyU6_N8cBY_5WiaTbFs5Nrjl_sY84ViBp_lx4MOaW6xpjS9evotqJ2HJcen5rPGTEz3o89v2evb8nKVfqnI-M2cnTSd9qN6M8aqvz8K1XtI_ts61wVbVNCM4S1UoohWTQB0MYHkAeljkzK7unLavErhZSajtRKgfHhfIfbPK-eHHyXFxbqQ_qFCAki9FCfUT79zd80TFURjb8DlcT0dBOtyIG75D8_cCkwG2JV4_Y3M1N77K0EOfDi80m51aHxfW6znaHBob_1em6qZxBLBQadGBTQvCj_jOWEVcgOsg=w800-h399-no?authuser=1"
campMaps = {
    "nsdc": "https://lh3.googleusercontent.com/jz7l8taMGnOPqRTafzGq_3Uflb92HE54IkQ4AwD1Za_e2W5ywkfP-fqYV2V_aQ91z7tKvBAbpGV2w9F5uB6zNXp2YOEuaXV3cOnA5WSQeiAmE-cMCW-K4GMSjSEozIqZ2pxt2Nz1aF_dWwHhczezH3nUWo1cK85IFD8HPd4Ct1qq-YlP84q0MN9JQAKTtnsowsuPe8IiXyq33UuHhzluOkkc2_pQdBBWZxgA7Sit767DkZO30GBrGSNkWI9GPk2G6PEWM5edoRgWqtxaFKXeYsPV4kd9eCud4SykFGlRHJuxk5c_CXA2FSZH7ZFQk1ikTyBkvMgAY9UycxNPO8lUxFb6FLwLqKBKoXcP7uIG0BfFtT9YLVh135NSuRBvl538qQG-zhkv1tYi-w03LgRdo9zk5790QrEszkkKFL8fcGoqkmuGrtIzGQ5mEgXPqhh4hZoiSkaDTMZHDLgTBl6IitaIrWtmnzs9f8OFNQGSGuB_4qAFavOgCvKITX4WiimtWQaD7WGky8RVKFiB7dlLc2uhu_BUeVVtUaD2EzWelye0lKr1dpob7LK6qd30Br2qf_7LDVUzjbMbRjE5LDn1UWsYXAT8oKWRn213sEwArF56lUDb8kYdpIkHQApqyjDuykVjPRrRRhXtNTjtOJdP4ZdIqZ15ks9eqU1F0P2dcTiZbWSqAO-esahf0zXS7I1XTFZiH6wXX6Plw2PGG9eGmoK0zw=w596-h792-no?authuser=1",
    "nsc": badURL,
    "mandai hill":badURL,
    "kc2":badURL,
    "kc3" :badURL,
    "mowbray": badURL,
    "hendon":badURL,
    "clementi":badURL,
    "maju":badURL,
    "gombak":badURL,
    "gedong":badURL
}

mappingMapDict = {1:"nsdc", 2:"nsc", 3:"mandai hill", 4:"kc2", 5:"kc3", \
    6:"mowbray", 7: "hendon", 8:"clementi", 9:"maju", 10:"gombak", 11:"gedong"}









@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, """ 
    Welcome to AED Bot!
    If you need to find the nearest AED or get a map of the AEDs at a certain camp use the /start command

    If you have any issues please contact 62FMD at 6AMB!
    
    """)


@bot.message_handler(commands=['start'])
def start(message):
    loc = telebot.types.KeyboardButton(text='Nearest AED', request_location=True)
    not_loc = telebot.types.KeyboardButton(text='Static Map')
    start = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    start.row(loc)
    start.row(not_loc)
    st = """
    Hello, would you like to see your nearest AED or a static map? 
    \n
If you click Nearest AED, the bot will request your location!
    """
    bot.send_message(message.chat.id,text= st, reply_markup=start)

    #bot.send_message(message.chat.id, "Welcome to AED Location Bot, How Can I Help?")
    



    

@bot.message_handler(content_types=['location'])
def currentLocation(message):
    try:
        chat_id = message.chat.id
        print("reached")
       
        one = telebot.types.KeyboardButton(text='NSDC')
        two = telebot.types.KeyboardButton(text='NSC')
        three = telebot.types.KeyboardButton(text='Mandai Hill')
        four = telebot.types.KeyboardButton(text='KC2')
        five = telebot.types.KeyboardButton(text='KC3')
        six = telebot.types.KeyboardButton(text='Mowbray')
        seven = telebot.types.KeyboardButton(text='Hendon')
        eight = telebot.types.KeyboardButton(text='Clementi')
        nine = telebot.types.KeyboardButton(text='Maju')
        ten = telebot.types.KeyboardButton(text='Gombak')
        eleven = telebot.types.KeyboardButton(text='Gedong')
        locs = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
   
        locs.add(one, two, three, four, five, six, seven, eight, nine, ten, eleven)

        if message.location:
            aed = AED(message.location)
            aedDict[chat_id] = aed
            print(message.location)
            sendString = """
            Which camp are you at?
        """
            
            msg = bot.send_message(message.chat.id,sendString, reply_markup=locs)
            bot.register_next_step_handler(msg, distanceCalculator)
        else:
            bot.send_message(message.chat.id,"Could not get user location, please try again" )
    except Exception as e:
        bot.reply_to(message, 'oooops')


def distanceCalculator(message):
    try:
        chat_id = message.chat.id
        
        camp =  message.text.lower()
        aed = aedDict[chat_id]
        
        if camp in locations.keys():
            closestAED = (0,0)
            minDist = 100000000000
            for coords in locations[camp].values():
                dist = geopy.distance.distance((aed.latitude, aed.longitude), coords).m
                
                #dist = geopy.distance.distance((1.405854, 103.818543), coords).m
                aed.aeds[dist] = coords
                if dist < minDist:
                    minDist = dist
                    closestAED = coords
            sortedDist = sorted(list(aed.aeds.keys()))
            print(sortedDist)
            bot.send_message(message.chat.id,"The AEDs below are sorted from nearest to farthest!" )
            bot.send_chat_action(message.chat.id, "typing")
            sleep(3)
            counter = 0
            for keys in sortedDist:
                if counter > 1: # to limit to the 2 closest AEDs
                    break
                bot.send_location(message.chat.id, aed.aeds[keys][0], aed.aeds[keys][1])
                sendString = "The AED at the above location is approximately " + str(round(keys)) + "m away"
                bot.send_message(message.chat.id,sendString )
                counter += 1
                
                sleep(0.5)
            finalString = "Stay Safe!"
            bot.send_message(chat_id, "If you need any more information, please type in the /start command again!")
            bot.send_message(message.chat.id, finalString )


            # bot.send_location(message.chat.id, 1.405854, 103.818543)
            # bot.send_location(message.chat.id, closestAED[0], closestAED[1])
            # sendString = "The closest AED is at the above location, approximately " + str(round(minDist)) + "m away"
            # bot.send_message(message.chat.id,sendString )
        else:
            bot.send_message(message.chat.id,"Sorry, we currently don't have the coordinates of the AEDs in this camp!" )
    except Exception as e:
        bot.reply_to(message, 'oooops')



#========================================================================


def checker (message):
    if message.text == "Static Map" and message.content_type == 'text':
        return True
    else:
        return False


@bot.message_handler(func=checker)
def staticMap(message):
    try:
       

        one = telebot.types.KeyboardButton(text='NSDC')
        two = telebot.types.KeyboardButton(text='NSC')
        three = telebot.types.KeyboardButton(text='Mandai Hill')
        four = telebot.types.KeyboardButton(text='KC2')
        five = telebot.types.KeyboardButton(text='KC3')
        six = telebot.types.KeyboardButton(text='Mowbray')
        seven = telebot.types.KeyboardButton(text='Hendon')
        eight = telebot.types.KeyboardButton(text='Clementi')
        nine = telebot.types.KeyboardButton(text='Maju')
        ten = telebot.types.KeyboardButton(text='Gombak')
        eleven = telebot.types.KeyboardButton(text='Gedong')
        locs = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
   
        locs.add(one, two, three, four, five, six, seven, eight, nine, ten, eleven)
        msg = bot.reply_to(message, """\
        Which camp would you like a map for?
        """, reply_markup=locs)
        bot.register_next_step_handler(msg, returnImage)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def returnImage(message):
    try:
        chat_id = message.chat.id
        msg = message.text.lower()
        url = campMaps[msg]
        
        
        if url == badURL:
            errorString = "Sorry, support for this camp is not available yet!"
            bot.send_message(message.chat.id,errorString )
        else:
            bot.send_photo(chat_id=chat_id, photo=url)
            bot.send_message(chat_id, "If you need any more information, please type in the /start command again!")
    except Exception as e:
        bot.reply_to(message, 'oooops')

bot.polling()
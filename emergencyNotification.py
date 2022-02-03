import requests

rate={'btcMax': 40000,'ethMax':3000,'xrpMax':1,'dotMax':20,'adaMax':2,
        'ltcMax':115,'bchMax':295,'linkMax':20,'xlmMax':1}

lowRate={'btcLow': 35000,'ethLow':2500,'xrpLow':0.1,'dotLow':15,'adaLow':1,
        'ltcLow':110,'bchLow':280,'linkLow':15,'xlmLow':0.1}

def telegramMessage(message):
    msgUrl = 'https://api.telegram.org/bot5127863428:AAG8wG2I518sP1h1diYnRbHn3TI_HOjk2mc/sendMessage?chat_id=-604428747&text={}'.format(
        message)

    requests.get(msgUrl)


def emergencyNotification(currency,rate):

    url='https://api.telegram.org/bot5127863428:AAG8wG2I518sP1h1diYnRbHn3TI_HOjk2mc/sendMessage?chat_id=1345837213&text={} High Value Reached...\n{} : {}'.format(currency,currency,rate)
    requests.get(url)

def lowRateEmergencyNotification(currency,rate):
    url = 'https://api.telegram.org/bot5127863428:AAG8wG2I518sP1h1diYnRbHn3TI_HOjk2mc/sendMessage?chat_id=1345837213&text={} Low Value Reached...\n{} : {}'.format(currency, currency, rate)
    requests.get(url)
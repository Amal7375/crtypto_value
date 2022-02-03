import requests
import time
from datetime import datetime

import emergencyNotification

def Value():

    currency = 'Bitcoin'
    currencyPrice='https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT'

    while True:
        time.sleep(60)

        price = requests.get(currencyPrice)
        response=price.json()

        btcResp= response['price']

        btc='{}  : ${}'.format(currency, btcResp[0:8])

        if float(btcResp) >= emergencyNotification.rate['btcMax'] :
            emergencyNotification.emergencyNotification(currency,btcResp)

        elif float(btcResp) <= emergencyNotification.lowRate['btcLow'] :
            emergencyNotification.lowRateEmergencyNotification(currency,btcResp)
        else:
            pass

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        currency = 'Ethereum'
        currencyPrice='https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT'


        price = requests.get(currencyPrice)
        response=price.json()

        ethResp= response['price']


        eth='{} : ${}'.format(currency, ethResp[0:8])

        if float(ethResp) >= emergencyNotification.rate['ethMax'] :
            emergencyNotification.emergencyNotification(currency,ethResp)
        elif float(ethResp) <= emergencyNotification.lowRate['ethLow']:
            emergencyNotification.lowRateEmergencyNotification(currency, ethResp)
        else:
            pass

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        currency = 'XRP'
        currencyPrice='https://api.binance.com/api/v3/avgPrice?symbol=XRPUSDT'


        price = requests.get(currencyPrice)
        response=price.json()

        xrpResp= response['price']


        xrp='{}      : ${}'.format(currency, xrpResp[0:8])
        if float(xrpResp) >= emergencyNotification.rate['xrpMax'] :

            emergencyNotification.emergencyNotification(currency,xrpResp)
        elif float(xrpResp) <= emergencyNotification.lowRate['xrpLow']:
            emergencyNotification.lowRateEmergencyNotification(currency, xrpResp)
        else:
            pass

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        currency = 'DOT'
        currencyPrice='https://api.binance.com/api/v3/avgPrice?symbol=DOTUSDT'


        price = requests.get(currencyPrice)
        response=price.json()

        dotResp= response['price']


        dot='{}      : ${}'.format(currency, dotResp[0:8])
        if float(dotResp) >= emergencyNotification.rate['dotMax'] :

            emergencyNotification.emergencyNotification(currency,dotResp)
        elif float(dotResp) <= emergencyNotification.lowRate['dotLow']:
            emergencyNotification.lowRateEmergencyNotification(currency, dotResp)
        else:
            pass

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        currency = 'ADA'
        currencyPrice='https://api.binance.com/api/v3/avgPrice?symbol=ADAUSDT'


        price = requests.get(currencyPrice)
        response=price.json()

        adaResp= response['price']


        ada='{}      : ${}'.format(currency, adaResp[0:8])

        if float(adaResp) >= emergencyNotification.rate['adaMax'] :

            emergencyNotification.emergencyNotification(currency,adaResp)
        elif float(adaResp) <= emergencyNotification.lowRate['adaLow']:
            emergencyNotification.lowRateEmergencyNotification(currency, adaResp)
        else:
            pass

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        currency = 'LTC'
        currencyPrice='https://api.binance.com/api/v3/avgPrice?symbol=LTCUSDT'


        price = requests.get(currencyPrice)
        response=price.json()

        ltcResp= response['price']


        ltc='{}      : ${}'.format(currency, ltcResp[0:8])

        if float(ltcResp) >= emergencyNotification.rate['ltcMax'] :

            emergencyNotification.emergencyNotification(currency,ltcResp)
        elif float(ltcResp) <= emergencyNotification.lowRate['ltcLow']:
            emergencyNotification.lowRateEmergencyNotification(currency, ltcResp)
        else:
            pass
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        currency = 'BCH'
        currencyPrice='https://api.binance.com/api/v3/avgPrice?symbol=BCHUSDT'


        price = requests.get(currencyPrice)
        response=price.json()

        bchResp= response['price']


        bch='{}      : ${}'.format(currency, bchResp[0:8])
        if float(bchResp) >= emergencyNotification.rate['bchMax'] :

            emergencyNotification.emergencyNotification(currency,bchResp)
        elif float(bchResp) <= emergencyNotification.lowRate['bchLow']:
            emergencyNotification.lowRateEmergencyNotification(currency, bchResp)
        else:
            pass
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        currency = 'LINK'
        currencyPrice='https://api.binance.com/api/v3/avgPrice?symbol=LINKUSDT'

        price = requests.get(currencyPrice)
        response=price.json()

        linkResp= response['price']


        link='{}     : ${}'.format(currency,linkResp[0:8])
        if float(linkResp) >= emergencyNotification.rate['linkMax'] :

            emergencyNotification.emergencyNotification(currency,linkResp)
        elif float(linkResp) <= emergencyNotification.lowRate['linkLow']:
            emergencyNotification.lowRateEmergencyNotification(currency, linkResp)
        else:
            pass

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        currency = 'XLM'
        currencyPrice='https://api.binance.com/api/v3/avgPrice?symbol=XLMUSDT'


        price = requests.get(currencyPrice)
        response=price.json()

        xlmResp= response['price']

        xlm='{}      : ${}'.format(currency, xlmResp[0:8])
        if float(xlmResp) >= emergencyNotification.rate['xlmMax'] :

            emergencyNotification.emergencyNotification(currency,xlmResp)
        elif float(xlmResp) <= emergencyNotification.lowRate['xlmLow']:
            emergencyNotification.lowRateEmergencyNotification(currency, xlmResp)
        else:
            pass
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        times = str(datetime.now().strftime('%d.%m.%Y (%H:%M)'))
        value = [times,'---------------------------------------------'
            ,btc,eth,xrp,dot,ada,ltc,bch,link,xlm]

        value='\n'.join(value)


        return (value)
        
        #time.sleep(5*60)
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



"""
This file Include End point links and data used for post requests.
"""
PATH_TO_SAVE_FIGURES = 'plots/'
API_HITS = 10
NOON_AND_KEBAB = '/v59/outlets?__i=2692567&__platform=ios&app_version=5.90.00&category=Restaurants%20and%20Bars&company=entertainer&currency=AED&device_key=ios-C002387E-908C-45FB-9EAF-768C60455414&device_model=iPhone%207&include_featured=1&language=en&lat=31.484388&lng=74.393182&location_id=1&offset=0&os_version=11.1.1&outlet_limit=60&redeemability=redeemable_reusable&session_token=32041547358d0c5edeaa804.53272884&sort=default&user_id=172451'
NOON_AND_KEBAB_WITHOUT_PARMS = '/v59/outlets?'
EMPTY_SEARCH_SCOPE_MODE = '/v59/merchants/22015?__i=0&__platform=ios&app_version=5.90.00&company=entertainer&currency=&device_key=ios-48195B02-3646-4EDF-A46B-67646935624B&device_model=iPhone%206S&language=en&lat=31.484087&lng=74.393194&location_id=1&os_version=10.3.3&session_token=&user_id=0'
MERCHANT_SEARCH_SCOPE_MODE = '/v59/merchants/22015?__i=2692567&__platform=ios&app_version=5.90.00&company=entertainer&currency=&device_key=ios-48195B02-3646-4EDF-A46B-67646935624B&device_model=iPhone%206S&language=en&lat=31.484087&lng=74.393194&location_id=1&os_version=10.3.3&session_token=32041547358d0c5edeaa804.53272884&user_id=0'
EMPTY_SEARCH_SCOPE_MODE_WITHOUT_PARMS = '/v59/merchants/22015?'
BUY_MORE = '/v59/outlets?__i=2692567&__platform=ios&app_version=5.90.00&category=Body&company=entertainer&currency=AED&device_key=ios-48195B02-3646-4EDF-A46B-67646935624B&device_model=iPhone%206S&language=en&lat=31.484074&lng=74.393189&location_id=1&offset=0&os_version=10.3.3&outlet_limit=60&redeemability=not_redeemable&session_token=32041547358d0c5edeaa804.53272884&sort=default&user_id=172451'
BIRTHDAY_DEEPLINK = '/v59/outlets?__i=2692567&__platform=ios&app_version=5.91.00&company=entertainer&currency=AED&device_key=ios-E7162FE2-16D2-4D79-943E-F159450ABFD0&device_model=iPhone%206%20Plus&filters_selected_for_yes[]=happy_birthday&language=en&lat=31.484115&lng=74.393207&location_id=1&offset=0&os_version=10.3&outlet_limit=0&session_token=32041547358d0c5edeaa804.53272884&sort=default&title=your%20birthday%20offers&user_id=172451'
DEEPLINKS_NOT_WORKING = '/v59/outlets?__i=2692567&__platform=ios&app_version=5.91.00&company=entertainer¤cy=AED&device_key=ios-E7162FE2-16D2-4D79-943E-F159450ABFD0&device_model=iPhone%206%20Plus&language=en&lat=31.484092&lng=74.393194&location_id=1&offset=0&os_version=10.3&outlet_limit=0&query=brunch&query_type=name&session_token=32041547358d0c5edeaa804.53272884&sort=default&user_id=172451'
DEEPLINKS_NOT_WORKING_AS_EXPECTED_BRUNCH = '/v59/outlets?__i=2692567&__platform=ios&app_version=5.91.00&company=entertainer¤cy=AED&device_key=ios-E7162FE2-16D2-4D79-943E-F159450ABFD0&device_model=iPhone%206%20Plus&language=en&lat=31.484092&lng=74.393194&location_id=1&offset=0&os_version=10.3&outlet_limit=0&query=brunch&query_type=name&session_token=32041547358d0c5edeaa804.53272884&sort=default&user_id=172451'
IS_DELIVERY_IS_GETTING_TRUE_OR_FALSE = '/v59/outlets?__i=2692567&__platform=ios&app_version=5.90.00&category=Restaurants%20and%20Bars&company=entertainer&device_key=ios-48195B02-3646-4EDF-A46B-67646935624B&device_model=iPhone%206S&filters_selected_for_yes[]=delivery&language=en&lat=31.484091&lng=74.393194&location_id=1&offset=120&os_version=10.3.3&outlet_limit=60&redeemability=redeemable_reusable&session_token=32041547358d0c5edeaa804.53272884&sort=default&user_id=172451'
DELIVERY_AND_MULTIPLE_FILTERS = '/v59/outlets?__i=2692567&__platform=ios&app_version=5.90.00&category=Restaurants%20and%20Bars&company=entertainer&currency=AED&device_key=ios-48195B02-3646-4EDF-A46B-67646935624B&device_model=iPhone%206S&filters_selected_for_yes[]=delivery&filters_selected_for_yes[]=alcohol&include_featured=1&language=en&lat=31.484023&lng=74.393176&location_id=1&offset=0&os_version=10.3.3&outlet_limit=60&redeemability=redeemable_reusable&session_token=32041547358d0c5edeaa804.53272884&sort=default&user_id=172451'
NAMING_ISSUE = '/v59/outlets?__i=2692567&__platform=ios&app_version=5.90.00&category=Restaurants%20and%20Bars&company=entertainer&currency=AED&device_key=ios-E0BF66D2-B3AE-4450-8FA6-91B3B084E0DC&device_model=iPhone%206S&include_featured=1&language=en&lat=24.473881&lng=54.343074&location_id=4&offset=0&os_version=11.0.3&outlet_limit=60&session_token=32041547358d0c5edeaa804.53272884&sort=default&user_id=172451&redeemability=not_redeemable'
INVALID_ID = '/v59/outlets?__i=2692567&__platform=ios&app_version=5.91.00&category=Restaurants%20and%20Bars&company=entertainer&currency=USD&device_key=ios-90E90E2E-D871-46DD-BA2E-2D273334F6C0&device_model=iPhone%207&include_featured=1&language=en&lat=31.484120&lng=74.393179&location_id=10&offset=0&os_version=11.1.1&outlet_limit=60&redeemability=redeemable_reusable&session_token=32041547358d0c5edeaa804.53272884&&sort=default&user_id=3211293'
HOME = '/v59/home?__i=3682073&__platform=ios&__sid=10088096&app_version=5.91.00&company=entertainer&currency=AED&device_key=ios-AB997B9A-87F9-4BAF-8577-78E912E027C4&device_model=iPhone%206%20Plus&language=en&location_id=2&os_version=10.3&session_token=2567d6d5-ed83-4906-abfc-648159500f3e&user_id=3682073'
RANKINGS = '/v59/user/friends/ranking?session_token=31083971405a5d8f162cbba4.71682356&currency=AED&language=en&__i=3682935&user_id=3682935'
RANKINGS_WITHOUT_PARMS = '/v59/user/friends/ranking?'
CONFIGURRATION_CHEERS = '/v59/configurations/cheers'
USER_PRODUCTS = '/v59/user/2692567/products?session_token=32041547358d0c5edeaa804.53272884&__i=2692567'
USER_PROFIE = '/v59/user/profile?session_token=31083971405a5d8f162cbba4.71682356&__i=3682935'
CONFIGS = '/v59/configs?__sid=10088513&session_token=31083971405a5d8f162cbba4.71682356&__i=3682935'
USER = '/v59/users'
SESSIONS = '/v59/sessions'
DEMOGRAPHIC_STATE = '/v59/user/update/demographic/state'
MAGNETO_LINK = '/v59/users/3682935/magento_autologin_token'
HOTELS = '/v59/hotels'
COUNTRY = '/v59/country'
MERCHANTS = '/v59/merchants'
MERCHAT_NAMES = '/v59/merchantnames'
MERCHAT_NAME = '/v59/merchantname' #Elastic search
MERCHANT_WITH_ID = '/v59/merchants/5315'
MERCHANT_OUTLETS_WITH_ID = '/v59/merchantoutlets/26169'
OUTLET_NAMES_WITHOUT_OFFER_ID = '/v59/outletnames'
OUTLET_NAMES_WITH_OFFER_ID_PYTHON = '/v59/outletnames?outlet_ids[]=5319'
OUTLET_NAMES_WITH_OFFER_ID_PHP = '/v59/outletnames?outlet_ids=5319'
CHEERS = '/v59/configurations/cheers'
SEND_AN_OFFER = '/v59/sharing/send'
SMILES = '/gamify/web/get_user_smiles?user_id=3682935&token=YzZmY2QwMjUxZjM2MThlNTE0NDM3ZWQ3OWEyY2QxN2U&lang=en'
FRIENTS_RANKINGS = '/v59/user/friends/ranking?session_token=31083971405a5d8f162cbba4.71682356&currency=AED&language=en&__i=3682935&user_id=3682935'
SHOWING_SAVING = '/v59/users/3682939/savings?session_token=31083971405a5d8f162cbba4.71682356&currency=AED&language=en&__i=3682935'
ACCEPT_OFFER = '/v59/sharing/accept'
SHARING_SEND_OFFERS = '/v59/sharing/sendoffers?session_token=32041547358d0c5edeaa804.53272884&__i=2692567'
SHARING_RECEIVE_OFFERS = '/v59/sharing/receivedoffers?__i=3682935&session_token=31083971405a5d8f162cbba4.71682356'
FEED_APPBOY = '/v59/feed/appboy'
SMILES_PURCHASE = '/v59/smiles/purchase'
OFFERS = '/v59/outlets?__i=2692567&__platform=ios&__sid=10086660&app_version=5.91.00&billing_country=BH&category=Travel&company=entertainer&currency=USD&device_key=ios-DC99C84A-2BB9-417D-A2E5-5B308F4BFC70&device_model=iPhone%206%20Plus&include_featured=1&language=en&location_id=2&offset=0&os_version=10.3&outlet_limit=60&redeemability=redeemable_reusable&session_token=32041547358d0c5edeaa804.53272884&sort=default&user_id=2692567'
HOME_WITHOUT_PARMS = '/v59/home?'
REDEMPTION = '/v59/redemptions?'
REDEMPTION_SYNC = 'v59/redemptions/sync?'
POST_DATA_FOR_SMILES_PURCHASE = {
    "__i": 2692567,
    "location_id": 1,
    "session_token":"32041547358d0c5edeaa804.53272884",
    "points": 10,
    "app_action_id": 10
}
PARAMS_RANKINGS = {
    'session_token': '31083971405a5d8f162cbba4.71682356',
    '__id':'3682935',
    'user_id':3682935
}
POST_DATA_FOR_APP_BOY = {
    "session_token":"31083971405a5d8f162cbba4.71682356",
    "platform":"ios",
    "user_id":3682930
}
POST_DATA_FOR_DEMOGRAPHIC_STATE = {
    "user_id": 3682935,
    "__i": 3682935,
    "session_token": "31083971405a5d8f162cbba4.71682356"
}
WRONG_DATA_FOR_ACCEPTING_OFFER = {
    "entry_id":326724,
    "status":2,
    "session_token":"31083971405a5d8f162cbba4.71682356",
    "__i":3682935
}
POST_DATA_FOR_SHARING = {
    "offer_id[]":326724,
    "session_token":"31083971405a5d8f162cbba4.71682356",
    "__i":3682935,
    "customer_id":3682935
}
POST_DATA_FOR_REDEMPTION_SYNC_PYTHON = {
    'lng': 74.39315784442998,
    'device_model': 'iPhone 7',
    'app_version': '5.91.00',
    'language': 'en',
    'device_key': 'ios-90E90E2E-D871-46DD-BA2E-2D273334F6C0',
    'merchant_pin': '9999',
    'outlet_id': 15610,
    'lat': 31.48417237477629,
    'isshared': '0',
    'os_version': '11.2.2',
    '__platform': 'ios',
    'session_token': '455a04e4-8d39-403b-9ae6-09c972696ff9',
    'company': 'entertainer',
    'quantity': [1],
    'product_id': '4229',
    'is_reattempt': 0,
    '__i': 172451,
    'transaction_id': 'ios-1515759658-172451-326724-15640',
    '__sid': 10088142,
    'offer_id': [326724],
    'user_id': 172451
    }
POST_DATA_FOR_REDEMPTION_SYNC_PHP = {
    'lng': 74.39315784442998,
    'device_model': 'iPhone 7',
    'app_version': '5.91.00',
    'language': 'en',
    'device_key': 'ios-90E90E2E-D871-46DD-BA2E-2D273334F6C0',
    'merchant_pin': '9999',
    'outlet_id': 15610,
    'lat': 31.48417237477629,
    'isshared': '0',
    'os_version': '11.2.2',
    '__platform': 'ios',
    'session_token': '455a04e4-8d39-403b-9ae6-09c972696ff9',
    'company': 'entertainer',
    'quantity[]': 1,
    'product_id': '4229',
    'is_reattempt': 0,
    '__i': 172451,
    'transaction_id': 'ios-1515759658-172451-326724-15660',
    '__sid': 10088142,
    'offer_id[]': 326724,
    'user_id': 172451
    }
POST_DATA_FOR_REDEMPTION_PYTHON = {
    'lng': 74.39315784442998,
    'device_model': 'iPhone 7',
    'app_version': '5.91.00',
    'language': 'en',
    'device_key': 'ios-90E90E2E-D871-46DD-BA2E-2D273334F6C0',
    'merchant_pin': '9999',
    'outlet_id': 15610,
    'lat': 31.48417237477629,
    'isshared': '0',
    'os_version': '11.2.2',
    '__platform': 'ios',
    'session_token': '455a04e4-8d39-403b-9ae6-09c972696ff9',
    'company': 'entertainer',
    'quantity': [1],
    'product_id': '4229',
    'is_reattempt': 0,
    '__i': 172451,
    'transaction_id': 'ios-1515759658-172451-326724-15641',
    '__sid': 10088142,
    'offer_id': [326724],
    'user_id': 172451
    }
POST_DATA_FOR_REDEMPTION_PHP = {
    'lng': 74.39315784442998,
    'device_model': 'iPhone 7',
    'app_version': '5.91.00',
    'language': 'en',
    'device_key': 'ios-90E90E2E-D871-46DD-BA2E-2D273334F6C0',
    'merchant_pin': '9999',
    'outlet_id': 15610,
    'lat': 31.48417237477629,
    'isshared': '0',
    'os_version': '11.2.2',
    '__platform': 'ios',
    'session_token': '455a04e4-8d39-403b-9ae6-09c972696ff9',
    'company': 'entertainer',
    'quantity[]': 1,
    'product_id': '4229',
    'is_reattempt': 0,
    '__i': 172451,
    'transaction_id': 'ios-1515759658-172451-326724-15661',
    '__sid': 10088142,
    'offer_id[]': 326724,
    'user_id': 172451
    }
POST_DATA_FOR_USER = {
    "firstname":"sa",
    "lastname":"qib",
    "country_of_residence": "PA",
    "email": "",
    "password":"saqib",
    "confirm_password":"saqib",
    "terms_acceptance": 1,
    "language": "en",
    "gender": "Male",
    "app_version": "5.9.0"
}
POST_DATA_FOR_SESSIONS = {
    "email":"testqamsd+h01@gmail.com",
    "device_model": "OPPO F1s",
    "__platform":"android",
    "password": "123456",
    "device_uid": "26bd5f87e8b2c275",
    "device_os": "ios",
    "device_key": "26bd5f87e8b2c275",
    "issocial":"0",
    "device_install_token": "123jk1n2j3nl1i42098",
    "app_version": "5.9.0",
    "language": "en",
    "facebook":"FacebookDummmyAccount",
    "session_token": ""
}
PARAMS_OUTLETS = {
    'offset': '0',
    'os_version': '11.1.1',
    'outlet_limit': '60',
    'include_featured': '1',
    'currency': 'AED',
    'location_id': '1',
    'session_token': '32041547358d0c5edeaa804.53272884',
    'device_model': 'iPhone%207',
    'user_id': '172451',
    'category': 'Restaurants%20and%20Bars',
    'lng': '74.393182',
    'redeemability': 'not_redeemable',
    'app_version': '5.90.00',
    'company': 'entertainer',
    '__platform': 'ios',
    '__i': '2692567',
    'device_key': 'ios-C002387E-908C-45FB-9EAF-768C60455415',
    'language': 'en',
    'sort': 'default',
    'lat': '31.484388'
}
PARAMS_MERCHANTS = {
    '__i': '269256',
    'user_id': '0',
    'company': 'entertainer',
    '__platform': 'ios',
    'lng': '74.393194',
    'session_token': '32041547358d0c5edeaa804.53272884',
    'lat': '31.484087',
    'location_id': '1',
    'os_version': '10.3.3',
    'language': 'en',
    'device_key': 'ios-48195B02-3646-4EDF-A46B-67646935624B',
    'currency': '',
    'app_version': '5.90.00',
    'device_model': 'iPhone%206S'
}
PARAMS_HOME = {
    'language': 'en',
    'device_key': 'ios-AB997B9A-87F9-4BAF-8577-78E912E027C4',
    'device_model': 'iPhone%206%20Plus',
    '__sid': '10088096',
    'app_version': '5.91.00',
    'currency': 'AED',
    'user_id': '3682073',
    'location_id': '2',
    'os_version': '10.3',
    'company': 'entertainer',
    '__i': '3682073',
    'session_token': '2567d6d5-ed83-4906-abfc-648159500f3e',
    '__platform': 'ios'
}
KEYS_RANKINGS = list(PARAMS_RANKINGS.keys())
KEYS_HOME = list(PARAMS_HOME.keys())
KEYS_MERCHANTS = list(PARAMS_MERCHANTS.keys())
KEYS_OUTLETS = list(PARAMS_OUTLETS.keys())

LATLNG = [('31.484388', '74.393182'),
          ('31.48417237477629', '74.39315784442998'),
          ('25.204849', '55.270783'),
          ('35.48417237477629', '92.39315784442998'),]

REDEMIBILITY_OPTIONS = ['all', 'not_redeemable', 'redeemed', 'redeemable', 'reusable', 'redeemable_reusable']
'''for parm in HOME.split('?')[1].split('&'):
    print(parm)
    if len(parm.split('=')) > 1:
        PARAMS_HOME[parm.split('=')[0]] = parm.split(('='))[1]
    else:
        print('one problem')


print(PARAMS_HOME)
'''
PHP_LINK = 'https://apistaging.theentertainerme.com/api_consolidation_v59/web'
PYTHON_LINK = 'http://134.213.138.226/api_consolidation/web'
PYTHON_LINK_ELASTIC_SEARCH = 'http://134.213.138.226:8087/api_consolidation/web'
PHP_LINK_SMILE = 'https://apistaging.theentertainerme.com/gamify/web/get_user_smiles?user_id=3682935&token=YzZmY2QwMjUxZjM2MThlNTE0NDM3ZWQ3OWEyY2QxN2U&lang=en'
PYTHON_LINK_SMILE = 'http://134.213.138.226:8086/gamify/web/get_user_smiles?user_id=3682935&token=YzZmY2QwMjUxZjM2MThlNTE0NDM3ZWQ3OWEyY2QxN2U&lang=en'


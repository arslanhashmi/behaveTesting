"""
Environment file having testing functions in TestAPI class
"""
import random
import string
import timeit
from datetime import datetime
from fake_useragent import UserAgent
from requests.auth import HTTPBasicAuth
from functions.global_variables import *
from functions.graph_functions import *


class TestAPITimings(object):

    END_POINTS = {
        'birthday_deeplink': BIRTHDAY_DEEPLINK,
        'buy_more': BUY_MORE,
        'cheers': CHEERS,
        'configs': CONFIGS,
        'country': COUNTRY,
        'deep_links_not_working': DEEPLINKS_NOT_WORKING,
        'deep_links_not_working_as_expected_brunch': DEEPLINKS_NOT_WORKING_AS_EXPECTED_BRUNCH,
        'delivery_status': IS_DELIVERY_IS_GETTING_TRUE_OR_FALSE,
        'delivery_status_with_multiple_filters': DELIVERY_AND_MULTIPLE_FILTERS,
        'demographic_state': DEMOGRAPHIC_STATE,
        'friends_rankings': FRIENTS_RANKINGS,
        'home': HOME,
        'hotels': HOTELS,
        'invalid_id': INVALID_ID,
        'merchants': MERCHANTS,
        'merchant_outlets_with_id': MERCHANT_OUTLETS_WITH_ID,
        'merchant_with_id': MERCHANT_WITH_ID,
        'merchant_empty_search_scope': EMPTY_SEARCH_SCOPE_MODE,
        'merchant_search_scope': MERCHANT_SEARCH_SCOPE_MODE,
        'merchant_names': MERCHAT_NAMES,
        'merchant_name': MERCHAT_NAME,
        'es_merchant_with_id': MERCHANT_WITH_ID,
        'naming_issue': NAMING_ISSUE,
        'offers': OFFERS,
        'outlets': NOON_AND_KEBAB,
        'outlet_names_without_offer_id': OUTLET_NAMES_WITHOUT_OFFER_ID,
        'outlet_names_with_offer_id': {
            'python': OUTLET_NAMES_WITH_OFFER_ID_PYTHON,
            'php': OUTLET_NAMES_WITH_OFFER_ID_PHP
        },
        'es_outlets': NOON_AND_KEBAB,
        'redemption': REDEMPTION,
        'redemption_sync': REDEMPTION_SYNC,
        'send_offer': SEND_AN_OFFER,
        'accept_offer': ACCEPT_OFFER,
        'sessions': SESSIONS,
        'sharing_send_offers': SHARING_SEND_OFFERS,
        'sharing_receive_offers': SHARING_RECEIVE_OFFERS,
        'showing_savings': SHOWING_SAVING,
        'smiles': SMILES,
        'smiles_purchase': SMILES_PURCHASE,
        'user_products': USER_PRODUCTS,
        'user_profile': USER_PROFIE,
        'user': USER
    }

    POST_DATA = {
        'smiles_purchase': POST_DATA_FOR_SMILES_PURCHASE,
        'demographic_state': POST_DATA_FOR_DEMOGRAPHIC_STATE,
        'send_offer': POST_DATA_FOR_SHARING,
        'redemption_sync': {
            'python': POST_DATA_FOR_REDEMPTION_SYNC_PYTHON,
            'php': POST_DATA_FOR_REDEMPTION_SYNC_PHP
        },
        'redemption': {
            'python': POST_DATA_FOR_REDEMPTION_PYTHON,
            'php': POST_DATA_FOR_REDEMPTION_PHP
        },
        'user': POST_DATA_FOR_USER,
        'sessions': POST_DATA_FOR_SESSIONS,
        'accept_offer': WRONG_DATA_FOR_ACCEPTING_OFFER
    }

    KEYS = {
        'outlets': KEYS_OUTLETS,
        'home': KEYS_HOME
    }

    END_POINTS_WITHOUT_PARMS = {
        'outlets': NOON_AND_KEBAB_WITHOUT_PARMS,
        'home': HOME_WITHOUT_PARMS
    }

    PARAMETERS = {
        'outlets': PARAMS_OUTLETS,
        'home': PARAMS_HOME
    }

    def __init__(self):
        """
        initializing variables to be used is every call
        """
        self.user_agent = UserAgent()
        self.header = {'user-agent': self.user_agent.chrome}
        self.http_auth = HTTPBasicAuth('prototype', 'prototype')
        self.date = str(
            datetime.now()
        ).split(' ')[0] # Setting current date

    def compare_get_response(self, end_point, elastic_search=False):
        """
        comparing get response timings
        :param end_point: end point name
        :param elastic_search: if true then change python link to elastic search
        """
        file_pointer = open('logs/{name}_{date}.txt'.format(
                date=self.date,
                name=end_point
            ),
            'w'
        )

        file_pointer.write('Going to test {name} response timings with correct date at {time}\n'.format(
                time=datetime.now(),
                name=end_point
            )
        )

        time_php = timeit.Timer(
            "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format(
                UPDATED_LINK=self.END_POINTS[end_point],
                header=self.header,
                PHP_LINK=PHP_LINK
            ),
            "import requests; from requests.auth import HTTPBasicAuth"
        )
        times_php = time_php.repeat(API_HITS, 1)

        time_python = timeit.Timer(
            "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},)".format(
                UPDATED_LINK=self.END_POINTS[end_point],
                header=self.header,
                PYTHON_LINK=PYTHON_LINK
            ),
            "import requests; from requests.auth import HTTPBasicAuth"
        )
        times_python = time_python.repeat(API_HITS, 1)

        file_pointer.write("Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format(
                API_HITS=API_HITS,
                average_time=format(
                    sum(times_php) / len(times_php),
                    '.4f'
                )
            )
        )
        file_pointer.write("Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format(
                API_HITS=API_HITS,
                average_time=format(
                    sum(times_python) / len(times_python),
                    '.4f'
                )
            )
        )

        make_box_plot(end_point, times_php, times_python)
        make_subplot(end_point, times_php, times_python)

        file_pointer.write('Test ends for {name} with correct date at {time}'.format(
                time=datetime.now(),
                name=end_point
            )
        )
        file_pointer.close()


    def compare_get_response_different_urls(self, end_point):
            """
            called when python and php has different urls for same end points
            :param
            end_point: name of end point

            """
            file_pointer = open('logs/{name}_{date}.txt'.format(
                    date=self.date,
                    name=end_point
                ),
                'w'
            )

            file_pointer.write('Going to test {name} response timings with correct date at {time}\n'.format(
                    time=datetime.now(),
                    name=end_point
                )
            )

            time_php = timeit.Timer(
                "requests.get('{PHP_LINK}'+'{UPDATED_LINK}', "
                "auth=HTTPBasicAuth('prototype', 'prototype'), "
                "headers = {header},)".format(
                    UPDATED_LINK=self.END_POINTS[end_point]['php'],
                    header=self.header,
                    PHP_LINK=PHP_LINK
                ),
                "import requests; from requests.auth import HTTPBasicAuth"
            )
            times_php = time_php.repeat(API_HITS, 1)

            time_python = timeit.Timer(
                "requests.get('{PYTHON_LINK}'+'{UPDATED_LINK}', "
                "auth=HTTPBasicAuth('prototype', 'prototype'), "
                "headers = {header},)".format(
                    UPDATED_LINK=self.END_POINTS[end_point]['python'],
                    header=self.header,
                    PYTHON_LINK=PYTHON_LINK
                ),
                "import requests; from requests.auth import HTTPBasicAuth"
            )
            times_python = time_python.repeat(API_HITS, 1)

            file_pointer.write("Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format(
                    API_HITS=API_HITS,
                    average_time=format(
                        sum(times_php) / len(times_php),
                        '.4f'
                    )
                )
            )
            file_pointer.write("Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format(
                    API_HITS=API_HITS,
                    average_time=format(
                        sum(times_python) / len(times_python),
                        '.4f'
                    )
                )
            )

            make_box_plot(end_point, times_php, times_python)
            make_subplot(end_point, times_php, times_python)

            file_pointer.write('Test ends for {name} with correct date at {time}'.format(
                    time=datetime.now(),
                    name=end_point
                )
            )
            file_pointer.close()

    def compare_post_response(self, end_point):
        """
        comparing post requests
        :param
        end_point: name of end point

        """
        file_pointer = open('logs/{name}_{date}.txt'.format(
                date=self.date,
                name=end_point
            ),
            'w'
        )

        file_pointer.write('Going to test {name} response timings with correct date at {time}\n'.format(
                time=datetime.now(),
                name=end_point
            )
        )

        time_php = timeit.Timer(
            "requests.post('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},"
            "data={data})".format(
                UPDATED_LINK=self.END_POINTS[end_point],
                header=self.header,
                PHP_LINK=PHP_LINK,
                data=self.POST_DATA[end_point]
            ),
            "import requests; from requests.auth import HTTPBasicAuth"
        )
        times_php = time_php.repeat(API_HITS, 1)

        time_python = timeit.Timer(
            "requests.post('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header}, "
            "data={data})".format(
                UPDATED_LINK=self.END_POINTS[end_point],
                header=self.header,
                PYTHON_LINK=PYTHON_LINK,
                data=self.POST_DATA[end_point]
            ),
            "import requests; from requests.auth import HTTPBasicAuth"
        )
        times_python = time_python.repeat(API_HITS, 1)

        file_pointer.write("Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format(
                API_HITS=API_HITS,
                average_time=format(
                    sum(times_php) / len(times_php),
                    '.4f'
                )
            )
        )
        file_pointer.write("Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format(
                API_HITS=API_HITS,
                average_time=format(
                    sum(times_python) / len(times_python),
                    '.4f'
                )
            )
        )

        make_box_plot(end_point, times_php, times_python)
        make_subplot(end_point, times_php, times_python)

        file_pointer.write('Test ends for {name} with correct date at {time}'.format(
                time=datetime.now(),
                name=end_point
            )
        )
        file_pointer.close()

    def compare_post_response_sign_up(self, end_point):
        """
        used just for sign up new user end point as of having a "random email every time" scenario
        :param
        end_point: name of end point

        """
        file_pointer = open('logs/{name}_{date}.txt'.format(
                date=self.date,
                name=end_point
            ),
            'w'
        )

        file_pointer.write('Going to test {name} response timings with correct date at {time}\n'.format(
                time=datetime.now(),
                name=end_point
            )
        )
        self.POST_DATA[end_point]['email'] = "{email}@gmail.com".format(
            email=random_email()
        )
        time_php = timeit.Timer(
            "requests.post('{PHP_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header},"
            "data={data})".format(
                UPDATED_LINK=self.END_POINTS[end_point],
                header=self.header,
                PHP_LINK=PHP_LINK,
                data=self.POST_DATA[end_point]
            ),
            "import requests; from requests.auth import HTTPBasicAuth"
        )
        times_php = time_php.repeat(API_HITS, 1)

        self.POST_DATA[end_point]['email'] = "{email}@gmail.com".format(
            email=random_email()
        )
        time_python = timeit.Timer(
            "requests.post('{PYTHON_LINK}'+'{UPDATED_LINK}', "
            "auth=HTTPBasicAuth('prototype', 'prototype'), "
            "headers = {header}, "
            "data={data})".format(
                UPDATED_LINK=self.END_POINTS[end_point],
                header=self.header,
                PYTHON_LINK=PYTHON_LINK,
                data=self.POST_DATA[end_point]
            ),
            "import requests; from requests.auth import HTTPBasicAuth"
        )
        times_python = time_python.repeat(API_HITS, 1)

        file_pointer.write("Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format(
                API_HITS=API_HITS,
                average_time=format(
                    sum(times_php) / len(times_php),
                    '.4f'
                )
            )
        )
        file_pointer.write("Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format(
                API_HITS=API_HITS,
                average_time=format(
                    sum(times_python) / len(times_python),
                    '.4f'
                )
            )
        )

        make_box_plot(end_point, times_php, times_python)
        make_subplot(end_point, times_php, times_python)

        file_pointer.write('Test ends for {name} with correct date at {time}'.format(
                time=datetime.now(),
                name=end_point
            )
        )
        file_pointer.close()

    def compare_post_response_different_data(self, end_point):

            """
            When the post data for both python and php is change this function is used
            :param
            end_point: name of end point

            """
            file_pointer = open('logs/{name}_{date}.txt'.format(
                    date=self.date,
                    name=end_point
                ),
                'w'
            )

            file_pointer.write('Going to test {name} response timings with correct date at {time}\n'.format(
                    time=datetime.now(),
                    name=end_point
                )
            )

            time_php = timeit.Timer(
                "requests.post('{PHP_LINK}'+'{UPDATED_LINK}', "
                "auth=HTTPBasicAuth('prototype', 'prototype'), "
                "headers = {header},"
                "data={data})".format(
                    UPDATED_LINK=self.END_POINTS[end_point],
                    header=self.header,
                    PHP_LINK=PHP_LINK,
                    data=self.POST_DATA[end_point]['php']
                ),
                "import requests; from requests.auth import HTTPBasicAuth"
            )
            times_php = time_php.repeat(API_HITS, 1)

            time_python = timeit.Timer(
                "requests.post('{PYTHON_LINK}'+'{UPDATED_LINK}', "
                "auth=HTTPBasicAuth('prototype', 'prototype'), "
                "headers = {header}, "
                "data={data})".format(
                    UPDATED_LINK=self.END_POINTS[end_point],
                    header=self.header,
                    PYTHON_LINK=PYTHON_LINK,
                    data=self.POST_DATA[end_point]['python']
                ),
                "import requests; from requests.auth import HTTPBasicAuth"
            )
            times_python = time_python.repeat(API_HITS, 1)

            file_pointer.write("Average time taken for {API_HITS} Php API hits took: {average_time} secs\n".format(
                    API_HITS=API_HITS,
                    average_time=format(
                        sum(times_php) / len(times_php),
                        '.4f'
                    )
                )
            )
            file_pointer.write("Average time taken for {API_HITS} Python API hits took: {average_time} secs\n".format(
                    API_HITS=API_HITS,
                    average_time=format(
                        sum(times_python) / len(times_python),
                        '.4f'
                    )
                )
            )

            make_box_plot(end_point, times_php, times_python)
            make_subplot(end_point, times_php, times_python)

            file_pointer.write('Test ends for {name} with correct date at {time}'.format(
                    time=datetime.now(),
                    name=end_point
                )
            )
            file_pointer.close()


def before_all(context):
    """
    called in the start when ever tests are run
    :param
    context: context.tester will be used in steps

    """
    context.tester = TestAPITimings()


def after_all(context):
    """
    called at the end of tests execution
    :param
    context: can be used to close some connections if required
    """
    pass


def random_email(string_size=10):
    """
    Used to generate random string on n size
    :param
    n: size of random string
    """
    return (''.join([random.choice(string.ascii_letters + string.digits) for _ in
                     range(string_size)]))


"""
Environment file having testing functions in TestAPI class
"""
import random
import string
from datetime import datetime
import requests
from fake_useragent import UserAgent
from functions.compare_json import *
from requests.auth import HTTPBasicAuth
from testResponses.functions.global_variables import *


class TestAPI(object):

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
        comparing get responses
        :param end_point: end point name
        :param elastic_search: if true then change python link to elastic search
        :return:
        """

        file_pointer = open('logs/{name}_{date}.txt'.format(
                date=self.date,
                name=end_point
            ), 'w'
        )

        file_pointer.write('Going to test {name} with correct date at {time}\n'.format(
                time=datetime.now(),
                name=end_point
            )
        )
        response_php = requests.get('{link}{end_point}'.format(
                link=PHP_LINK,
                end_point=self.END_POINTS[end_point]
            ), auth=self.http_auth, headers=self.header
        )

        response_python = requests.get('{link}{end_point}'.format(
                link=PYTHON_LINK if not elastic_search else PYTHON_LINK_ELASTIC_SEARCH,
                end_point=self.END_POINTS[end_point]
            ), auth=self.http_auth, headers=self.header
        )

        file_pointer.write(
            '{response_php} is php response status code and {response_python} is python response status code\n'.format(
                response_php=response_php.status_code,
                response_python=response_python.status_code
            )
        )

        assert response_php.status_code == response_python.status_code

        try:
            assert compare_data_dictionaries(response_php.json(), response_python.json(), file_pointer)

        except Exception as e:
            file_pointer.write(
                'While comparing JSON an exception occurred: {exception}\n'.format(
                    exception=e
                )
            )

        finally:
            file_pointer.write('Test ends for {name} with correct date at {time}'.format(
                    time=datetime.now(),
                    name=end_point
                )
            )
            file_pointer.close()

    def compare_get_response_with_missing_arguments(self, end_point):
        """
        Used when checking different scenarios with skipping arguments.
        :param end_point: name of the end point
        :return:
        """

        file_pointer = open('logs/{name}_{date}.txt'.format(
                date=self.date,
                name=end_point
            ), 'w'
        )

        for parameter in self.KEYS[end_point]:
            updated_link = self.END_POINTS_WITHOUT_PARMS[end_point]

            file_pointer.write('Going to test {name} with skipping {parameter} at {time}\n'.format(
                    time=datetime.now(),
                    parameter=parameter,
                    name=end_point
                )
            )

            for param, value in self.PARAMETERS[end_point].items():
                if param is not parameter: #which is going to be skipped
                    updated_link = "{link}{parm}={val}&".format(
                        link=updated_link,
                        parm=param,
                        val=value
                    )

            updated_link = updated_link[0:len(updated_link) - 1] #removing & from end

            file_pointer.write('Going to test {name} with correct date at {time}\n'.format(
                    time=datetime.now(),
                    name=end_point
                )
            )

            response_php = requests.get('{link}{end_point}'.format(
                    link=PHP_LINK,
                    end_point=updated_link
                ),
                auth=self.http_auth,
                headers=self.header
            )

            response_python = requests.get('{link}{end_point}'.format(
                    link=PYTHON_LINK,
                    end_point=updated_link
                ),
                auth=self.http_auth,
                headers=self.header
            )

            file_pointer.write(
                '{response_php} is php response status code and {response_python} is python response status code\n'.format(
                    response_php=response_php.status_code,
                    response_python=response_python.status_code
                )
            )

            assert response_php.status_code == response_python.status_code

            try:
                assert compare_data_dictionaries(response_php.json(), response_python.json(), file_pointer)

            except Exception as e:
                file_pointer.write('Going to test {name} with skipping {parameter} at {time}\n'.format(
                        time=datetime.now(),
                        parameter=parameter,
                        name=end_point
                    )
                )

            finally:
                file_pointer.write('Going to test {name} with correct date at {time}\n'.format(
                        time=datetime.now(),
                        name=end_point
                    )
                )
        file_pointer.close()

    def compare_get_response_different_urls(self, end_point):
            """
            called when python and php has different urls for same end points
            :param end_point: name of end point
            :return:
            """
            file_pointer = open('logs/{name}_{date}.txt'.format(
                    date=self.date,
                    name=end_point
                ), 'w'
            )

            file_pointer.write('Going to test {name} with correct date at {time}\n'.format(
                    time=datetime.now(),
                    name=end_point
                )
            )
            response_php = requests.get('{link}{end_point}'.format(
                    link=PHP_LINK,
                    end_point=self.END_POINTS[end_point]['php']
                ),
                auth=self.http_auth,
                headers=self.header
            )

            response_python = requests.get('{link}{end_point}'.format(
                    link=PYTHON_LINK,
                    end_point=self.END_POINTS['python'][end_point]
                ),
                auth=self.http_auth,
                headers=self.header
            )

            file_pointer.write(
                '{response_php} is php response status code and {response_python} is python response status code\n'.format(
                    response_php=response_php.status_code,
                    response_python=response_python.status_code
                )
            )

            assert response_php.status_code == response_python.status_code

            try:
                assert compare_data_dictionaries(response_php.json(), response_python.json(), file_pointer)

            except Exception as e:
                file_pointer.write(
                    'While comparing JSON an exception occurred: {exception}\n'.format(
                        exception=e
                    )
                )

            finally:
                file_pointer.write('Test ends for {name} with correct date at {time}'.format(
                        time=datetime.now(),
                        name=end_point
                    )
                )
                file_pointer.close()

    def compare_post_response(self, end_point):
        """
        comparing post requests
        :param end_point: name of end point
        :return:
        """

        file_pointer = open('logs/{name}_{date}.txt'.format(
                date=self.date,
                name=end_point
            ), 'w'
        )

        file_pointer.write('Going to test {name} with correct date at {time}\n'.format(
                time=datetime.now(),
                name=end_point
            )
        )

        response_php = requests.post('{link}{end_point}'.format(
                link=PHP_LINK,
                end_point=self.END_POINTS[end_point]
            ),
            auth=self.http_auth,
            headers=self.header,
            data=self.POST_DATA[end_point]
        )

        response_python = requests.post('{link}{end_point}'.format(
                link=PYTHON_LINK,
                end_point=self.END_POINTS[end_point]
            ),
            auth=self.http_auth,
            headers=self.header,
            data=self.POST_DATA[end_point]
        )

        file_pointer.write(
            '{response_php} is php response status code and {response_python} is python response status code\n'.format(
                response_php=response_php.status_code,
                response_python=response_python.status_code
            )
        )

        assert response_php.status_code == response_python.status_code

        try:
            assert compare_data_dictionaries(response_php.json(), response_python.json(), file_pointer)

        except Exception as e:
            file_pointer.write(
                'While comparing JSON an exception occurred: {exception}\n'.format(
                    exception=e
                )
            )

        finally:
            file_pointer.write('Test ends for {name} with correct date at {time}'.format(
                    time=datetime.now(),
                    name=end_point
                )
            )
            file_pointer.close()

    def compare_post_response_sign_up(self, end_point):
        """

        :param end_point: name of end point
        :return:
        """
        file_pointer = open('logs/{name}_{date}.txt'.format(
                date=self.date,
                name=end_point
            ), 'w'
        )

        file_pointer.write('Going to test {name} with correct date at {time}\n'.format(
                time=datetime.now(),
                name=end_point
            )
        )

        self.POST_DATA[end_point]['email'] = "{email}@gmail.com".format(
            email=random_email()
        )
        response_php = requests.post('{link}{end_point}'.format(
                link=PHP_LINK,
                end_point=self.END_POINTS[end_point]
            ),
            auth=self.http_auth,
            headers=self.header,
            data=self.POST_DATA[end_point]
        )

        self.POST_DATA[end_point]['email'] = "{email}@yahoo.com".format(
            email=random_email()
        )
        response_python = requests.post('{link}{end_point}'.format(
                link=PYTHON_LINK,
                end_point=self.END_POINTS[end_point]
            ),
            auth=self.http_auth,
            headers=self.header,
            data=self.POST_DATA[end_point]
        )

        file_pointer.write(
            '{response_php} is php response status code and {response_python} is python response status code\n'.format(
                response_php=response_php.status_code,
                response_python=response_python.status_code
            )
        )

        assert response_php.status_code == response_python.status_code

        try:
            assert compare_data_dictionaries(response_php.json(), response_python.json(), file_pointer)

        except Exception as e:
            file_pointer.write(
                'While comparing JSON an exception occurred: {exception}\n'.format(
                    exception=e
                )
            )

        finally:
            file_pointer.write('Test ends for {name} with correct date at {time}'.format(
                    time=datetime.now(),
                    name=end_point
                )
            )
            file_pointer.close()

    def compare_post_response_different_data(self, end_point):

            """
            When the post data for both python and php is change this function is used
            :param end_point: name of end point
            :return:
            """
            file_pointer = open('logs/{name}_{date}.txt'.format(
                    date=self.date,
                    name=end_point
                ), 'w'
            )

            file_pointer.write('Going to test {name} with correct date at {time}\n'.format(
                    time=datetime.now(),
                    name=end_point
                )
            )

            response_php = requests.post('{link}{end_point}'.format(
                    link=PHP_LINK,
                    end_point=self.END_POINTS[end_point]
                ),
                auth=self.http_auth,
                headers=self.header,
                data=self.POST_DATA[end_point]['php']
            )


            response_python = requests.post('{link}{end_point}'.format(
                    link=PYTHON_LINK,
                    end_point=self.END_POINTS[end_point]
                ),
                auth=self.http_auth,
                headers=self.header,
                data=self.POST_DATA[end_point]['python']
            )

            file_pointer.write(
                '{response_php} is php response status code and {response_python} is python response status code\n'.format(
                    response_php=response_php.status_code,
                    response_python=response_python.status_code
                )
            )

            assert response_php.status_code == response_python.status_code

            try:
                assert compare_data_dictionaries(response_php.json(), response_python.json(), file_pointer)

            except Exception as e:
                file_pointer.write(
                    'While comparing JSON an exception occurred: {exception}\n'.format(
                        exception=e
                    )
                )

            finally:
                file_pointer.write('Test ends for {name} with correct date at {time}'.format(
                        time=datetime.now(),
                        name=end_point
                    )
                )
                file_pointer.close()


def before_all(context):
    """
    called in the start when ever tests are run
    :param context: context.tester will be used in steps
    :return:
    """
    context.tester = TestAPI()


def after_all(context):
    """
    called at the end of tests execution
    :param context:
    :return:
    """
    pass


def random_email(n=10):
    """
    Used to generate random string on n size
    """
    return (''.join([random.choice(string.ascii_letters + string.digits) for _ in
                     range(n)]))


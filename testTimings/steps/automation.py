"""
Decorators for implementing Gerkins scenarios
"""

from behave import given, then, when


@given('Test "{end_point}" get-request')
def compare_get_request(context, end_point):
    context.tester.compare_get_response(end_point)


@given('Test "{end_point}" get-request elastic search')
def compare_get_request(context, end_point):
    context.tester.compare_get_response(end_point, elastic_search=True)


@given('Test "{end_point}" get-request with different urls for php and python')
def compare_get_request_different_urls(context, end_point):
    context.tester.compare_get_response_different_urls(end_point)


@given('Test "{end_point}" post-request')
def compare_get_request(context, end_point):
    context.tester.compare_post_response(end_point)


@given('Test "{end_point}" post-request sign up')
def compare_get_request(context, end_point):
    context.tester.compare_post_response_sign_up(end_point)


@given('Test "{end_point}" post-request different data')
def compare_get_request(context, end_point):
    context.tester.compare_post_response_different_data(end_point)


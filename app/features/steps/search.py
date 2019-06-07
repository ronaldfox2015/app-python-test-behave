import requests
from behave import *
from schemas.search import SearchSchema 

## BACKGROUND ##

@given('I access the resource')
def step_impl(context):
	context.response_len = 0

## SCENARIO: Search a announcement by id ##

@given('I put the information of the location')
def step_impl(context):
	pass

@when("I search the q {q}")
def step_impl(context, q):
	payload = {'id': q}
	r = requests.get(context.resource_url+"locations", params=payload)
	print(r.encode('utf-8').strip().json())

	context.response_len = len(r.json()['results'])
	context.response_status_code = r.status_code

@then("The quantity of result should be {expected_response_len:d}")
def step_impl(context, expected_response_len):
	assert context.response_len == expected_response_len

## SCENARIO: Search announcements ##

@given('I search announcements')
def step_impl(context):
	pass

@when("I dont use filters")
def step_impl(context):
	r = requests.get(context.resource_url)
	context.response = r.json()
	context.response_status_code = r.status_code

@then("The result should be a list of announcements")
def step_impl(context):
	errors = SearchSchema().validate(context.response)
	assert {} == errors

## DEFAULT THEN ##

@then("The status code should be {expected_status_code:d}")
def step_impl(context, expected_status_code):
	assert context.response_status_code == expected_status_code
from behave import *

use_step_matcher("parse")

@given(u'Exists a vehicle registered by "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists a vehicle registered by "user1"')


@when(u'I edit the vehicle with type "Car"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit the vehicle with type "Car"')


@then(u'I\'m viewing the details page for vehicle by "user1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the details page for vehicle by "user1"')


@then(u'There are 1 vehicle')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 vehicle')


@when(u'I edit the vehicle with plate number "12345ABC"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit the vehicle with plate number "12345ABC"')

@given(u'Exists vehicle registered by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists vehicle registered by "user"')

@given(u'Exists parking spot')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists parking spot')

@when(u'I register vehicle')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register vehicle')


@then(u'There are 1 vehicles')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 vehicles')


@then(u'There are 0 vehicles')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 0 vehicles')
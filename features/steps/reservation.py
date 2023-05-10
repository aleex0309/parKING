from behave import *

use_step_matcher("parse")

@given(u'Exists reservation registered by "user"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists reservation registered by "user"')

@when(u'I edit the date of the reservation of the vehicle "AudiA3"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit the date of the reservation of the vehicle "AudiA3"')

@then(u'I\'m viewing the user dashboard with the reservation date updated')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the user dashboard with the reservation date updated')


@then(u'There are 1 reservation')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 1 reservation')


@when(u'I cancel the reservation for vehicle "AudiA3"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I cancel the reservation for vehicle "AudiA3"')


@then(u'I\'m viewing the user dashboard with the reservation cancelled')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the user dashboard with the reservation cancelled')


@then(u'There are 0 reservations')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There are 0 reservations')

@when(u'I register reservation at parking spot "UdL"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I register reservation at parking spot "UdL"')


@then(u'I\'m viewing the user dashboard with the recently created reservation listed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the user dashboard with the recently created reservation listed')
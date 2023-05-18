from behave import *
from django.db.models import Q

use_step_matcher("parse")

@given(u'Exists reservation registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from web.models import Reservation
    for row in context.table:
        reservation = Reservation(user=user)
        for heading in row.headings:
            setattr(reservation, heading, row[heading])
        reservation.save()

@when(u'I register reservation at parking spot "UdL"')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('web:reserve'))
        if context.browser.url == context.get_url('web:reserve'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_tag('button').first.click()

@then(u'There are {count:n} reservation')
def step_impl(context, count):
    from web.models import Reservation
    assert Reservation.objects.count() == count

@then(u'I\'m viewing the user dashboard with the recently created reservation listed')
def step_impl(context):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(user=User.objects.get(username='user')))
    from web.models import Reservation
    assert Reservation.objects.filter(*q_list).count() == 1

@when(u'I edit the date of the reservation of the vehicle "12345ABC"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I edit the date of the reservation of the vehicle "12345ABC"')


@then(u'I\'m viewing the user dashboard with the reservation date updated')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the user dashboard with the reservation date updated')


@when(u'I cancel the reservation for vehicle "12345ABC"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I cancel the reservation for vehicle "12345ABC"')


@then(u'I\'m viewing the user dashboard with the reservation cancelled')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I\'m viewing the user dashboard with the reservation cancelled')

@given(u'Exists parking spot')
def step_impl(context):
    from web.models import ParkingSpot
    for row in context.table:
        parking_spot = ParkingSpot()
        for heading in row.headings:
            setattr(parking_spot, heading, row[heading])
        parking_spot.save()





from behave import *
from django.db.models import Q

use_step_matcher("parse")

@given(u'Exists vehicle registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from web.models import Vehicle
    for row in context.table:
        vehicle = Vehicle(user=user)
        for heading in row.headings:
            setattr(vehicle, heading, row[heading])
        vehicle.save()

@when(u'I register vehicle')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('web:vehicle_create'))
        if context.browser.url == context.get_url('web:vehicle_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_tag('button').first.click()

@then(u'There are {count:n} vehicle')
def step_impl(context, count):
    from web.models import Vehicle
    assert Vehicle.objects.count() == count

@when(u'I edit the vehicle with plate number "12345ABC"')
def step_impl(context):
    from web.models import Vehicle
    vehicle = Vehicle.objects.get(plate_number='12345ABC')
    context.browser.visit(context.get_url('web:vehicle_edit', vehicle.pk))
    if context.browser.url == context.get_url('web:vehicle_edit', vehicle.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[heading])
        form.find_by_tag('button').first.click()


@then(u'I\'m viewing the details page for vehicle by "user"')
def step_impl(context):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(user=User.objects.get(username='user')))
    from web.models import Reservation
    assert Reservation.objects.filter(*q_list).count() == 1
#!/usr/bin/env python


from behave import given, when, then
from grupos_personas import Group, Person

'''
Trabajo Practico numero 4 parte 2 Behave
Curso de Python noviembre - diciembre 2016
Pfluger Federico Andres
'''


@given('The Person "{p1}" called "{name1}" and is "{age1}" years,')
def step_impl(context, p1, name1, age1):
    context.p1 = Person(name1, int(age1))


@given(u'the Person "{p2}" called "{name2}" and is "{age2}" years')
def step_impl(context, p2, name2, age2):
    context.p2 = Person(name2, int(age2))


@when('we add these 2 people')
def step_impl(context):
    try:
        context.sum2people = context.p1 + context.p2
        assert True
    except Exception as err:
        context.error = err
        assert False


@then('we get a Group of 2 people Containing them')
def step_impl(context):
    assert (
        isinstance(context.sum2people, Group) and
        len(context.sum2people) == 2 and
        context.p1 in context.sum2people and
        context.p2 in context.sum2people)

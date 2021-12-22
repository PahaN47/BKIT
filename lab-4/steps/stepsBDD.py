from behave import given, when, then
from prog import biquad_roots

@given("coefficients {a:g}, {b:g}, {c:g}")
def given_c(context, a, b, c):
    context.a = a
    context.b = b
    context.c = c

@when("the roots get calculated")
def calculation(context):
    context.result = biquad_roots(context.a, context.b, context.c)

@then("they are [{result}]")
def get_result(context, result):
    result_list = []
    for value in result.split(', '):
        try:
            result_list.append(float(value))
        except ValueError:
            pass
    assert context.result == result_list

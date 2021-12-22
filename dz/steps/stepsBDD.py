from behave import given, when, then
from custom_filter import CurrentState
from values import state
import values
import plotter
import os

@given("required states are {required_states}, current state is {current_state}")
def given_c(context, required_states, current_state):
    values.current_state = state[current_state]
    context.required_states = list(map(state.__getitem__, required_states.split(', ')))

@when("checking for state")
def calculation(context):
    context.result = CurrentState.check(None, context.required_states)

@then("current state being in required is {result}")
def get_result(context, result):
    result = bool(result)
    assert context.result == result

@given("the plotted function is '{fstr}'")
def given_c(context, fstr):
    context.plot_path = plotter.plot(fstr)

@when("plotting and saving the file")
def calculation(context):
    context.result = os.path.exists(context.plot_path)

@then("it is {result} that the file is there")
def get_result(context, result):
    result = bool(result)
    assert context.result == result
    if result:
        os.remove(context.plot_path)

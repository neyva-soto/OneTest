from assertpy import assert_that
from behave import given, when, then

from src.pages.login.login_page import LoginPage


@given(u'The user is on the login page')
def the_user_is_on_the_page(context):
    login_page = LoginPage(context)
    login_page.open()
    context.search_summary_at_very_beginning = login_page.get_summary_text()


@when(u'the user enters the value "{value}" in the text-input for username')
def the_user_enters_the_value_in_the_username_text_input(context, value):
    login_page = LoginPage(context)
    login_page.set_search_user_input(value)


@when(u'the user enters the value "{value}" in the text-input for password')
def the_user_enters_the_value_in_the_password_text_input(context, value):
    login_page = LoginPage(context)
    login_page.set_search_pass_input(value)


@when(u'the user clicks login button')
def the_user_clears_filters(context):
    login_page = LoginPage(context)
    login_page.login_button_click()


@then(u'the user should see the following text in the page "{value}"')
def the_user_should_see_the_following_result_summary(context, value):
    login_page = LoginPage(context)
    summary_text = login_page.get_dashboard_text()
    assert_that(summary_text).is_equal_to(value)


@then(u'I see input field in the page with id "{id_selector}"')
def step_the_user_should_see_the_field(context, id_selector):
    login_page = LoginPage(context)
    input_field = login_page.verify_input_field(id_selector)
    assert_that(input_field).is_not_none()



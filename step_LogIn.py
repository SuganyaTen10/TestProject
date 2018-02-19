from behave import *

use_step_matcher("re")


@when("user clicks on LogIn Link")
def step_impl(context):
    context.browser.find_element_by_link_text('Log in').click()


@then("the user should navigate to LogIn User page")
def step_impl(context):
    context.browser.forward()


@given("Students Admin user is on LogIn page")
def step_impl(context):
    # context.browser.get("http://localhost/WebIndividual/Account/Login")
    assert context.browser.title == "Log in - Contoso University"


@when("user provides Email,Password as mandatory details")
def step_impl(context):
    user_element = context.browser.find_element_by_name('ctl00$MainContent$Email')
    user_element.send_keys('user1@mail.com')
    ps_element = context.browser.find_element_by_name('ctl00$MainContent$Password')
    ps_element.send_keys('P@ssw0rd')


@step("clicks LogIn button")
def step_impl(context):
    context.browser.find_element_by_name('ctl00$MainContent$ctl05').click()
     #getLogin.click()


@step("user must have Hello,UserName! in navigation bar")
def step_impl(context):
    context.browser.forward()
    assert "Hello, user1@mail.com !" in context.browser.page_source


@step("user must have 'Log off' link to log off")
def step_impl(context):
    context.browser.find_element_by_link_text('Log off').click()
    context.browser.forward()
# allure.attach(context.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
# context.allure_report

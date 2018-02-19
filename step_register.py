from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pyodbc

use_step_matcher("re")


@given("Students Admin user is on Home Page")
def step_impl(context):
    context.browser.get("http://localhost/WebIndividual")
    assert context.browser.title == "Home Page - Contoso University"


@when("user clicks on Register Link")
def step_impl(context):
    context.browser.find_element_by_link_text('Register').click()


@then("the user should navigate to Register User page")
def step_impl(context):
    assert context.browser.title == "Register - Contoso University"


@given("Students Admin user is on Register new user page")
def step_impl(context):
    context.browser.get("http://localhost/WebIndividual/Account/Register")
    assert context.browser.title == "Register - Contoso University"


@when("user provides Email,Password,ConfirmPassword as mandatory details")
def step_impl(context):
    user_element = context.browser.find_element_by_name('ctl00$MainContent$Email')
    user_element.send_keys('user@mail.com')
    ps_element = context.browser.find_element_by_name('ctl00$MainContent$Password')
    ps_element.send_keys('P@ssw0rd')
    cps_element = context.browser.find_element_by_name('ctl00$MainContent$ConfirmPassword')
    cps_element.send_keys('P@ssw0rd')


@when("clicks Register button")
def step_impl(context):
    context.browser.find_element_by_name('ctl00$MainContent$ctl08').click()


@then("user detail must be added")
def step_impl(context):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"  # your host
                          "Server=W10180110;"
                          "Database=WebIndividual;"
                          "Trusted_Connection=yes;"
                          "UID=WebIndividual;PWD=india123")

    cursor = cnxn.cursor()
    cursor.execute("SELECT UserName FROM AspNetUsers where Email like 'user%@mail.com'")

    for row in cursor:
        print('row = %r' % (row,))


@then("user should navigate to Home page")
def step_impl(context):
    context.browser.forward()


@then("Navigation bar must have Hello,UserName!")
def step_impl(context):
    context.browser.forward()
    assert "Hello, user@mail.com !" in context.browser.page_source


@when("user provides Email and mismatching Password and Confirm Password")
def step_impl(context):
    user_element = context.browser.find_element_by_name('ctl00$MainContent$Email')
    user_element.send_keys('userpsd@mail.com')
    ps_element = context.browser.find_element_by_name('ctl00$MainContent$Password')
    ps_element.send_keys('P@ssw0rd')
    cps_element = context.browser.find_element_by_name('ctl00$MainContent$ConfirmPassword')
    cps_element.send_keys('P@ssw0rd1')


@then("error message must be displayed as 'Password and Confirm Password do not match'")
def step_impl(context):
    assert "The password and confirmation password do not match." in context.browser.page_source


@then("user detail must not be added")
def step_impl(context):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"  # your host
                          "Server=W10180110;"
                          "Database=WebIndividual;"
                          "Trusted_Connection=yes;"
                          "UID=WebIndividual;PWD=india123")

    cursor = cnxn.cursor()
    cursor.execute("SELECT UserName FROM AspNetUsers where Email like 'user%@mail.com'")

    for row in cursor:
        print('row = %r' % (row,))


@step("error message must be displayed as 'Name user@mail\.com is already taken\.'")
def step_impl(context):
    assert "Name user@mail.com is already taken." in context.browser.page_source

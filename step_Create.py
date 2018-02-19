from behave import *
import pyodbc
from selenium.webdriver.support.ui import Select

use_step_matcher("re")


@given("Students Admin user is on Student Account Page")
def step_impl(context):
    context.browser.get("http://localhost/WebIndividual/Account/Students")
    user_element = context.browser.find_element_by_name('ctl00$MainContent$Email')
    user_element.send_keys('user1@mail.com')
    ps_element = context.browser.find_element_by_name('ctl00$MainContent$Password')
    ps_element.send_keys('P@ssw0rd')
    context.browser.find_element_by_name('ctl00$MainContent$ctl05').click()
    context.browser.forward()
    context.browser.find_element_by_link_text('Students').click()


@when("user wants to add new student")
def step_impl(context):
    context.browser.forward()


@then('there must be a link as "Add New Student"')
def step_impl(context):
    context.browser.find_element_by_link_text('Add New Student').click()


@step("clicking the link should navigate to Add Students Page")
def step_impl(context):
    context.browser.forward()


@given("Students Admin user is on Add Student Page")
def step_impl(context):
    pass


@when("user provides FirstName,LastName, Academic Year as mandatory details")
def step_impl(context):
    last_name = context.browser.find_element_by_name('ctl00$MainContent$addStudentForm$ctl04$ctl00$__LastName$TextBox1')
    last_name.send_keys('Test')
    first_name = context.browser.find_element_by_name('ctl00$MainContent$addStudentForm$ctl04$ctl01$__FirstName$TextBox1')
    first_name.send_keys('TestStudent')
    year = Select(context.browser.find_element_by_name('ctl00$MainContent$addStudentForm$ctl04$ctl02$__Year$DropDownList1'))
    year.select_by_visible_text('Junior')
    context.browser.find_element_by_name('ctl00$MainContent$addStudentForm$ctl02').click()
    context.browser.forward()


@then("clicking Insert button should add the Student detail")
def step_impl(context):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"  # your host
                          "Server=W10180110;"
                          "Database=WebIndividual;"
                          "Trusted_Connection=yes;"
                          "UID=WebIndividual;PWD=india123")

    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Students where FirstName like 'TestStudent%'")

    for row in cursor:
        print('row = %r' % (row,))
    assert False


@step("the user should navigate to Students page")
def step_impl(context):
    context.browser.forward()


@given("Students Admin user is again on Add Student Page")
def step_impl(context):
    context.browser.find_element_by_link_text('Add New Student').click()


@when("user decides to cancel the addition of new Student")
def step_impl(context):
    cancel = context.browser.find_element_by_name('ctl00$MainContent$addStudentForm$ctl03')
    cancel.is_enabled()


@then("clicking cancel button should cancel the addition")
def step_impl(context):
    last_name = context.browser.find_element_by_name('ctl00$MainContent$addStudentForm$ctl04$ctl00$__LastName$TextBox1')
    last_name.send_keys('Test')
    context.browser.find_element_by_name('ctl00$MainContent$addStudentForm$ctl03').click()
    context.browser.forward()

from behave import *
import pyodbc
from selenium.webdriver.support.ui import Select
#import page

use_step_matcher("re")


@when("user wants to edit a student")
def step_impl(context):
    context.browser.forward()


@then('there must be a link as "Edit"')
def step_impl(context):
    context.browser.forward()


@step("clicking the link should navigate to Edit Students Page")
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="MainContent_GridView1"]/tbody/tr[2]/td[1]/a[1]').click()


@given("Students Admin user is on Edit Student Page")
def step_impl(context):
    """
        :type context: behave.runner.Context
        """
    pass


@when("user wants to edit FirstName,LastName,Academic Year")
def step_impl(context):
    last_name = context.browser.find_element_by_xpath('//*[@id="MainContent_GridView1___LastName_0_TextBox1_0"]')
    last_name.send_keys('edit')
    first_name = context.browser.find_element_by_xpath('//*[@id="MainContent_GridView1___FirstName_0_TextBox1_0"]')
    first_name.send_keys('edit')
    year = Select(context.browser.find_element_by_xpath('//*[@id="MainContent_GridView1___Year_0_DropDownList1_0"]'))
    year.select_by_value('3')



@then("clicking Update button should update the Student detail")
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="MainContent_GridView1"]/tbody/tr[2]/td[1]/a[1]').click()


@given("Students Admin user is again on Edit Student Page")
def step_impl(context):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"  # your host
                          "Server=W10180110;"
                          "Database=WebIndividual;"
                          "Trusted_Connection=yes;"
                          "UID=WebIndividual;PWD=india123")

    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Students where FirstName like '%edit%'")

    for row in cursor:
        print('row = %r' % (row,))


@when("user decides to cancel editing Student details")
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="MainContent_GridView1"]/tbody/tr[2]/td[1]/a[1]').click()


@then("clicking cancel button should cancel the edit")
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="MainContent_GridView1"]/tbody/tr[2]/td[1]/a[2]').click()
    context.browser.forward()



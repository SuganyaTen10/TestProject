from behave import *
import pyodbc

use_step_matcher("re")


@when("user wants to delete a student detail")
def step_impl(context):
    context.browser.forward()


@then('there must be a link as "Delete"')
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="MainContent_GridView1"]/tbody/tr[13]/td[1]/a[2]').click()


@step("clicking the link should delete a student from list")
def step_impl(context):
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"  # your host
                          "Server=W10180110;"
                          "Database=WebIndividual;"
                          "Trusted_Connection=yes;"
                          "UID=WebIndividual;PWD=india123")

    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Students ")

    for row in cursor:
        print('row = %r' % (row,))


@step("user should be in the same Students page")
def step_impl(context):
    context.browser.forward()
    assert False

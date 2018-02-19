import unittest
from selenium import webdriver


def before_all(context):
    print("Executing before all")
    # context.browser = webdriver.Chrome(executable_path=r"chromedriver.exe")


def before_feature(context, feature):
    print("Before feature\n")
    context.browser = webdriver.Chrome(executable_path=r"chromedriver.exe")


# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):
    # context.browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
    print("Before scenario\n")


def after_scenario(context, scenario):
    #  context.browser.quit()

    print("After scenario\n")


def after_feature(context, feature):
    print("\nAfter feature")
    context.browser.quit()


def after_all(context):
    print("Executing after all")
    # context.browser.quit()

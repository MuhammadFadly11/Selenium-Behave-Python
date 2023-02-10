from behave import *
from selenium.webdriver.common.by import By

@given(u'Open Home Page')
def step_impl(context):
    context.browser.get("https://www.saucedemo.com/")
    assert(context.browser.title) == "Swag Labs"

@given(u'I Fill my credentials')
def step_impl(context):
    context.browser.find_element(By.ID, "user-name").send_keys("standard_user")
    context.browser.find_element(By.ID, "password").send_keys("secret_sauce")

@when(u'I Click Login Button')
def step_impl(context):
    context.browser.find_element(By.ID, "login-button").click()


@then(u'I should be logged in')
def step_impl(context):
    assert(context.browser.find_element(By.CSS_SELECTOR, "span.title").text) == "PRODUCTS"

@given(u'I Fill my credentials with wrong email')
def step_impl(context):
    context.browser.find_element(By.ID, "user-name").send_keys("standard_users")
    context.browser.find_element(By.ID, "password").send_keys("secret_sauce")


@then(u'I should not be logged in')
def step_impl(context):
    assert(context.browser.title) == "Swag Labs"


@then(u'I should see the error message')
def step_impl(context):
    assert(context.browser.find_element(By.CSS_SELECTOR, "div.error-message-container").text) == "Epic sadface: Username and password do not match any user in this service"

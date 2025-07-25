from pageObjects.login import LoginPage
from utils.api_framework_base import APIUtils
from pytest_bdd import given, when, then, scenarios, parsers
import pytest
import time

scenarios('features/orderTransaction.feature')


@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('Place the item order with {username} and {password}'))
def place_item_order(playwright, shared_data, username, password):
    user_credentials = {
        "userEmail": username,
        "userPassword": password
    }

    api_utils = APIUtils()
    orderId = api_utils.create_order(playwright, user_credentials)
    shared_data['orderId'] = orderId
    print("OrderId = ", orderId)


@given('the user is on the landing page')
def user_on_landing_page(browserInstance, shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    shared_data['loginPage'] = loginPage
    assert "login" in browserInstance.url


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    loginPage = shared_data['loginPage']
    dashboardPage = loginPage.login(username, password)
    shared_data['dashboardPage'] = dashboardPage


@when('Navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data['dashboardPage']
    ordersHistoryPage = dashboardPage.selectOrdersNavLink()
    shared_data['ordersHistoryPage'] = ordersHistoryPage


@when('Select the orderId')
def select_order_id(shared_data):
    ordersHistoryPage = shared_data['ordersHistoryPage']
    orderId = shared_data['orderId']
    orderDetailsPage = ordersHistoryPage.selectOrder(orderId)
    shared_data['orderDetailsPage'] = orderDetailsPage


@then('Order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    orderDetailsPage = shared_data['orderDetailsPage']
    orderDetailsPage.verifyOrderMessage()
    time.sleep(5)

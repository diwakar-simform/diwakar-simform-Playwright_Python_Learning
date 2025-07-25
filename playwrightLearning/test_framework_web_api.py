import json
from playwright.sync_api import Page, expect, Playwright
import time

import pytest
from pageObjects.login import LoginPage
from utils.api_framework_base import APIUtils

# Converting JSON --> Utils --> Python object like list, dictionary' # Well dictionary is also like a json file
with open('data/credentials.json','r') as f:
    jsonData = json.load(f) # here load is a method which converts json file into python object
    print(jsonData)
    user_credentials_list = jsonData["userCredentials"]
    print("user_credentials_list = ", user_credentials_list)


# Task: Place an order using api calls
@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, browserInstance, user_credentials): # user_credentials is a fixture
    page = browserInstance
    
    userEmail = user_credentials["userEmail"]
    userPassword = user_credentials["userPassword"]

    # Step1: Login
    loginPage = LoginPage(page)
    loginPage.navigate()
    assert "login" in page.url
    dashboardPage = loginPage.login(userEmail, userPassword)

    # Step2: Create order --> Get orderId
    api_utils = APIUtils()
    orderId = api_utils.create_order(playwright, user_credentials)
    print("OrderId = ",orderId)

    # Step3: Go to order History page --> Verify order is present or not
    ordersHistoryPage = dashboardPage.selectOrdersNavLink()
    orderDetailsPage = ordersHistoryPage.selectOrder(orderId) 
    orderDetailsPage.verifyOrderMessage()

    time.sleep(5)

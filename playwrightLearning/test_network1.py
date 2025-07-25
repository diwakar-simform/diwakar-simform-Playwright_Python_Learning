from playwright.sync_api import Page
import time
import pytest


fakePayLoadOrderResponse = {"data":[],"message":"No Orders"}

# here you are mocking your response and filling fakedata
def intercept_response(route):
    route.fulfill(
        json =  fakePayLoadOrderResponse
    )

# Task: is to verify in case where no order is present in the order history
@pytest.mark.smoke
def test_network1(page: Page):
    
    # Step1: Login
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    assert "login" in page.url
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("diwakar12345@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Diwakar@123")
    page.get_by_role("button", name="Login").click()

    # Step2: 
    page.get_by_role("button", name="ORDERS").click()
    message = page.locator(".mt-4").text_content()
    print("Message = ", message)

    time.sleep(5)

    
import playwright
from playwright.sync_api import Page, expect, Playwright
import time
from utils.api_base import APIUtils
# email = diwakar12345@gmail.com
# password = Diwakar@123

# Task: Place an order using api calls
def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Step1: Login
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    assert "login" in page.url
    page.get_by_placeholder("email@example.com").fill("diwakar12345@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Diwakar@123")
    page.get_by_role("button", name="Login").click()
    # time.sleep(2)
    # assert "dashboard" in page.url

    # Step2: Create order --> Get orderId

    api_utils = APIUtils()
    orderId = api_utils.create_order(playwright)
    print("OrderId = ",orderId)

    # Step3: Go to order History page --> Verify order is present or not
    page.get_by_role("button", name="ORDERS").click()
    orderRow = page.locator("tr").filter(has_text=orderId)
    orderRow.get_by_role("button", name="View").click() 
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")

    time.sleep(5)

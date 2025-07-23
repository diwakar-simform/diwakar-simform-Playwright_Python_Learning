# How to bypass login by providing tokens

from playwright.sync_api import Playwright, expect
from utils.api_base import APIUtils
import time


def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    token = api_utils.getToken(playwright)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # script to add here to bypass the login
    page.add_init_script(f"""localStorage.setItem('token','{token}')""") # this is  a javascript injection
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.locator("h1")).to_have_text("Your Orders")
    expect(page.get_by_text("Your Orders")).to_be_visible()
    print("H1 = ",page.locator("h1").text_content())

    time.sleep(5)

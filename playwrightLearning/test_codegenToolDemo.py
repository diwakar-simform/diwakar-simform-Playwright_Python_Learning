import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
    page.locator("div").filter(has_text=re.compile(r"^Brocolli - 1 Kg120–\+ADD TO CART$")).get_by_role("link").nth(1).click()
    page.locator("div").filter(has_text=re.compile(r"^Cauliflower - 1 Kg60–\+ADD TO CART$")).get_by_role("link").nth(1).click()
    page.locator("div").filter(has_text=re.compile(r"^Brocolli - 1 Kg120–\+ADD TO CART$")).get_by_role("button").click()
    page.locator("div").filter(has_text=re.compile(r"^Cauliflower - 1 Kg60–\+ADD TO CART$")).get_by_role("button").click()
    page.locator("div").filter(has_text=re.compile(r"^Cucumber - 1 Kg48–\+ADD TO CART$")).get_by_role("button").click()
    page.locator("div").filter(has_text=re.compile(r"^Tomato - 1 Kg16–\+ADD TO CART$")).get_by_role("link").nth(1).click()
    page.locator("div").filter(has_text=re.compile(r"^Tomato - 1 Kg16–\+ADD TO CART$")).get_by_role("link").nth(1).click()
    page.get_by_role("link", name="Cart").click()
    page.get_by_role("button", name="PROCEED TO CHECKOUT").click()
    page.get_by_role("button", name="Place Order").click()
    page.get_by_role("combobox").select_option("India")
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Proceed").click()
    page.get_by_role("link", name="Home").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


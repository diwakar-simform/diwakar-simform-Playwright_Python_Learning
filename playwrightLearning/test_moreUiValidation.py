from playwright.sync_api import Page, expect
import time

# Hide/Show element, get element by placeholder
def test_moreUiValidations(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_placeholder("Hide/Show Example").fill("Hello World")
    page.get_by_role("button", name="Hide").click() # click on hide button
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(5)

# how to handle popups and alert boxes using playwright and python
def test_handleAlertBox(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dailog: dailog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)

    # another way to handle: If you wanted to see the dialogbox
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
     # Don't auto-accept yet
    page.once("dialog", lambda dialog: (
        print("Dialog message:", dialog.message), # this will print the dialog box message in the terminal
        time.sleep(3),  # Pause so you can see the dialog
        dialog.accept()
    ))
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)

# how to handle iframes using playwright and python
def test_handleFrames(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text(" Happy Subscibers!")
    time.sleep(5)

# how to handle web tables using playwright and python
def test_handleWebTables(page: Page):
    # Task: Check the price of rice equal to 37
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # Step1: Identify the price column
    priceColIndex = -1
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).text_content() == "Price":
            priceColIndex = index
            print("PriceColIndex = ", priceColIndex)
            break
        
    # Step2: Identify the rice row
    riceRow = page.locator("tr").filter(has_text="Rice")
    print("Price of rice =", riceRow.locator("td").nth(priceColIndex).text_content())
    # Step3: Extract the price of the rice.
    priceOfRice = riceRow.locator("td").nth(priceColIndex)
    print("priceOfRice Variable: ", priceOfRice)
    # print("Price of the rice: ",riceRow.nth(priceColIndex).text_content())
    expect(priceOfRice).to_have_text("37")

    time.sleep(5)

# How to handles mouse hover:
def test_handleMouseHover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.pause()
    page.locator("#mousehover").hover()
    page.pause()
    page.get_by_role("link", name="Top").click()
    page.pause()
    time.sleep(5)



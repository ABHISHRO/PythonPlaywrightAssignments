

"""playwright core package is a lightweight browser automation library for controlling browsers
While Playwright test runner package is  a comprehensive testing framework that includes library as well end-to-end test runner """
from playwright.sync_api import Page, expect


"""Create a first test that opens the EventHub login page (/login).
Confirm the page shows the Sign in to EventHub heading, the email field with placeholder you@email.com, and the Sign In button.
"""
def test_launchEventHubloginpage(page: Page):
    page.goto("https://eventhub.rahulshettyacademy.com")
    expect(page.get_by_text("Sign in to EventHub")).to_be_visible()
    expect(page.get_by_role("heading", name="Sign in to EventHub")).to_be_visible()
    expect(page.get_by_placeholder("you@email.com")).to_be_visible()
    expect(page.get_by_role("button", name = "Sign In")).to_be_visible()

"""Add a second login-page smoke check that asserts 
the Password field is visible, 
the URL contains /login, 
and the Sign in to EventHub heading is still visible.
"""

def test_smokeTestLogin(page:Page):
    page.goto("https://eventhub.rahulshettyacademy.com")
    expect(page.locator("#password")).to_be_visible()
    expect(page).to_have_url("https://eventhub.rahulshettyacademy.com/login")
    expect(page.get_by_text("Sign in to EventHub")).to_be_visible()


#Test result screenshot uploaded on Github
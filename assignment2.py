"""Assignment2
Write a smoke test that opens /login using the configured base URL.
Assert the page title matches EventHub, the email field is visible, and the Sign In button is visible.

Note:
1] Page fixture -> Playwright gives  ready to use page in every test.
  It already know the base URL, so page.goto("/login") works.
2] browser context -> a separate session container (like a new incognito window) with its own
  cookies and storage.
3] A fresh context starts with isolated state
"""
from playwright.sync_api import Page, Browser, expect



def test_loginPageWithBaseUrl(page: Page):
    page.goto("/login")   # base URL in conftest.py
    expect(page).to_have_title("EventHub — Discover & Book Events")
    expect(page.get_by_placeholder("you@email.com")).to_be_visible()
    expect(page.get_by_role("button", name="Sign In")).to_be_visible()


"""Use the page fixture to fill the email field and confirm it value is retained.
Create a fresh isolated browser context and page, open the login page with the  URL,
confirm the heading is visible and the email field is empty. Close the context at the end.
"""
def test_pageFixtureVsNewContext(page: Page, browser: Browser):
    # Page fixture
    page.goto("/login")
    page.get_by_placeholder("you@email.com").fill("beginner@sample.com")
    expect(page.get_by_placeholder("you@email.com")).to_have_value("beginner@sample.com")

    # Step 2: New context and page
    context = browser.new_context()
    newPage = context.new_page()
    newPage.goto("https://eventhub.rahulshettyacademy.com/login")
    expect(newPage.get_by_role("heading", name="Sign in to EventHub")).to_be_visible()
    expect(newPage.get_by_placeholder("you@email.com")).to_have_value("")

    # Step 3: close the context
    context.close()


# Cmd to run in headed mode pytest --headed assignment2.py -v
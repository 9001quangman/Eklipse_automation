import pytest
import re
from playwright.sync_api import Page, expect

def test_lg_001_login_with_valid_account(page: Page):
    page.goto("https://eklipse.gg/")
    page.locator("header").get_by_role("link", name="Sign In").click()
    page.wait_for_url(lambda url: "login" in url, timeout=10000)

    page.fill("input#username", "lequangman9002@gmail.com")
    page.fill("input#password", "Abc1234#")
    page.get_by_role("button", name="Sign In").click()

    page.wait_for_url(lambda url: "home" in url, timeout=15000) # Wait for the home page to load since  assert page.url.startswith("https://app.eklipse.gg/home") not working on some versions
  
  
  # Could not catch popup_btn = page.get_by_role("button", name="Skip for now") by using this, so i used try except instead
    try:
        skip_btn = page.locator("button.btn.btn-link--highlight", has_text="Skip for now")
        skip_btn.wait_for(state="visible", timeout=5000)
        skip_btn.click()
    except:
        pass    
    expect(page).to_have_url(re.compile(".*home"))

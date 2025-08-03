import re
import pytest
from playwright.sync_api import Page, expect
from helpers.auth_helpers import login_with_valid_account


def navigate_to_clip_detail_via_notification(page: Page):
    login_with_valid_account(page)
    page.set_viewport_size({"width": 1920, "height": 1080})
    print("[INFO] Logged in and navigated to homepage")

    # Step 1: Click notification bell icon
    notif_icon = page.locator("ul.nav-account.nav-notification .nav-link .ic-bell").first
    expect(notif_icon).to_be_visible()
    notif_icon.click()
    print("[✓] Clicked notification bell")

    # Step 2: Wait for notification dropdown
    dropdown = page.locator("div.dropdown-menu-notification[aria-hidden='false']")
    expect(dropdown).to_be_visible()
    expect(dropdown.locator("div.text-noti", has_text="Notification")).to_be_visible()
    print("[✓] Notification dropdown is visible")

    # Step 3: Click "🎉 Clip Champion 🎉" notification item
    clip_title = dropdown.locator("div.item-title", has_text="🎉 Clip Champion 🎉").first
    clip_title.scroll_into_view_if_needed()
    clip_title.click()
    print("[✓] Clicked 'Clip Champion' notification")

    # Step 4: Wait for redirect to clip detail
    expect(page).to_have_url(re.compile(r".*/video-library/streams/\d+"))
    print(f"[✓] Navigated to clip detail: {page.url}")


def test_ft_002_ai_edit(page: Page):
    navigate_to_clip_detail_via_notification(page)

    # Step 5: Close watermark popup if exists
    try:
        popup = page.locator("div.carousel-caption >> text=Want to have no watermark")
        popup.wait_for(state="visible", timeout=5000)
        page.locator("button.close").click()
        print("[✓] Closed watermark popup")
    except:
        print("[i] No watermark popup appeared")

    # Step 6: Click AI Edit button
    ai_edit_btn = page.locator("button#btn-auto-edit", has_text="AI Edit").first
    expect(ai_edit_btn).to_be_visible()
    print(f"[DEBUG] Current page before AI Edit: {page.url}")
    ai_edit_btn.click()
    print("[✓] Clicked AI Edit button")

    # Step 7: Wait for AI Edit modal popup
    modal = page.locator("div.modal-content", has_text="AI Edit")
    expect(modal).to_be_visible(timeout=10000)
    print("[✓] AI Edit modal appeared")

    # Step 8: Click Start AI Edit inside popup
    start_btn = modal.locator("button.ek-primary-button", has_text="Start AI Edit")
    expect(start_btn).to_be_visible()
    start_btn.click()
    print("[✓] Clicked Start AI Edit")

    # Step 9: Wait for navigation to ai-edit-studio
    for _ in range(10):
        page.wait_for_timeout(1000)
        if re.search(r"/ai-edit-studio", page.url):
            break
    assert re.search(r"/ai-edit-studio", page.url), f"[✗] Expected ai-edit-studio page, but got {page.url}"
    print(f"[✓] Navigated to AI Edit Studio: {page.url}")

    # Optional: short wait to ensure UI fully loads
    page.wait_for_timeout(25000)

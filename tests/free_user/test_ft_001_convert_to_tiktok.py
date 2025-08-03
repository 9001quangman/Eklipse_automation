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


def test_ft_001_convert_to_tiktok(page: Page):
    navigate_to_clip_detail_via_notification(page)

    # Step 5: Close watermark popup if exists
    try:
        popup = page.locator("div.carousel-caption >> text=Want to have no watermark")
        popup.wait_for(state="visible", timeout=5000)
        page.locator("button.close").click()
        print("[✓] Closed watermark popup")
    except:
        print("[i] No watermark popup appeared")

    # Step 6: Click Convert to TikTok / Shorts / Reels button
    tiktok_btn = page.locator("button", has_text="Convert to TikTok / Shorts / Reels").first
    expect(tiktok_btn).to_be_visible()
    tiktok_btn.click()
    print("[✓] Clicked Convert to TikTok / Shorts / Reels")

    # Step 7: Wait for Preview-Only popup to appear
    preview_modal = page.locator("div.modal-content", has_text="Preview-Only Mode Activated!")
    expect(preview_modal).to_be_visible(timeout=10000)
    expect(preview_modal.locator("h3", has_text="Preview-Only Mode Activated!")).to_be_visible()
    print("[✓] Preview-Only popup is visible")

    # Optional: short pause to observe UI (can be removed)
    page.wait_for_timeout(3000)
import re
import pytest
from playwright.sync_api import Page, expect
from helpers.auth_helpers import login_with_valid_account

def test_hm_001_homepage_ui_display(page: Page):
    login_with_valid_account(page)
    page.set_viewport_size({"width": 1920, "height": 1080})
    print("[INFO] Logged in and navigated to homepage")

    # Step 1: Verify Sidebar Menu
    sidebar_menu = page.locator("ul.sidebar-menu")
    sidebar_targets = {
        "Home": "/home",
        "Clip Library": "/video-library/streams",
        "Edits": "/edited-clip/ai-edit",
        "Content Publisher": "/content-planner",
    }

    for label, href in sidebar_targets.items():
        item = sidebar_menu.locator(f"a.sidebar-link[href='{href}']", has_text=label)
        expect(item).to_be_visible()
        print(f"[✓] Sidebar menu '{label}' is visible")

    # Step 2: Verify User Email/Avatar in sidebar
    user_info = page.locator("div.current-name")
    expect(user_info).to_have_text(re.compile("lequangman9002@gmail.com"))
    print(f"[✓] User email 'lequangman9002@gmail.com' is displayed")

    # Step 3: Top Feature Bar
    top_buttons = {
        "Import Streams": "import-stream-item",
        "AI Edit": "ai-edit-item",
        "Convert to Vertical": "convert-tiktok-item",
        "Share": "share-item",
        "Private Stream": "private-stream-item",
    }

    for label, class_name in top_buttons.items():
        btn = page.locator(f"div.{class_name}")
        expect(btn).to_contain_text(label)
        print(f"[✓] Top bar button '{label}' is visible")

    # Step 4: Content bar - Stream List
    stream_list = page.locator("div.ek-clips--box")
    expect(stream_list).to_be_visible()
    print("[✓] Content area (stream list) is visible")

    see_more = stream_list.locator("text=See More")
    expect(see_more).to_be_visible()
    print("[✓] 'See More' item in content bar is visible")

    # Step 5: Right Panel - Premium Games
    expect(page.locator("text=Premium Exclusive Games")).to_be_visible()
    print("[✓] 'Premium Exclusive Games' widget is visible")

    # Step 6: Community Highlights
    expect(page.locator("text=Community Highlights")).to_be_visible()
    print("[✓] 'Community Highlights' section is visible")

    # Step 7: Tutorial Section
    expect(page.locator("text=Tutorial")).to_be_visible()
    print("[✓] 'Tutorial' section is visible")


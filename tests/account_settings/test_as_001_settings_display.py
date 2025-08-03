import re
import pytest
from playwright.sync_api import Page, expect
from helpers.auth_helpers import login_with_valid_account

def test_as_001_settings_display(page: Page):
    login_with_valid_account(page)
    page.set_viewport_size({"width": 1920, "height": 1080})  # Ensure full viewport for testing

    page.locator("i.ic-user").first.click()

    profile_text = page.locator("p.ic-name", has_text="Profile").first
    profile_text.wait_for(state="visible", timeout=5000)

    account_settings_btn = page.locator("button.dropdown-item", has_text="Account Settings").first
    account_settings_btn.wait_for(state="visible", timeout=5000)
    account_settings_btn.click()
    expect(page).to_have_url(re.compile("account"))

    # Step 3: Verify the 3 main tabs in the Account Settings page are visible
    main_tabs = ["Personal Details", "Plugin Setting", "Game Setting"]
    for tab in main_tabs:
        tab_locator = page.locator("ul.account-setting-header li.account-setting-tab", has_text=tab)
        print(f"[debug] Found {tab_locator.count()} elements matching tab: {tab}")
        expect(tab_locator).to_be_visible()
        print(f"[✓] Tab '{tab}' is visible")

    # Step 4: Verify each Connected Account section has icon, name and Connect button
    connected_accounts = {
        "Twitch": "icon-twitch.png",
        "Youtube": "icon-youtube.png",
        "Facebook": "icon-facebook.png",
        "Kick": "icon-kick.png",
        "Rumble": "icon-rumble.png",
    }

    for platform, icon_filename in connected_accounts.items():
        section = page.locator("div.account-detail-container", has_text=platform)
        print(f"[INFO] Verifying Connected Account section: {platform}")

        # Icon
        icon_locator = section.locator(f"img[src*='{icon_filename}']")
        expect(icon_locator).to_be_visible()
        print(f"[✓] Icon for {platform} is visible")

        # Name
        name_locator = section.locator("p", has_text=platform)
        expect(name_locator).to_be_visible()
        print(f"[✓] Name for {platform} is visible")

        # Connect Button
        connect_btn = section.locator("button.ek-primary-button", has_text="Connect")
        expect(connect_btn).to_be_visible()
        print(f"[✓] Connect button for {platform} is visible")
        
    # Step5: Verify Social Profile
    social_profiles = {
        "Tiktok": ("icon-tiktok.png", "Connect"),
        "Discord Settings": ("icon-discord.png", None), # No button for Discord Settings
        "Discord Account": ("icon-discord-account.png", "Connect"),
        "Eklipse Bot": ("icon-discord-bot.png", "Add to Server"),
    }
    
    for platform, (icon_filename, button_text) in social_profiles.items():
        section = page.locator("div.account-detail-container", has_text=platform)
        print(f"[INFO] Verifying Social Profile section: {platform}")
        section.scroll_into_view_if_needed()

        ## Icon
        icon_locator = section.locator(f"img[src*='{icon_filename}']")
        expect(icon_locator).to_be_visible()
        print(f"[✓] Icon for {platform} is visible")
        
        # Name
        name_locator = section.locator("p", has_text=platform)
        expect(name_locator).to_be_visible()
        print(f"[✓] Name for {platform} is visible")
        
        # Button visibility check
        if button_text:
            button_locator = section.locator("button.ek-primary-button", has_text=button_text)
            expect(button_locator).to_be_visible()
            print(f"[✓] Button '{button_text}' for {platform} is visible")
        else:
            print(f"[i] Skipped button check for {platform} (no button expected)")
            
        # Step 6: Scroll to bottom of the page to reveal all settings
        page.locator("text=Delete Account").scroll_into_view_if_needed()
        print("[INFO] Scrolled to bottom to verify Community/Profile/Password/Account Removal sections")
        
        # Community Settings
        expect(page.locator("p", has_text="Community Settings")).to_be_visible()
        expect(page.locator("text=Share clips to Community Highlights")).to_be_visible()
        toggle = page.locator("div.community-clip-setting input[type='checkbox']")
        assert toggle.count() > 0
        assert toggle.is_checked(), "[✗] Toggle should be ON (checked)"
        print("[✓] Community Settings text and toggle are visible and checked")
        
        # Profile Settings
        profile_section = page.locator("div.ek-personal-detail")
        expect(profile_section.locator("p", has_text="Profile settings")).to_be_visible()
        # Name and Email fields
        expect(profile_section.locator("label[for='Name']")).to_be_visible()
        expect(profile_section.locator("input[name='Name']")).to_be_visible()
        expect(profile_section.locator("label[for='Email']")).to_be_visible()
        expect(profile_section.locator("input[name='Email']")).to_be_visible()
        expect(profile_section.locator("button.ek-primary-button", has_text="Save Changes")).to_be_visible()
        print("[✓] Profile Settings fields and button are visible")
        
        # Password section
        expect(page.locator("p", has_text="Password")).to_be_visible()
        expect(page.locator("button", has_text="Change Password")).to_be_visible()
        print("[✓] Password section and Change button are visible")
        
        #Account Removal
        expect(page.locator("p", has_text="Account Removal")).to_be_visible()
        expect(page.locator("text=Delete your account means")).to_be_visible()
        expect(page.locator("button", has_text="Delete Account")).to_be_visible()
        print("[✓] Account Removal text and Delete button are visible")
        

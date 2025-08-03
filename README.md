# Eklipse Automation Testing Suite

This repository contains **Playwright-based UI automation tests** for key user flows on [https://eklipse.gg](https://eklipse.gg), focusing on both guest and logged-in user interactions.

## 📂 Project Structure

```
Eklipse_automation/
├── tests/
│   ├── account_settings/
│   │   └── test_as_001_settings_display.py
│   ├── free_user/
│   │   ├── test_ft_001_convert_to_tiktok.py
│   │   └── test_ft_002_ai_edit.py
│   ├── home/
│   │   └── test_hm_001_homepage.py
│   ├── landing/
│   │   └── test_lp_001_banner.py
│   ├── register_login/
│   │   └── test_lg_001_login_with_valid_account.py
├── helpers/
│   └── auth_helpers.py
```

## 🧪 Test Cases Overview

### 🔓 Landing Page

* `test_lp_001_banner.py`

  * Verifies main banner text, subheadline, CTA buttons, and promotional video on the homepage.

### 🔐 Login

* `test_lg_001_login_with_valid_account.py`

  * Simulates login with a valid account, handles optional "Skip for now" popup, and ensures navigation to the dashboard.

### 🏠 Home Page

* `test_hm_001_homepage_ui_display.py`

  * Validates the visibility and structure of sidebar, top navigation, user info, content streams, widgets, and tutorials.

### 👤 Account Settings

* `test_as_001_settings_display.py`

  * Navigates to account settings.
  * Verifies the presence of profile/game/plugin tabs.
  * Checks the availability of connected accounts, social profiles, and profile settings.

### 🆓 Free User Features

#### Convert to TikTok / Shorts / Reels

* `test_ft_001_convert_to_tiktok.py`

  * Opens a stream via notification.
  * Closes watermark popup if present.
  * Clicks the Convert to TikTok button.
  * Verifies the preview-only modal appears.

#### AI Edit Flow

* `test_ft_002_ai_edit.py`

  * Opens a stream via notification.
  * Closes watermark popup if present.
  * Clicks AI Edit and confirms AI Edit modal appears.
  * Starts AI Edit and waits for navigation to `ai-edit-studio`.

## 🚀 Running the Tests

### ✅ Prerequisites

* Python 3.10+
* Dependencies: `playwright`, `pytest`

```bash
pip install -r requirements.txt
playwright install
```

### ▶ Run All Tests

```bash
pytest tests/
```

### ▶ Run Specific Test File

```bash
pytest tests/home/test_hm_001_homepage.py
```

## ⚙️ Notes

* Login credentials and reusable login logic are defined in `helpers/auth_helpers.py`.
* Tests use `expect` assertions and visibility checks.
* Viewport is set to 1920x1080 to ensure full-page rendering.

---

Maintained by [lequangman9002](https://github.com/9001quangman)

import pytest
from playwright.sync_api import Page, expect

def test_lp_001_banner(page: Page):
    page.goto("https://eklipse.gg/")
    
    expect(page.locator("text=Capture Your Best Moments")). to_be_visible()
    
    # Check the subheadline
    expect(page.locator("text=10x Faster with AI!")).to_be_visible()
    
    # Check the CTA button by text content
    expect(page.locator("text=Start for Free")).to_be_visible()
    expect(page.locator("text=Learn Premium")).to_be_visible()
    
    # Check media preview element exists
    video = page.locator("video.elementor-video")
    assert video.count() >0
    assert video.get_attribute("src") == "https://eklipse.gg/wp-content/uploads/2025/01/LP_Marvel.mp4"

    

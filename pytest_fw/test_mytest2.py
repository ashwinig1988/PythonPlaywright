from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.tamm.abudhabi/")
    page.get_by_role("link", name="icon Housing & Properties Houses, Lands and Real Estate").click()
    page.get_by_role("link", name="Request a Residential Land Grant").click()
    page.get_by_role("button", name="button-primary").click()
    page.get_by_role("link", name="UAEPass Button").click()

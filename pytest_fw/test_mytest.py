from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/python/")
    page.get_by_role("link", name="Docs").click()
    page.get_by_role("link", name="Installation").click()
    page.get_by_role("listitem").filter(has_text="Getting StartedInstallationWriting testsRunning testsTest generatorTrace viewerP").get_by_role("link", name="Test generator").click()

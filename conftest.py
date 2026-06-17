import pytest

from playwright.sync_api import sync_playwright

from utils.config_reader import ConfigReader


@pytest.fixture(scope="session")
def browser():

    config = ConfigReader.read()

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=config["headless"]
        )

        yield browser

        browser.close()


@pytest.fixture
def page(browser):

    page = browser.new_page()

    page.set_default_timeout(60000)

    yield page

    page.close()

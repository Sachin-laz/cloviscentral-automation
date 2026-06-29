from pages.login_page import LoginPage
from pages.systems_page import SystemsPage
from utils.config_reader import ConfigReader


def test_verify_system_tab_navigation(page):

    config = ConfigReader.read()

    page.goto(config["url"])

    login = LoginPage(page)

    login.login(
        config["username"],
        config["password"]
    )

    systems = SystemsPage(page)

    assert systems.open_systems(), \
        "Failed to open Systems page."

    assert systems.click_active_tab(), \
        "Failed to switch to Active tab."

    assert systems.click_inactive_tab(), \
        "Failed to switch to Inactive tab."

    assert systems.click_pending_tab(), \
        "Failed to switch back to Pending tab."
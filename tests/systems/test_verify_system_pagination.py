from pages.login_page import LoginPage
from pages.systems_page import SystemsPage
from utils.config_reader import ConfigReader


def test_verify_system_pagination(page):

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

    # Verify Rows Per Page
    assert systems.change_rows_per_page("10"), \
        "Failed to change Rows Per Page."

    assert systems.verify_rows_per_page("10"), \
        "Rows Per Page was not updated."
    
    assert systems.wait_for_pagination_load()
    
     # Store default pagination
    default_pagination = systems.get_pagination_text()

    print("Default  :", default_pagination)

    # Verify Next Page
    assert systems.click_next_page(), \
        "Failed to navigate to the next page."

    next_page_pagination = systems.get_pagination_text()

    print("Next     :", next_page_pagination)

    assert next_page_pagination != default_pagination, \
        "Pagination did not change after clicking Next."

    # Verify Previous Page
    assert systems.click_previous_page(), \
        "Failed to navigate to the previous page."

    previous_page_pagination = systems.get_pagination_text()

    print("Previous :", previous_page_pagination)

    assert previous_page_pagination == default_pagination, \
        "Failed to navigate back to the first page."

    
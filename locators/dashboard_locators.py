class DashboardLocators:
    
    DASHBOARD_MENU = "#side-menu-dashboard"
    
    PROFILE_ICON = "#header-my-account-icon-btn"

    LOGOUT_BUTTON = "span:has-text('Logout')"

    LOGIN_PAGE = "button[type='submit']"

    CONFIRM_LOGOUT = "text='Yes'"

    CUSTOMERS_CARD = "span:text-is('Total Customers')"

    CLIENT_COUNT = "//span[text()='Total Customers']/ancestor::div[contains(@class,'MuiCardContent-root')]//div[contains(@class,'MuiTypography-h5')]"
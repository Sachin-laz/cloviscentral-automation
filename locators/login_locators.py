class LoginLocators:

    USERNAME = "[name='email']"

    PASSWORD = "[name='password']"

    LOGIN_BUTTON = "button[type='submit']"

    DASHBOARD_HEADER = "h4:has-text('Dashboard')"

    ERROR_MESSAGE = "//p[text()='Invalid Email or password']"

    USERNAME_REQUIRED = "#login-email-helper-text"

    PASSWORD_REQUIRED = "#login-password-helper-text"

    FORGOT_PASSWORD = "#forgot-password-btn"

    FORGOT_PASSWORD_HEADING = "h5:has-text('Forgot Password?')"

    PASSWORD_TOGGLE = "#login-show-password-btn"

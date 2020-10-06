from selenium.webdriver.common.by import By


class LoginLocator:

    # LoginPage Objects
    username_textbox = (By.ID, "txtUsername")
    password_textbox = (By.ID, "txtPassword")
    login_button = (By.ID, "btnLogin")
    invalid_username_messageText = (By.CSS_SELECTOR, "span#spanMessage")

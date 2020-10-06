from selenium.webdriver.common.by import By


class DashboardLocator:

    # DashboardPage Objects
    welcome_link = (By.ID, "welcome")
    logout_link = (By.LINK_TEXT, "Logout")

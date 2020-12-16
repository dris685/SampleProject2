from Testcase.BaseTest import BaseTest
from Page.LoginPage import LoginPage
from Page.DashboardPage import DashboardPage
import pytest
import allure
import time


class LoginTest(BaseTest):
    @allure.description("Validates OrangeHRM with valid login credentials")
    @allure.severity(severity_level="CRITICAL")
    def test_validLogin(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_valid_username()
        self.loginPage.enter_valid_password()
        self.loginPage.click_login_button()
        self.dashboardPage = DashboardPage(self.driver)
        assert self.dashboardPage.is_dashboard_url_valid()

    @allure.description("Validates OrangeHRM with invalid login credentials")
    @allure.severity(severity_level="NORMAL")
    def test_invalidLogin(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_invalid_username()
        self.loginPage.enter_invalid_password()
        self.loginPage.click_login_button()
        self.dashboardPage = DashboardPage(self.driver)
        try:
            assert self.dashboardPage.is_dashboard_url_valid()
        finally:
            if AssertionError:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name="Invalid Credentials",
                              attachment_type=allure.attachment_type.PNG)

    # @allure.description("Validates OrangeHRM with valid login credentials")
    # @allure.severity(severity_level="CRITICAL")
    # @pytest.mark.parametrize("username, password", [("admin", "admin123")])
    # def test_validLogin_para(self, username, password):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.enter_valid_username()
    #     self.loginPage.enter_valid_password()
    #     self.loginPage.click_login_button()
    #     self.dashboardPage = DashboardPage(self.driver)
    #     assert self.dashboardPage.is_dashboard_url_valid()
    #
    # @allure.description("Validates OrangeHRM with invalid login credentials")
    # @allure.severity(severity_level="NORMAL")
    # @pytest.mark.parametrize("username, password", [("Admin", "Admin123")])
    # def test_invalidLogin_para(self, username, password):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.enter_invalid_username()
    #     self.loginPage.enter_invalid_password()
    #     self.loginPage.click_login_button()
    #     self.dashboardPage = DashboardPage(self.driver)
    #     try:
    #         assert self.dashboardPage.is_dashboard_url_valid()
    #     finally:
    #         if AssertionError:
    #             allure.attach(self.driver.get_screenshot_as_png(),
    #                           name="Invalid Credentials",
    #                           attachment_type=allure.attachment_type.PNG)

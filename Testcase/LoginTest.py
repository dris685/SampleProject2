import unittest
from Page.LoginPage import LoginPage
from Page.DashboardPage import DashboardPage
from Driver.DriverWrapper import DriverWrapper


class LoginTest(unittest.TestCase):

    def test_login_valid(self):
        DriverWrapper.setUp()
        loginPage = LoginPage()
        loginPage.enter_valid_username()
        loginPage.enter_valid_password()
        loginPage.click_login_button()
        dashboardPage = DashboardPage()
        dashboardPage.click_welcome_link()
        dashboardPage.click_logout_link()
        DriverWrapper.tearDown()

    # @unittest.skip("skip testing")
    def test_login_invalid_username(self):
        DriverWrapper.setUp()
        loginPage = LoginPage()
        loginPage.enter_invalid_username()
        loginPage.enter_valid_password()
        loginPage.click_login_button()
        expected_message = "Invalid credentials"
        actual_message = loginPage.get_invalid_username_messageText()
        self.assertEqual(expected_message, actual_message)
        DriverWrapper.tearDown()




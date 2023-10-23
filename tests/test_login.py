import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

login_page: LoginPage


class Login_Test(unittest.TestCase):

    def setUp(self):
        global login_page
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)

    def test_valid_login(self):
        # Login with valid credentials
        login_page.login("standard_user", "secret_sauce")
        # Verify successful login by checking for the presence of the product list
        product_list = self.driver.find_element(By.CLASS_NAME, "inventory_list")
        self.assertTrue(product_list.is_displayed())

    def test_invalid_username(self):
        # Attempt to log in with invalid credentials
        login_page.login("invalid_username", "secret_sauce")
        # Verify that an error message is displayed
        self.assertTrue(login_page.is_error_message_displayed())

    def test_invalid_password(self):
        # Attempt to log in with invalid credentials
        login_page.login("visual_user", "invalid_password")
        # Verify that an error message is displayed
        self.assertEqual("Epic sadface: Username and password do not match any user in this service", login_page.get_error_message_text())

    def test_blank_login(self):
        # Attempt to log in without input
        login_page.click_login()
        # Verify that an error message is displayed
        self.assertTrue(login_page.is_error_message_displayed())

    def tearDown(self):
        # Close browser
        self.driver.quit()
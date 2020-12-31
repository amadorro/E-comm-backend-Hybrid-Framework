# Goal: Test login and logout properly
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time
import pytest

class Test_01_LoginPage:
    # class variables
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_loginPage(self, setup):
        self.logger.info("**** Test_01_LoginPage Started *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # create a new variable to connect to pageObjects
        self.lp = LoginPage(self.driver)
        self.logger.info("**** Login Page Test Started *****")
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)

        self.lp.clickLogin()
        self.logger.info("**** Login Page Test Completed *****")
        time.sleep(5)

        # validate
        act_title = self.driver.title
        time.sleep(5)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**** Title Page Matched **** ")
        else:
            self.logger.error("**** Title Page Matched Failed **** ")
            self.driver.save_screenshot("./Screenshots/" + "Test_01_LoginPage.png")
            assert False

        # click logout
        time.sleep(5)
        self.lp.clickLogout()
        self.logger.info("***** Logout Test Completed *****")
        self.logger.info("***** Test_01_LoginPage Completed *****")







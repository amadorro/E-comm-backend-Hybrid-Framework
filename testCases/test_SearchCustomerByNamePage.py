
from pageObjects.SearchCustomerByEmailPage import SearchCustomers
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time
import pytest

class Test_03_SearchName:
    # class variables
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_OrderTotals(self, setup):
        self.logger.info("***** Test_03_SearchName Test Started *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # create a new variable to login
        self.logger.info("***** Login Test Started *****")
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login test Completed ****")


        # create a new variable to access the search-customer page
        self.sc = SearchCustomers(self.driver)
        self.sc.setSelectCustomers()
        self.sc.setSelectCustomersItem()

        # validate search name
        self.logger.info("***** Search Name Test Started ****")
        time.sleep(5)
        sc = SearchCustomers(self.driver)
        sc.setFname("John")
        sc.setLname("Smith")
        sc.clickSearch()
        time.sleep(5)
        status = sc.searchCustomerByName("John Smith")
        self.driver.close()
        assert True == status
        self.logger.info("***** Search Name Test Completed ****")
        self.logger.info("***** Test_03_SearchName Test Completed *****")











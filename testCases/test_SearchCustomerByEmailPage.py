from pageObjects.SearchCustomerByEmailPage import SearchCustomers
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time
import pytest

class Test_02_SearchEmail:
    # class variables
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_OrderTotals(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # create a new variable to login
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # create a new variable to access the search-customer page
        self.sc = SearchCustomers(self.driver)
        self.sc.setSelectCustomers()
        self.sc.setSelectCustomersItem()

        # validate search email
        sc = SearchCustomers(self.driver)
        sc.setEmail("victoria_victoria@nopCommerce.com")
        sc.clickSearch()
        time.sleep(5)
        status = sc.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True == status











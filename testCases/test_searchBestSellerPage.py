from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchBestSellerPage import SeachBestSeller
import time
import pytest

class Test_04_SearchBestSeller:
    # class variables
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_BestSeller(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # create a new variable to login
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # create a new variable to select reports
        self.sbs = SeachBestSeller(self.driver)
        time.sleep(5)
        self.sbs.clickReports()
        time.sleep(5)
        self.sbs.clickBestsellers()
        time.sleep(5)
        self.sbs.clickRunReport()
        self.sbs.searchBestsellerByFirstRow("Vintage Style Engagement Ring")




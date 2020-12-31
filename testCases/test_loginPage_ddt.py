
# Goal: Test login and logout properly
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time
import pytest

class Test_05_LoginPage:
    # class variables
    baseURL = ReadConfig.getApplicationURL()
    path = './TestData/Data.xlsx'
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginPage(self, setup):
        self.logger.info("**** Test_01_LoginPage Started *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # create a new variable to connect to pageObjects
        self.lp = LoginPage(self.driver)

        # create a variable for row count
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows:', self.rows)
        # empty list for exp values
        lst_status = []

        for r in range(2, self.rows + 1):
            # create new variables from XLUtils
            self.user = XLUtils.readData(self.path, 'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1',r,3)

            # use the above variable on the LoginPage
            self.lp.setEmail(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            # test both: title and exp values. Append the results to empty list
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == 'pass':
                    self.lp.clickLogout();
                    lst_status.append('pass')
                elif self.exp == 'fail':
                    self.lp.clickLogout();
                    lst_status.append('fail')

            elif act_title != exp_title:
                if self.exp == 'pass':
                    lst_status.append('fail')
                elif self.exp == 'fail':
                    lst_status.append('pass')
            print(lst_status)

        if 'fail' not in lst_status:
            self.driver.close()
            assert True
        else:
            self.close()
            assert False


                    













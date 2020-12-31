# Goal: Search for the bestseller which is located at the first row of the table

class SeachBestSeller:
    # locators
    click_reports_xpath = "//span[normalize-space()='Reports']"
    click_bestsellers_xpath = "//span[normalize-space()='Bestsellers']"
    click_RunReport_xpath = "//button[normalize-space()='Run report']"
    # Bestseller table locators:
    # note: find the xpath of first tr(rows) and td(columns)
    # remove the last part [1] so that applies to all the rows and columns
    BS_table_xpath = "//*[@id='salesreport-grid']"
    rows_tr_xpath = "//*[@id='salesreport-grid']/tbody/tr"
    columns_td_xpath = "//*[@id='salesreport-grid']/tbody/tr[1]/td"

    def __init__(self, driver):
        self.driver = driver

    def clickReports(self):
        self.driver.find_element_by_xpath(self.click_reports_xpath).click()

    def clickBestsellers(self):
        self.driver.find_element_by_xpath(self.click_bestsellers_xpath).click()

    def clickRunReport(self):
        self.driver.find_element_by_xpath(self.click_RunReport_xpath).click()

    # count number of rows in a table
    def setTableRows(self):
        return len(self.driver.find_elements_by_xpath(self.rows_tr_xpath))

    # verify: 'Vintage Style Engagement Ring' is on the first row of the table(Bestseller)
    def searchBestsellerByFirstRow(self, Name):
        flag = False
        for r in range(1, self.setTableRows() + 1):
            # create a variable for the table
            table = self.driver.find_element_by_xpath(self.BS_table_xpath)
            # using the table variable, find the first row and first column
            Name_id = table.find_element_by_xpath("//*[@id='salesreport-grid']/tbody/tr['+str(r)+']/td[1]").text
            if Name_id == Name:
                flag = True
                break
        return flag











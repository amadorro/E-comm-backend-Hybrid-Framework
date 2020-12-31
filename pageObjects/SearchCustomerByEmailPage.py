# Goal: Search customer by email and name

class SearchCustomers:
    # locators
    Customers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    CustomersItem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    email_txtbox_id = "SearchEmail"
    fname_txtbox_id = "SearchFirstName"
    lname_txtbox_id = "SearchLastName"
    search_button_id = "search-customers"

    # table locators
    # xpath can be created by searching table //table
    tableSearch_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id = 'customers-grid']"
    # note: remove the last part so it applies to all the rows/trs
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    # note: remove the last part so it applies to all the columns/tds
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self, driver):
        self.driver = driver

    def setSelectCustomers(self):
        self.driver.find_element_by_xpath(self.Customers_menu_xpath).click()

    def setSelectCustomersItem(self):
        self.driver.find_element_by_xpath(self.CustomersItem_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.email_txtbox_id).clear()
        self.driver.find_element_by_id(self.email_txtbox_id).send_keys(email)

    def setFname(self, name):
        self.driver.find_element_by_id(self.fname_txtbox_id).clear()
        self.driver.find_element_by_id(self.fname_txtbox_id).send_keys(name)

    def setLname(self, lname):
        self.driver.find_element_by_id(self.lname_txtbox_id).clear()
        self.driver.find_element_by_id(self.lname_txtbox_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.search_button_id).click()

    def getNoRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoColms(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    # This is a true or false method
    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoRows() + 1):
            # create a new variable for the table_xpath
            table = self.driver.find_element_by_xpath(self.table_xpath)
            # using table variable find the email in text form for column 2
            # note: add ['+str(r)+'] next to tr to read it as string
            email_id = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr['+str(r)+']/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    # This is a true or false method
    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoRows() + 1):
            # create a new variable for the table
            table = self.driver.find_element_by_xpath(self.table_xpath)
            # using the table variable find the name in the text form for column 3
            name_id = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr['+str(r)+']/td[3]").text
            if name_id == name:
                flag = True
                break
        return flag







from selenium.webdriver.common.by import By

class LoginPage:
    # locators
    email_textbox_id = "Email"
    password_textbox_id = "Password"
    click_login_xpath = "//input[@class='button-1 login-button']"
    click_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.click_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.click_logout_linktext).click()

'''Fixtures are functions, which will run
before each test function to which it
is applied'''
# Run the test on the desire browser

from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Users/Amador/Desktop/chromedriver_win32/chromedriver.exe")
        print("Launching Chrome")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/Amador/Desktop/geckodriver-v0.27.0-win64/geckodriver.exe")
        print("Launching Firefox")
    # default browser
    else:
        driver = webdriver.Ie(executable_path="C:/Users/Amador/Desktop/IEDriverServer_x64_3.150.1/IEDriverServer.exe")
    return driver

# This will get the value from command-line/hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

# This will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Generate html report
# Add this:
def pytest_configure(config):
    config._metadata['Project Name'] = "NopCommerce"
    config._metadata['Module Name'] = "Backend Testing"
    config._metadata['Tester'] = "Amador Rodriguez"

# This is for delete/modify environment info to HTML Report
# Remove this:
@pytest.mark.optionalhook
def pytest_medatada(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
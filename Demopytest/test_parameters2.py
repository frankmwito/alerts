import pytest
from selenium.webdriver.common.by import By
      
@pytest.mark.usefixtures("initialize_driver")
class BassClass:
    pass

class Test_Driver(BassClass):
    def test_multiple_Browsers(self):
        self.driver.get("https://www.lambdatest.com/selenium-playground/")
        header = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Selenium Playground']").text
        print("Header: ", header)
        assert header == "Selenium Playground"
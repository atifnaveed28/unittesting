import time  # for time wait
import unittest  # Unit testing framework
from selenium import webdriver  # call webdriver
from selenium.webdriver.common.by import By   # Get Xpath


class LoginWithSelenium(unittest.TestCase):  # Class Name

    def setUp(self):
        # Set up the WebDriver (use appropriate driver for your browser)
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

    def test_login_page(self):
        # Navigate to the example website
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(15)  # wait to get webpage load properly
        time.sleep(5)  # wait 5 seconds after any event i-e login button clicked

        # username
        self.driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
        # Password
        self.driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
        # Login Btn
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(5)

        # Assert that the search results page title contains "Selenium in Python"
        # self.assertIn("Dashboard", self.driver.title)
        self.assertIn("Dashboard", self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6').text)


if __name__ == '__main__':
    unittest.main()

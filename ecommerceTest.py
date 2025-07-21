import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import helpers as hp


class EcomerceTest(unittest.TestCase):

    def setUp(self):

        chrome_options = ChromeOptions()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

    def test_001(self):

        driver = self.driver
        driver.get(hp.ecommerce)
        hp.scroll_down(driver, By.XPATH, hp.mensCoat_buy, 2, 10)
        hp.click_on_elem(driver, By.XPATH, hp.mensCoat_buy, 10)
        hp.delay()
        hp.check_url(driver, "http://localhost:3000/product/3", 10)
        hp.click_on_elem(driver, By.XPATH, hp.addToCart,10)
        hp.click_on_elem(driver, By.XPATH, hp.goToCart,10)
        hp.check_url(driver, hp.cart_url,10)
        try:
            # Try to find the element
            element = driver.find_element(By.XPATH, "//strong[normalize-space()='Mens Cotton Jacket']")
            # If found, assert True
            self.assertTrue(element.is_displayed(), "Element was found but is not visible")
            print("The item as added to cart")
        except NoSuchElementException:
            # If not found, fail the test
            self.fail("Element not found on the page")





    def tearDown(self):
        """Cleanup after each test"""
        self.driver.quit()





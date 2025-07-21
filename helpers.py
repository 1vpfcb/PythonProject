import time
import random
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#locators
ecommerce = "http://localhost:3000"
mensCoat_buy = "//div[@id='3']//a[@class='btn btn-dark m-1'][normalize-space()='Buy Now']"
goToCart = "//a[@class='btn btn-dark mx-3']"
addToCart = "//button[@class='btn btn-outline-dark']"
cart_url = "http://localhost:3000/cart"



# functions

def click_on_elem(driver, by, value, timeout):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, value)),
                f"Element '{value}' not clickable within {timeout} seconds"
            )
            driver.execute_script("""
                        arguments[0].scrollIntoView({
                            behavior: 'smooth',
                            block: 'center'
                        });
                    """, element)

            element.click()

            print(f"Clicked on element: {value}")
            return True

        except TimeoutException:
            print(f"Timeout waiting for element to be clickable: {value}")
            return False

        except Exception as e:
            print(f"Error clicking element '{value}': {e}")
            return False



def delay():
    time.sleep(random.randint(2, 4))




def scroll_down(driver, by, value, pause_duration=2, timeout=10):
    try:
        # wait for the element to be present in the DOM
        target_element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        driver.execute_script("""
                   arguments[0].scrollIntoView({
                       behavior: 'smooth',
                       block: 'center'
                   });
               """, target_element)

        #scroll the element into view using JavaScript
        #driver.execute_script("arguments[0].scrollIntoView(true);", target_element)

        #pause to simulate scrolling completion or data entry
        time.sleep(pause_duration)

        #optionally, return the element for further interaction
        return target_element

    except Exception as e:
        print(f"An error occurred while scrolling to the element: {e}")
        raise


def check_url(driver, expected_url, timeout):
    try:
        WebDriverWait(driver,timeout).until(
            EC.url_to_be(expected_url)
        )
        print(f"URL matched: {driver.current_url}")
    except Exception:
        actual_url = driver.current_url
        raise AssertionError(f"URL mismatch! Expected: {expected_url}, Actual: {actual_url}")















import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_star_ratings(self, star_values):
        try:
            time.sleep(2)

            for star_value in star_values:
                selectors = [
                    f"//div[@data-filters-item='class:class={star_value}']",
                    f"//div[contains(text(), '{star_value} stars')]",
                    f"//div[@aria-label='{star_value} stars']",
                    f"//div[contains(@class, 'eaa3cb80f6')]//div[contains(text(), '{star_value}')]",
                ]

                for selector in selectors:
                    try:
                        star_element = self.driver.find_element(By.XPATH, selector)
                        star_element.click()
                        break
                    except:
                        continue

        except Exception as e:
            print(f"Error selecting stars: {e}")
            return False

        return True

    def sorting_by_price(self):
        time.sleep(1)
        sorting_prices = self.driver.find_element(
            By.XPATH,
            '//*[@id="bodyconstraint-inner"]/div/div/div[2]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div/span/button/span',
        )
        
        sorting_prices.click()

        low_to_high = self.driver.find_element(
            By.XPATH,
            "//span[normalize-space()='Property rating (low to high)']",
        )
        low_to_high.click()
        

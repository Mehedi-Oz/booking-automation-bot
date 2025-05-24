import time
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport


class Booking(webdriver.Chrome):
    def __init__(self):
        super(Booking, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency):
        currency_element = self.find_element(
            By.XPATH,
            '//*[@id="b2indexPage"]/div[2]/div/div/header/div/nav[1]/div[2]/span[1]/button',
        )
        currency_element.click()

        selected_currency = self.find_element(
            By.XPATH, f'//div[normalize-space()="{currency}"]'
        )
        selected_currency.click()

    def select_place_to_go(self, place_to_go=None):
        search_field = self.find_element(By.XPATH, '//*[@id=":rh:"]')
        search_field.clear()
        search_field.send_keys(place_to_go)
        search_field.click()
        time.sleep(1)

        first_result = self.find_element(By.XPATH, '//*[@id="autocomplete-result-1"]')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.XPATH, f'//span[@data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.XPATH, f'//span[@data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_adults(self, count):
        selection_element = self.find_element(
            By.XPATH, ' //*[@id="indexsearch"]/div[2]/div/form/div/div[3]/div/button'
        )
        selection_element.click()
        time.sleep(0.5)

        while True:

            decrease = self.find_element(
                By.XPATH, '//*[@id=":ri:"]/div/div[1]/div[2]/button[1]'
            )
            decrease.click()

            current_adults_element = self.find_element(By.ID, "group_adults")
            current_adults_value = int(current_adults_element.get_attribute("value"))

            if current_adults_value == 1:
                break

        time.sleep(0.5)

        increase_adults = self.find_element(
            By.XPATH, '//*[@id=":ri:"]/div/div[1]/div[2]/button[2]'
        )

        try:
            increase_adults = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id=":ri:"]/div/div[1]/div[2]/button[2]')
                )
            )

            for i in range(count - 1):
                increase_adults.click()

        except Exception as e:
            print(f"Error selecting adults: {e}")

        finally:
            done_button = self.find_element(
                By.XPATH, "//span[normalize-space()='Done']"
            )
            done_button.click()

    def search_hotels(self):
        search_button = self.find_element(
            By.XPATH, "//span[normalize-space()='Search']"
        )
        search_button.click()

        try:
            button = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[@aria-label='Close map']",
                    )
                )
            )
            button.click()
        except NoSuchElementException:
            pass

    def apply_filters(self):
        filtration = BookingFiltration(driver=self)
        filtration.select_star_ratings([4, 5])
        filtration.sorting_by_price()

    def report_results(self):
        time.sleep(3) 
        hotel_boxes = self.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="property-card"]'
        )

        report = BookingReport(hotel_boxes)
        report.pull_titles()

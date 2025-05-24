from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import List
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from prettytable import PrettyTable

class BookingReport:
    def __init__(self, boxes_section_element: List[WebElement]):
        self.boxes_section_element = boxes_section_element

    def pull_titles(self):
        try:
            button = WebDriverWait(self, 5).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[@aria-label='Close map']",
                    )
                )
            )
            button.click()
        except:
            pass

        hotels = []

        for deal_box in self.boxes_section_element:
            try:
                name = deal_box.find_element(
                    By.XPATH, ".//div[@data-testid='title']"
                ).text.strip()

                try:
                    price = deal_box.find_element(
                        By.CSS_SELECTOR,
                        "span[data-testid='price-and-discounted-price']",
                    ).text.strip()
                except:
                    price = "Price not available"

                score = deal_box.find_element(
                    By.CSS_SELECTOR,
                    "div[data-testid='review-score'] .f63b14ab7a.dff2e52086",
                ).text.strip()

                if name:
                    hotels.append({"name": name, "price": price, "score": score})

            except Exception as e:
                continue

        table = PrettyTable()
        table.field_names = ["No.", "Hotel Name", "Price", "Score"]
        table.align["Hotel Name"] = "l"
        table.align["Price"] = "r"
        table.align["Score"] = "c"
        
        for index, hotel in enumerate(hotels, 1):
            table.add_row([
                index,
                hotel['name'],
                hotel['price'],
                hotel['score']
            ])

        print("\n=== Found Hotels ===")
        print(f"Total hotels found: {len(hotels)}\n")
        print(table)

        return hotels

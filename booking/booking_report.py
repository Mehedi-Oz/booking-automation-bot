from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import List
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookingReport:
    def __init__(self, boxes_section_element: List[WebElement]):
        self.boxes_section_element = boxes_section_element

    def pull_titles(self):
        try:
            # Close the map if it's open
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
                # Get the hotel name
                name = deal_box.find_element(
                    By.XPATH, ".//div[@data-testid='title']"
                ).text.strip()

                # Get the hotel price
                try:
                    price = deal_box.find_element(
                        By.CSS_SELECTOR,
                        "span[data-testid='price-and-discounted-price']",
                    ).text.strip()
                except:
                    price = "Price not available"

                # Get the hotel score
                try:
                    score = deal_box.find_element(
                        By.CSS_SELECTOR, "div[data-testid='review-score']"
                    ).text.strip()
                except:
                    score = "Score not available"

                # Get the review summary (e.g., "Good")
                try:
                    review_summary = deal_box.find_element(
                        By.CSS_SELECTOR, "span[data-testid='review-score-label']"
                    ).text.strip()
                except:
                    review_summary = "Review summary not available"

                # Get the number of reviews (e.g., "3,154 reviews")
                try:
                    num_reviews = deal_box.find_element(
                        By.CSS_SELECTOR, "span[data-testid='review-score-reviews']"
                    ).text.strip()
                except:
                    num_reviews = "Number of reviews not available"

                # Append the hotel data to the list
                if name:
                    hotels.append({
                        "name": name,
                        "price": price,
                        "score": score,
                        "review_summary": review_summary,
                        "num_reviews": num_reviews
                    })

            except Exception as e:
                print(f"Error getting hotel data: {e}")
                continue

        # Print results
        print("\n=== Found Hotels ===")
        print(f"Total hotels found: {len(hotels)}\n")

        for index, hotel in enumerate(hotels, 1):
            print(f"{index}. 🏨 {hotel['name']}")
            print(f"   💲 Price: {hotel['price']}")
            print(f"   ⭐ Score: {hotel['score']}")
            print(f"   📝 Review Summary: {hotel['review_summary']}")
            print(f"   🗨️ Number of Reviews: {hotel['num_reviews']}")
            print("-" * 50)

        return hotels
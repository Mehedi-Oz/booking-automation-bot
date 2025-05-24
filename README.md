# Booking.com Automation Bot

A Python-based web automation tool that uses Selenium to search and filter hotels on Booking.com. This bot automates the hotel search process, applies filters for star ratings, and generates a formatted report of available hotels.

## Features

* **Automated Hotel Search**: Search for hotels in any destination
* **Date Selection**: Choose check-in and check-out dates
* **Guest Configuration**: Specify number of adults
* **Currency Selection**: Set currency to USD
* **Smart Filtering**: Automatically filter for 4-5 star hotels
* **Price Sorting**: Sort results by property rating (low to high)
* **Formatted Reports**: Generate clean, tabulated results with hotel names, prices, and scores

## Project Structure

```
booking-automation-bot/
├── main.py                   # Main execution script
├── README.md                 # Project documentation
└── booking/                  # Package directory
    ├── __init__.py           # Package initializer
    ├── constants.py          # Configuration constants
    ├── booking.py            # Main booking automation class
    ├── booking_filtration.py # Hotel filtering functionality
    └── booking_report.py     # Results reporting and formatting
```

## Usage

To run this project, simply run:
```bash
python main.py
```

## Example Output

The bot provides an interactive experience and generates a clean, formatted table of hotel results:

```
Where do you want to travel? Los Angeles

Enter dates in YYYY-MM-DD format (e.g., 2025-05-29)
Check in date: 2025-05-26
Check out date: 2025-05-31

Number of adults: 2

=== Found Hotels ===
Total hotels found: 24

+----+----------------------------------------------------------------+---------+-------+
| No.| Hotel Name                                                     | Price   | Score |
+----+----------------------------------------------------------------+---------+-------+
| 1  | H Hotel Los Angeles, Curio Collection By Hilton                | US$905  | 8.0   |
| 2  | Ayres Hotel Manhattan Beach                                    | US$642  | 8.3   |
| 3  | Hilton Los Angeles Airport                                     | US$691  | 7.5   |
| 4  | Hotel Erwin Venice Beach                                       | US$1,465| 8.2   |
| 5  | The Westin Los Angeles Airport                                 | US$770  | 8.2   |
...and more results
```
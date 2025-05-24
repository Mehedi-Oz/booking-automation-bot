import time
import traceback
from datetime import datetime
from booking.booking import Booking

def validate_date(date_string):
    try:
        date_string = date_string.strip()
        if len(date_string) != 10: 
            return None
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return None


with Booking() as bot:
    try:
        bot.land_first_page()
        time.sleep(30)
        bot.change_currency(currency="USD")

        destination = input("\nWhere do you want to travel? ").strip()

        print("\nEnter dates in YYYY-MM-DD format (e.g., 2025-05-29)")
        while True:
            try:
                check_in = input("Check in date: ").strip()
                check_in_date = validate_date(check_in)
                if check_in_date:
                    if check_in_date > datetime.now():
                        break
                    print("Error: Check-in date must be in the future!")
                else:
                    print("Error: Invalid date format! Use YYYY-MM-DD")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user")
                exit(0)

        while True:
            try:
                check_out = input("Check out date: ").strip()
                check_out_date = validate_date(check_out)
                if check_out_date and check_out_date > check_in_date:
                    break
                print("Error: Check-out date must be after check-in date!")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user")
                exit(0)

        # Rest of your booking logic
        bot.select_place_to_go(destination)
        bot.select_dates(check_in, check_out)

        adults = input("\nNumber of adults: ").strip()
        bot.select_adults(int(adults))

        bot.search_hotels()
        bot.apply_filters()
        bot.report_results()

        time.sleep(5)

    except Exception as e:
        # print(f"\nError occurred: {str(e)}")
        print("\nFull error trace:")
        # print(traceback.format_exc())
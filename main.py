import time
import traceback
from booking.booking import Booking

with Booking() as bot:
    try:
        bot.land_first_page()

        bot.change_currency(currency="USD")

        bot.select_place_to_go(place_to_go="New York")

        bot.select_dates(check_in_date="2025-05-29", check_out_date="2025-06-15")

        bot.select_adults(2)

        bot.search_hotels()

        bot.apply_filters()
        
        bot.refresh
        bot.report_results()
        
        time.sleep(5)

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print("\nFull error trace:")
        print(traceback.format_exc())
    finally:
        print("\nScript execution completed")
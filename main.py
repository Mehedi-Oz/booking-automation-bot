import time
from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    time.sleep(1)

    # bot.change_currency(currency="USD")
    # time.sleep(1)

    bot.select_place_to_go(place_to_go="New York")
    time.sleep(2)

    bot.select_dates(check_in_date='2025-05-29', check_out_date='2025-06-15')
    time.sleep(2)

    bot.select_adults(2)
    time.sleep(2)

    bot.search_hotels()
    time.sleep(1)

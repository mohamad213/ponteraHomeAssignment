import pytest

from src.dto.BookingDatesDto import BookingDates
from src.dto.BookingDto import Booking
from src.clients.HttpClient import BookerApiClient


@pytest.fixture(scope="session")
def default_booking_data():
    """
    Fixture that provides default booking data for tests.
    """

    default_booking_data = Booking(first_name="Jim",
                                   last_name="Brown",
                                   total_price=1151,
                                   deposit_paid=True,
                                   booking_dates=BookingDates(checkin="1970-01-01",
                                                              checkout="1970-01-01"),
                                   additional_needs="Breakfast")
    return default_booking_data


@pytest.fixture(scope="session")
def booker_api_client():
    """
    Fixture that provides an instance of the BookerApiClient for tests.
    """
    booker_api_client = BookerApiClient()
    return booker_api_client

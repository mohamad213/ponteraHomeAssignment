import json
from src.dto.BookingDatesDto import BookingDates


class Booking:
    def __init__(self, first_name: str, last_name: str, total_price: int, deposit_paid, booking_dates: BookingDates,
                 additional_needs: str):
        self.first_name = first_name
        self.last_name = last_name
        self.total_price = total_price
        self.deposit_paid = deposit_paid
        self.booking_dates = booking_dates
        self.additional_needs = additional_needs

    def update_fields(self, first_name=None, last_name=None, total_price=None, deposit_paid=None,
                      checkin=None, checkout=None, additional_needs=None):
        """
        Updates fields in the Booking instance and the nested booking_dates instance.

        :param first_name: New first_name to set.
        :param last_name: New last_name to set.
        :param total_price: New total price to set.
        :param deposit_paid: New deposit paid status to set.
        :param checkin: New checkin date to set.
        :param checkout: New checkout date to set.
        :param additional_needs: New additional needs to set.
        """
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if total_price is not None:
            self.total_price = total_price
        if deposit_paid is not None:
            self.deposit_paid = deposit_paid
        if checkin is not None or checkout is not None:
            self.booking_dates.update(checkin=checkin, checkout=checkout)
        if additional_needs is not None:
            self.additional_needs = additional_needs

    def get_as_dict(self):
        """
        Convert the booking instance to a dictionary.

        Returns:
            dict: A dictionary representation of the booking instance.
        """

        return {
            'firstname': self.first_name,
            'lastname': self.last_name,
            'totalprice': self.total_price,
            'depositpaid': self.deposit_paid,
            'bookingdates': self.booking_dates.get_as_dict(),
            'additionalneeds': self.additional_needs
        }

    def get_as_json(self):
        """
        Convert the booking instance to a JSON string.

        Returns:
            str: A JSON string representation of the booking instance.
        """

        return json.dumps(self.get_as_dict())

    def set_checkin(self, checkin: str):
        self.booking_dates.update(checkin=checkin)

    def set_checkout(self, checkout: str):
        self.booking_dates.update(checkout=checkout)

    def __repr__(self):
        """
        Return a string representation of the Booking instance for debugging purposes.

        Returns:
            str: A string representation of the Booking instance.
        """

        return json.dumps(self.get_as_dict(), indent=4)

import json


class BookingDates:
    def __init__(self, checkin: str, checkout: str):
        self.checkin = checkin
        self.checkout = checkout


    def update(self, checkin=None, checkout=None):
        """
        Updates fields in the booking_dates instance.

        :param checkin: New checkin date to set.
        :param checkout: New checkout date to set.
        """
        if checkin:
            self.checkin = checkin
        if checkout:
            self.checkout = checkout

    def get_as_dict(self):
        """
        Convert the bookingDates instance to a dictionary.

        Returns:
            dict: A dictionary representation of the bookingDates instance.
        """

        return {
            'checkin': self.checkin,
            'checkout': self.checkout
        }

    def __repr__(self):
        """
        Return a string representation of the BookingDates instance for debugging purposes.

        Returns:
            str: A string representation of the BookingDates instance.
        """

        return json.dumps(self.get_as_dict(), indent=4)

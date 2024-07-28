from src.errorhandler.StatusCodeError import StatusCodeError, BookIDError
from datetime import datetime, timedelta


def extract_field_from_json(json_data, field_name):
    """
    Recursively search for a specific field in a nested JSON dictionary or list.

    Args:
        json_data (dict or list): The JSON data to search within.
        field_name (str): The name of the field to search for.

    Returns:
        The value of the field if found, otherwise None.
    """

    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == field_name:
                return value
            elif isinstance(value, dict):
                result = extract_field_from_json(value, field_name)
                if result is not None:
                    return result
            elif isinstance(value, list):
                for item in value:
                    result = extract_field_from_json(item, field_name)
                    if result is not None:
                        return result
        return None


def is_book_id_in_booking_ids_list(booking_list, book_id_to_find):
    """
    Check if a specific booking ID exists in a list of bookings ids.

    Args:
        booking_list (list): A list of dictionaries, each representing a booking.
        book_id_to_find (int): The booking ID to search for.

    Returns:
        bool: True if the booking ID is found, False otherwise.
    """

    # Iterate through each dictionary in the list
    for booking in booking_list:
        # Check if the booking id matches the id to find
        if booking.get('bookingid') == book_id_to_find:
            return True
    return False


def verify_status_code(status_code, expected):
    """
    Verify that the actual status code matches the expected status code.

    Args:
        status_code (int): The actual status code returned from an HTTP request.
        expected (int): The expected status code.

    Raises:
        StatusCodeError: If the actual status code does not match the expected status code.
    """

    if status_code != expected:
        raise StatusCodeError(status_code, expected)


def verify_book_id_field_exist(book_id):
    """
    Verify that the book ID is not None.

    Args:
        book_id: The book ID to verify.

    Raises:
        BookIDError: If the book ID is None.
    """

    if book_id is None:
        raise BookIDError()


def get_future_date(days):
    """
    Get the date for a specified number of days in the future.

    Args:
        days (int): The number of days to add to the current date.

    Returns:
        str: The future date formatted as YYYY-MM-DD.
    """
    # Get the current date and time
    today = datetime.now()

    # Calculate the future date by adding the specified number of days
    future_date = today + timedelta(days=days)

    # Format the future date as YYYY-MM-DD
    formatted_date = future_date.strftime("%Y-%m-%d")

    return formatted_date

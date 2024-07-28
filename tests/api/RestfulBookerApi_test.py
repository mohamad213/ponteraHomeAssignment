from src.common.Utils import (extract_field_from_json, is_book_id_in_booking_ids_list, verify_status_code,
                              verify_book_id_field_exist, get_future_date)
from src.common.Consts import AUTHORIZATION
from src.common.Logger import logger
import json
import pytest


class TestRestfulBookerApi:

    @pytest.mark.apiTests
    def test_creation_new_book(self, default_booking_data, booker_api_client):
        """
        Test the creation of a new booking and verify its presence in the list of all bookings.
        """

        # Initialize booking data
        booking_data = default_booking_data

        # Set check-in and check-out dates to 7 and 9 days in the future - in order to book 2 nights next week
        checkin = get_future_date(7)
        checkout = get_future_date(9)
        booking_data.set_checkin(checkin=checkin)
        booking_data.set_checkout(checkout=checkout)

        # Convert booking data to JSON format
        booking_data_json = booking_data.get_as_json()

        # Send request to create a new booking
        logger.info(message=f"calling create book api request, with payload:\n{booking_data_json}")
        create_response = booker_api_client.create_new_book(payload=booking_data_json)

        # Verify that the status code of the create api response is 200 (OK)
        logger.info(message=f"verify create book api status code")
        verify_status_code(status_code=create_response.status_code, expected=200)

        # Parse the response JSON to extract the booking ID
        create_response_json = json.loads(create_response.text)
        book_id = extract_field_from_json(json_data=create_response_json, field_name="bookingid")

        # Verify that the booking ID field exists in the response
        logger.info(message=f"verify bookingid field exists")
        verify_book_id_field_exist(book_id=book_id)

        # Send request to get the list of all bookings
        logger.info(message=f"calling get all books ids api request")
        get_all_booking_response = booker_api_client.get_all_booking_ids()

        # Verify that the status code of the get all bookings response is 200 (OK)
        logger.info(message=f"verify get booking ids api status code")
        verify_status_code(status_code=get_all_booking_response.status_code, expected=200)

        # Parse the response JSON to get the list of all bookings
        get_all_booking_response_json = json.loads(get_all_booking_response.text)

        # Check if the newly created booking ID is present in the list of all bookings
        is_book_exit = is_book_id_in_booking_ids_list(get_all_booking_response_json, book_id)

        # Assert that the newly created booking is present in the list
        assert is_book_exit is True, f"recently created book, id:{book_id} was not found on all booking list."

    @pytest.mark.apiTests
    def test_updating_exist_book(self, default_booking_data, booker_api_client):
        """
        Test the updating of an existing booking and verify the updated fields.
        """

        # Initialize booking data
        booking_data = default_booking_data

        # Set initial check-in and check-out dates to 7 and 11 days in the future - in order to book 4 nights next week
        checkin = get_future_date(7)
        checkout = get_future_date(11)
        booking_data.set_checkin(checkin=checkin)
        booking_data.set_checkout(checkout=checkout)

        # Convert booking data to JSON format
        booking_data_json = booking_data.get_as_json()

        # Send request to create a new booking
        logger.info(message=f"calling create book api request, with payload:\n{booking_data_json}")
        create_response = booker_api_client.create_new_book(payload=booking_data_json)

        # Verify that the status code of the create api response is 200 (OK)
        logger.info(message=f"verify create book api status code")
        verify_status_code(status_code=create_response.status_code, expected=200)

        # Parse the response JSON to extract the booking ID
        create_response_json = json.loads(create_response.text)
        book_id = extract_field_from_json(json_data=create_response_json, field_name="bookingid")

        # Verify that the booking ID field exists in the response
        logger.info(message=f"verify bookingid field exists")
        verify_book_id_field_exist(book_id=book_id)

        # Update the check-out date to 12 days in the future - in order extend the book to 5 nights
        checkout = get_future_date(12)
        booking_data.update_fields(checkout=checkout)

        # Convert updated booking data to JSON format
        updated_data = booking_data.get_as_json()

        # Send request to update the booking by ID
        logger.info(message=f"calling update book by id api request, with payload:\n{updated_data}")
        update_response = booker_api_client.update_book_by_id(book_id=book_id, payload=updated_data,
                                                              authorization=AUTHORIZATION)

        # Verify that the status code of the update response is 200 (OK)
        logger.info(message=f"verify update book by id api status code")
        verify_status_code(status_code=update_response.status_code, expected=200)

        # Parse the update response JSON to extract the new check-out date
        update_response_json = json.loads(update_response.text)
        new_checkout = extract_field_from_json(json_data=update_response_json, field_name='checkout')

        # Assert that the new check-out date matches the expected check-out date
        assert new_checkout == checkout, (f"new checkout expected to be equals to: {checkout}, "
                                          f""f"actual: {new_checkout}")

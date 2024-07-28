import requests
from src.common.Consts import BOOKER_API_BASE_URL


class BookerApiClient:
    def __init__(self):
        """
        Initializes the APIClient with the base URL of the API.
        """
        self.base_url = BOOKER_API_BASE_URL

    def get_book_by_id(self, book_id: int):
        """
        Retrieve a booking by its ID.

        Args:
            book_id (int): The ID of the booking to retrieve.

        Returns:
            Response: The response object from the GET request.

        Raises:
            Exception: If there is an error during the API call.
        """

        try:
            url = f"{self.base_url}/booking/{book_id}"  # Construct the URL for the GET request
            headers = {'Accept': 'application/json'}  # Set the request headers
            response = requests.request(method="GET", url=url, headers=headers)  # Make the GET request
            return response
        except Exception as e:
            # Raise an exception with a custom error message if an error occurs
            raise Exception(f"Error during get_book_by_id: {e}")

    def create_new_book(self, payload: str):
        """
        Create a new booking with the provided payload.

        Args:
            payload (str): The JSON payload containing the booking details.

        Returns:
            Response: The response object from the POST request.

        Raises:
            Exception: If there is an error during the API call.
        """

        try:
            url = f"{self.base_url}/booking"  # Construct the URL for the POST request
            # Set the request headers
            headers = {'Content-Type': 'application/json',
                       'Accept': 'application/json'}
            response = requests.request(method="POST", url=url, headers=headers, data=payload)  # Make the POST request
            return response
        except Exception as e:
            # Raise an exception with a custom error message if an error occurs
            raise Exception(f"Error during create_new_book: {e}")

    def update_book_by_id(self, book_id: int, payload: str, authorization: str):
        """
        Update an existing booking by its ID with the provided payload and authorization.

        Args:
            book_id (int): The ID of the booking to update.
            payload (str): The JSON payload containing the updated booking details.
            authorization (str): The authorization token for the request.

        Returns:
            Response: The response object from the PUT request.

        Raises:
            Exception: If there is an error during the API call.
        """

        try:
            url = f"{self.base_url}/booking/{book_id}"  # Construct the URL for the PUT request
            # Set the request headers
            headers = {'Content-Type': 'application/json',
                       'Accept': 'application/json',
                       'Authorization': authorization}
            response = requests.request(method="PUT", url=url, headers=headers, data=payload)  # Make the PUT request
            return response
        except Exception as e:
            # Raise an exception with a custom error message if an error occurs
            raise Exception(f"Error during update_book_by_id: {e}")

    def get_all_booking_ids(self):
        """
        Retrieve all bookings ids.

        Returns:
            Response: The response object from the GET request.

        Raises:
            Exception: If there is an error during the API call.
        """

        try:
            url = f"{self.base_url}/booking"  # Construct the URL for the GET request
            response = requests.request(method="GET", url=url)  # Make the GET request
            return response
        except Exception as e:
            # Raise an exception with a custom error message if an error occurs
            raise Exception(f"Error during get_all_booking: {e}")

class StatusCodeError(Exception):
    """Custom exception for status code verification errors."""
    def __init__(self, status_code, expected):
        self.status_code = status_code
        self.expected = expected
        super().__init__(f"Status code {status_code} does not match expected {expected}")


class BookIDError(Exception):
    """Custom exception for None book_id errors."""
    def __init__(self):
        super().__init__("bookingid cannot be None")
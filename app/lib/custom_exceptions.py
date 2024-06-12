from app.lib.constants import DEFAULT_ERROR_MESSAGE


class CustomBaseException(Exception):
    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class DuplicateRecordException(CustomBaseException):
    """Raise when Duplicate record is created"""


class DBCreateRecordException(CustomBaseException):
    """Raise while failed to create a new record in database table"""


class DBRecordNotFoundException(CustomBaseException):
    """Raise when no record exist based on query parameters."""


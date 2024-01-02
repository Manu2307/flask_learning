DEFAULT_ERROR_MESSAGE = 'An unexpected error has occurred.'

class DuplicateRecordException(Exception):
    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class CreateRecordFailed(Exception):
    def __init__(self, msg=DEFAULT_ERROR_MESSAGE, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class CreateRecordFailure(Exception):
    pass


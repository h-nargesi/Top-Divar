class StorageError(Exception):
    pass


class DuplicateTokenError(StorageError):
    pass


class DuplicateUsernameError(StorageError):
    pass

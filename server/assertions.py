from server.exceptions import InvalidUsage


def assert_true(condition, message='Forbidden', status_code=403):
    if condition is not True:
        raise InvalidUsage(message, status_code=status_code)


def assert_found(instance, message='Not Found', status_code=404):
    if instance is None:
        raise InvalidUsage(message, status_code=status_code)


def assert_valid(condition, message='Bad Request'):
    assert_true(condition, message, status_code=400)


def assert_good(condition, message='Something went wrong'):
    assert_true(condition, message, status_code=500)


def assert_auth(condition, message='Unauthorized'):
    assert_true(condition, message, status_code=401)

class CustomError(Exception):
    pass

class SpecificError(Exception):
    pass

try:
    raise SpecificError("This is a specific error.")
except SpecificError as specific_exception:
    try:
        raise CustomError("Custom error occurred.") from specific_exception
    except CustomError as custom_exception:
        print("Custom Error Message:", custom_exception)
        print("Original Exception Message:", custom_exception)

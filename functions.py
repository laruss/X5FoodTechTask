""" module with reusable functions """
from zoneinfo import ZoneInfo


def assert_type(data, data_type):
    """ asserts that @data has certain type """
    assert type(data) == data_type


def assert_str_as_int(value):
    """ asserts that @value is string, but int(string) can be used"""
    assert_type(value, str)
    assert_type(int(value), int)


def time_as_str_test(time_as_str):
    """ asserts the @time_as_str is string and its valid """
    """ @time_as_str is '23:10' """
    time_list = time_as_str.split(':')
    assert 0 <= int(time_list[0]) < 24
    assert 0 <= int(time_list[1]) < 60


def timezone_test(timezone):
    """ asserts the @timezone is valid time zone """
    try:
        ZoneInfo(timezone)
    except:
        raise ValueError("Timezone {} is not valid".format(timezone))

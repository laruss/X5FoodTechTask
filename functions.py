from zoneinfo import ZoneInfo


def assert_type(data, data_type):
    assert type(data) == data_type


def assert_str_as_int(value):
    assert_type(value, str)
    assert_type(int(value), int)


def time_as_str_test(time_as_str):
    time_list = time_as_str.split(':')
    assert 0 <= int(time_list[0]) < 24
    assert 0 <= int(time_list[1]) < 60


def timezone_test(timezone):
    try:
        ZoneInfo(timezone)
    except:
        raise ValueError("Timezone {} is not valid".format(timezone))

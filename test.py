from settings import *
import functions as f


def test_request_status_content_type(client):
    r = client.get(PATH)
    assert r.status_code == 200
    assert r.headers["Content-Type"] == "application/json"


def test_request_data(client):
    """ main test of request's data """

    def item_test(item):
        """ test for content in `item` """
        f.assert_type(item['id'], int)
        f.assert_str_as_int(item['shop_id'])
        zones_test(item['zones'])
        f.assert_type(item['accepting'], bool)
        f.assert_type(item['enable'], bool)
        schedule_test(item['schedule'])
        weight_limits_test(item['weight_limits'])
        f.timezone_test(item['timezone'])

    def zones_test(zones):
        """ test for content in `zones` """
        assert len(zones) > 0
        for zone in zones:
            for z in zone:
                f.assert_type(z['lat'], float)
                assert abs(z['lat']) <= 90

                f.assert_type(z['lng'], float)
                assert abs(z['lng']) <= 180

    def schedule_test(schedule):
        """ test for content in `schedule` """
        f.assert_type(schedule['open'], int)
        f.assert_type(schedule['close'], int)
        f.time_as_str_test(schedule['open_str'])
        f.time_as_str_test(schedule['close_str'])

    def weight_limits_test(weight_limits):
        """ test for content in `weight_limits` """
        f.assert_type(weight_limits['total_initial'], int)
        f.assert_type(weight_limits['total_replacement'], int)
        f.assert_type(weight_limits['drinks_initial'], float)
        f.assert_type(weight_limits['drinks_replacement'], int)
        f.assert_type(weight_limits['ignore'], bool)

    r = client.get(PATH)
    data = r.get_json()

    assert data['TYPE'] == 'SUCCESS'

    items = data['ANS']['items']
    f.assert_type(items, list)
    assert len(items) > 0

    for item in items:
        item_test(item)

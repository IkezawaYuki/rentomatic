from rentomatic.requests.room_list import build_room_list_request


def test_build_room_list_request_without_parameters():
    request = build_room_list_request()

    assert request.filter is None
    assert bool(request) is True


def test_build_room_list_request_from_empty_dict():
    request = build_room_list_request({})
    assert request.filters == 0
    assert bool(request) is True


def test_build_room_list_request_with_invalid_filters_parameter():
    request = build_room_list_request(filters=5)
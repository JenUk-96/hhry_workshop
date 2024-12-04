from src.hh_api import HeadHunterApi
from unittest.mock import patch


@patch("requests.get")
def test_head_hunter_api_requests(test_requests_api):

    obj_api = HeadHunterApi()
    assert type(obj_api) is HeadHunterApi
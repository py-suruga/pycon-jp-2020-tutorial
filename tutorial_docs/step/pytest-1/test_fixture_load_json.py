import json
import pytest


# jsonをloadする共通の関数
@pytest.fixture
def get_json_dict():

    return json.loads(
        """
        {"k1": "testval1", "k2": "testval2"}
        """
    )


# fixtureを使いたいテスト関数にfixture化した関数を引数へ指定する
def test_check_val1(get_json_dict):
    json_dict = get_json_dict
    assert "testval1" == json_dict["k1"]


def test_check_val2(get_json_dict):
    json_dict = get_json_dict
    assert "testval1" != json_dict["k2"]

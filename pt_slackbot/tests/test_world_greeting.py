from botfunc import world_greeting
import pytest


@pytest.fixture()
def setup_non_random(monkeypatch):

    # ランダムで返す結果を固定にする
    monkeypatch.setattr(world_greeting, "GREETING_LIST", [("こんにちは！", ":jp:")])


# @pytest.mark.parametrize()
def test_greeting_result(setup_non_random):
    """
    アイサツの文章が決めたとおりに出力されるかを確認
    """
    result = world_greeting.call_function("test")

    assert result == ":jp:ノアイサツデス :robot_face: 「こんにちは！」"

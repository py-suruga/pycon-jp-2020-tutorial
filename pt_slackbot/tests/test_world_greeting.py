from botfunc import world_greeting
import pytest


@pytest.fixture()
def setup_non_random(monkeypatch):

    # ランダムで返す結果を固定にする:アイサツリストを1行のみにして、結果的に1つの結果のみを返すようにする
    monkeypatch.setattr(world_greeting, "GREETING_LIST", [("こんにちは！", ":jp:")])


def test_greeting_result(setup_non_random):
    """
    アイサツの文章が決めたとおりに出力されるかを確認
    """
    result = world_greeting.call_function("test")

    assert result == ":jp:ノアイサツデス :robot_face: 「こんにちは！」"

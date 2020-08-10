from botfunc import search_connpass_online
import pytest


@pytest.fixture()
def mock_json(monkeypatch):
    """
    connpassAPIのレスポンスになるjsonをjsonファイルに固定する
    """

    # monkeypatch.setattr(world_greeting, "GREETING_LIST", [("こんにちは！", ":jp:")])


def test_search_online_event(mock_json):
    """
    アイサツの文章が決めたとおりに出力されるかを確認
    """
    result = search_connpass_online.search_online_event()

    assert result == "connpassで検索したオンラインに関係するイベントです"

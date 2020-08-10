from botfunc import search_connpass_online
import pytest
import json

from pathlib import Path


@pytest.fixture()
def mocking_connpass_json(monkeypatch):
    """
    connpassAPIのレスポンスになるjsonをjsonファイルに固定する
    """

    def test_connpass_json(ym):
        """
        テスト用のconnpass api レスポンス結果をjsonファイルからloadする

        引数ymは受け取るだけ
        """

        test_jsonpath = Path(__file__).parent / "test_connpass_api.json"
        return json.load(open(test_jsonpath, encoding="utf-8"))

    monkeypatch.setattr(
        search_connpass_online, "request_connpass_api", test_connpass_json
    )


def test_search_online_event(mocking_connpass_json):
    """
    アイサツの文章が決めたとおりに出力されるかを確認
    """
    result = search_connpass_online.search_online_event("202008")

    assert "connpassで検索したオンラインに関係する" in result

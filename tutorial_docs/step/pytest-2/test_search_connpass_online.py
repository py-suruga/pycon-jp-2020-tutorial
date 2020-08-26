from botfunc import search_connpass_online
import pytest
import json

from pathlib import Path


@pytest.fixture()
def mocking_connpass_json(monkeypatch):
    """
    connpassAPIのレスポンスになるjsonをjsonファイルに固定するmonkeypatch
    """

    def test_connpass_json(ym):
        """
        テスト用のconnpass api レスポンス結果をjsonファイルからloadする
        引数ymは受け取るだけ
        pytest monkeypachで関数の置き換えを行うときに利用する
        """

        test_jsonpath = Path(__file__).parent / "test_connpass_api.json"
        return json.load(open(test_jsonpath, encoding="utf-8"))

    monkeypatch.setattr(
        search_connpass_online, "request_connpass_api", test_connpass_json
    )


def test_search_online_event(mocking_connpass_json):
    """
    connpass bot側が決めたとおりに文字列を生成するかを調べる
    """
    # 引数は実質意味がないです
    result = search_connpass_online.search_online_event("202008")

    # connpass apiレスポンスからjson -> 置き換えたjson生成の関数 でbotの返答文字列が生成されている
    assert "connpassで検索したオンラインに関係する" in result

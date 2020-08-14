# coding:utf-8

import copy
from typing import Union

import requests


def request_connpass_api(ym):
    """
    connpass APIへのリクエストを行う。
    connpassで、"Python"に関係する"オンライン"イベントを検索する。
    年月を指定して、その年月から関係するイベントから先頭20件を取得する
    """
    api_url = "https://connpass.com/api/v1/event/"
    keywords = ["オンライン", "Python"]

    # connpass apiよりイベント情報を取得する
    # keywordを複数入れるので、
    payload = {"keyword": keywords, "count": 20, "ym": ym}
    r = requests.get(api_url, params=payload)

    # jsonをパースする
    return r.json()


def search_online_event(ym: str) -> Union[str, None]:
    """
    request_connpass_apiで受け取った結果をbotの戻り文字列として生成する
    """

    # jsonをパースする
    result = request_connpass_api(ym)
    events: list = copy.copy(result["events"])

    # オンラインイベントのみを抽出する。

    if not events:
        return None

    events.sort(key=lambda x: x["started_at"])

    result_lines = list()
    # 結果を書き出す

    result_lines.append("connpassで検索したオンラインに関係するイベントです")

    for event in events:
        ev_date = event["started_at"][0:10]  # json日付文字列なので10文字分スライスする
        ev_title = event["title"]
        ev_link = event["event_url"]

        # イベント情報を
        result_lines.append("- {}|{}|{}".format(ev_date, ev_title, ev_link))

    return "\n".join(result_lines)


def call_function(match_group: Union[str, None]) -> Union[str, None]:
    """
    botの結果を返すfunction
    """

    result = search_online_event(match_group)

    if result is None:
        return None
    return result

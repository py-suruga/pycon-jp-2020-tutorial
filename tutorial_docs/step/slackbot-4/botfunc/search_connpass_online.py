# coding:utf-8

import copy

import requests


def search_online_event(ym: str) -> str:
    """
    request_connpass_apiで受け取った結果をbotの戻り文字列として生成する
    """

    api_url = "https://connpass.com/api/v1/event/"
    keywords = ["オンライン", "Python"]

    # connpass apiよりイベント情報を取得する
    # keywordを複数入れるので、
    payload = {"keyword": keywords, "count": 20, "ym": ym}
    r = requests.get(api_url, params=payload)

    # jsonをパースする
    result = r.json()
    events = copy.copy(result["events"])

    # 結果が無い場合は空文字を返す
    if not events:
        return ""

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


def call_function(arg: str = "") -> str:
    return search_online_event(arg)

# coding:utf-8

import copy
from typing import Union

import requests


def search_online_event():
    """
    connpassでオンラインイベントを検索する
    今日を基準に50件ほどの検索結果を出して、オンラインのイベントを返す
    """
    api_url = "https://connpass.com/api/v1/event/"
    keyword = "オンライン"

    # コマンド情報から年月の数字を抜き出す

    # connpass apiよりイベント情報を取得する
    payload = {"keyword": keyword, "count": 50}
    r = requests.get(api_url, params=payload)

    # jsonをパースする
    result = r.json()
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
        result_lines.append("- {}:{} {}".format(ev_date, ev_title, ev_link))

    return "\n".join(result_lines)


def call_function(match_group: Union[str, None]) -> Union[str, None]:
    """
    botの結果を返すfunction
    """

    result = search_online_event()

    if result is None:
        return None
    return result

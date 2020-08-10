# coding:utf-8

import requests
from pathlib import Path
import json


def main(ym: str):
    """
    テスト用にconnpassからテストデータ用のjsonをDLするスクリプト

    """
    api_url = "https://connpass.com/api/v1/event/"
    keywords = ["オンライン", "Python"]

    payload = {"keyword": keywords, "count": 20, "ym": ym}
    r = requests.get(api_url, params=payload)
    r.encoding = r.apparent_encoding

    # jsonをパースする
    with open(
        Path(__file__).parent / "./test_connpass_api.json", "w", encoding="utf-8"
    ) as connpass_api_json:
        json.dump(r.json(), connpass_api_json, indent=4, ensure_ascii=False)


if __name__ == "__main__":

    main("202008")

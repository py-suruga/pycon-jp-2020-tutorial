# coding:utf-8

from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup

# 気象庁の週間天気予報はあらかじめ生成している

JMA_WEEKLY_XMLFILESS_DIR = Path(__file__).parent / "jma_weekly_xmlfiles"

KISYODAI_STATION_MAPS = {
    "東京都府県週間天気予報": ["東京", "東京地方"],
    "静岡県府県週間天気予報": ["静岡", "静岡県"],
}


def get_weekly_weather(station_name: str) -> str:
    # KISYODAI_STATION_MAPSをループして、該当の地域かをチェック
    weekly_weather_xml_soup = None
    for kisyodai_name, station_list in KISYODAI_STATION_MAPS.items():
        # callbackの引数の文字列に、station_listから検索
        if station_name in station_list:
            xml_filepath = JMA_WEEKLY_XMLFILESS_DIR / "{}.xml".format(kisyodai_name)
            with open(xml_filepath, "r", encoding="utf-8") as weekly_weather_xml:
                weekly_weather_xml_soup = BeautifulSoup(weekly_weather_xml, "xml")
            break

    # 該当しない場合は何も返せなかったとしてNoneを返す
    if not weekly_weather_xml_soup:
        return None

    # 該当した場合は、気象台の情報をもとに、気象台のxmlを開いて予報を取得
    kuiki_yohou = weekly_weather_xml_soup.find("MeteorologicalInfos", type="区域予報")

    # 天気を表示

    # 時間とセット
    daylist = kuiki_yohou.TimeSeriesInfo.find_all("TimeDefine")
    weatherlist = kuiki_yohou.find_all("jmx_eb:Weather")

    # （破壊的変更）zip関数でまとめるためにIDでソート:しなくても本当は良いけど
    daylist.sort(key=lambda t: t["timeId"])
    weatherlist.sort(key=lambda t: t["refID"])

    # 必要な情報だけを抜き出す
    yohou_set = zip(
        [datetime.fromisoformat(d.DateTime.text).strftime("%m/%d") for d in daylist],
        [w.text for w in weatherlist],
    )

    # 文字列として流す用に整形する:気象台発表の週間天気予報
    result_lines = list()
    result_lines.append(
        "{}発表、{}の週間天気予報です。".format(
            weekly_weather_xml_soup.PublishingOffice.text, station_name
        )
    )
    for yohou_date, yohou_weather in yohou_set:
        result_lines.append("{} : {}".format(yohou_date, yohou_weather))

    return "\n".join(result_lines)


def call_function(arg: str = "") -> str:

    return get_weekly_weather(arg)

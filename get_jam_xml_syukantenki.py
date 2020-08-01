# coding: utf-8

from pprint import pprint
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime

# ファイルを読み込んで週間天気予報を表示する
for file in Path("./syukantenki_xml").glob("*.xml"):

    xml_soup = BeautifulSoup(open(file, encoding="utf-8"), "xml")

    # 地域名
    kuiki = xml_soup.find("MeteorologicalInfos", type="区域予報")

    print(
        "{}: {}".format(xml_soup.Head.Title.text, kuiki.TimeSeriesInfo.Area.Name.text)
    )
    # 天気を表示

    # 時間とセット
    weather_days: list = kuiki.TimeSeriesInfo.find_all("TimeDefine")
    yohou_list = kuiki.find_all("jmx_eb:Weather")

    # IDでソートして:しなくても本当は良いけどね（破壊的変更））
    weather_days.sort(key=lambda t: t["timeId"])
    yohou_list.sort(key=lambda t: t["refID"])

    # zipでまとめた
    yohou_set = list(zip(weather_days, yohou_list))

    pprint(
        [
            (
                datetime.fromisoformat(date_t.DateTime.text).strftime("%m/%d"),
                yohou_t.text,
            )
            for date_t, yohou_t in yohou_set
        ]
    )

    # exit()

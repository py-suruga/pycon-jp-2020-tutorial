# coding: utf-8

from pathlib import Path
from bs4 import BeautifulSoup

# ファイルを読み込んで週間天気予報を表示する
for file in Path("./syukantenki_xml").glob("*.xml"):

    xml_soup = BeautifulSoup(open(file, encoding="utf-8"), "xml")

    with open(
        file.parent / "{}_prettify.xml".format(file.name), "w", encoding="utf-8"
    ) as xml_soup_prettify:
        xml_soup_prettify.write(xml_soup.prettify())

    print(xml_soup.Head.Title)

    # 地域名
    kuiki = xml_soup.find_all("MeteorologicalInfos", type="区域予報")
    print(len(kuiki))
    # 天気を

    # exit()

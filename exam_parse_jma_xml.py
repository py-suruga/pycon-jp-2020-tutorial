# coding: utf-8
import itertools
from bs4 import BeautifulSoup

with open("regular_l.xml", encoding="utf-8") as jma_xmlfile:
    soup_jma_xml = BeautifulSoup(jma_xmlfile, "xml")

# entityから、府県週間天気予報 > 各気象台の情報を一覧でだして、最新の予報の電文xmlを探しに行く

tenki_list = list()

# 週間予報のみのリストを作る
yohou_list = sorted(
    [e for e in soup_jma_xml.find_all("entry") if e.find("title", text="府県週間天気予報")],
    key=lambda e: e.author.text,
)

# groupbyで地域事の週間天気予報の電文をまとめる
station_by_yohou_list = itertools.groupby(yohou_list, lambda e: e.content.text)

for name, g in station_by_yohou_list:
    content = name
    list_g = list(g)

    # ソートで最新の週間天気予報の電文を取りに行く
    g_new = sorted(list_g, key=lambda e: e.updated.text, reverse=True)[0]

    updated = g_new.updated.text
    new_url = g_new.link["href"]

    print(f"{content}: updated:{updated} new_url:{new_url}")
    tenki_list.append(f"{content}: updated:{updated} new_url:{new_url}\n")


with open("export_tenki_list.txt", "w", encoding="utf-8") as export_file:
    export_file.writelines(tenki_list)

#


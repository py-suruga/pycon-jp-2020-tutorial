# coding: utf-8

from pathlib import Path
from bs4 import BeautifulSoup

# ファイルを読み込んでxml
for file in Path("./syukantenki_xml").glob("*.xml"):

    xml_soup = BeautifulSoup(open(file, encoding="utf-8"), "xml")

    print(xml_soup)

    exit()

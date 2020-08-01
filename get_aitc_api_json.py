import json
import requests

from pathlib import Path


syukantenki_dir = Path("./syukantenki_json/")
syukantenki_dir.mkdir(exist_ok=True)

# aitcで "週間天気予報", 日時を今日, 昨日 で絞る
search_url = "http://api.aitc.jp/jmardb-api/search?datetime=2020-07-31 00:00:00&datetime=2020-08-01 00:00:00&order=new&title=府県週間天気予報&limit=55"
search_result_response = requests.get(search_url)


search_result = json.loads(search_result_response.text)

# print(search_result)
# jsonをループして、項目ごとのjsonから気象台名とurlを取り出す。
# 週間予報は日に二回ほどあるが、一度だけでいい（検索結果のAPIで新しい順にするので自動的に最新になる）ので、気象台の名称を見て二度目を追加しないようにする

download_syukanyohou_kisyodai = list()
for syukanyohou in search_result["data"]:
    # jsonのget
    print(syukanyohou["link"] + ".json")
    syukanyohou_response = requests.get(syukanyohou["link"] + ".json")
    syukanyohou_json = json.loads(syukanyohou_response.text)

    kisyodai_name = syukanyohou_json["report"]["head"]["title"]

    print(kisyodai_name)
    # すでに追加済みの気象台があったら
    if kisyodai_name in download_syukanyohou_kisyodai:
        continue

    # ファイルの保存
    savefilepath = syukantenki_dir / "{}.json".format(kisyodai_name)
    with open(savefilepath, "w", encoding="utf-8") as savefile:
        savefile.write(json.dumps(syukanyohou_json, indent=4, ensure_ascii=False))

    # ＤL済みの週間予報の気象台名を記載
    download_syukanyohou_kisyodai.append(kisyodai_name)

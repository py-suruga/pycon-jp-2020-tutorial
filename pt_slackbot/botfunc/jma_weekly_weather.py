# coding:utf-8
import itertools
import pickle
from datetime import datetime, timedelta
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from pytz import timezone

# 気象庁の週間天気予報をここで生成する

JMA_WEEKLY_XMLFILESS_DIR = Path(__file__).parent / "jma_weekly_xmlfiles"

KISYODAI_STATION_MAPS = {
    "東京都府県週間天気予報": ["東京", "東京地方"],
    "宮崎県府県週間天気予報": ["宮崎", "宮崎県"],
    "岡山県府県週間天気予報": ["岡山", "岡山県"],
    "千葉県府県週間天気予報": ["千葉", "千葉県"],
    "栃木県府県週間天気予報": ["栃木", "栃木県"],
    "三重県府県週間天気予報": ["三重", "三重県"],
    "福島県府県週間天気予報": ["福島", "福島県", "中通り・浜通り"],
    "茨城県府県週間天気予報": ["茨城", "茨城県"],
    "新潟県府県週間天気予報": ["新潟", "新潟県"],
    "八重山地方府県週間天気予報": ["八重山地方"],
    "熊本県府県週間天気予報": ["熊本", "熊本県"],
    "岐阜県府県週間天気予報": ["岐阜", "岐阜県"],
    "鳥取県府県週間天気予報": ["鳥取", "鳥取県"],
    "群馬県府県週間天気予報": ["群馬", "群馬県"],
    "長野県府県週間天気予報": ["長野", "長野県"],
    "石川県府県週間天気予報": ["石川", "石川県"],
    "奈良県府県週間天気予報": ["奈良", "奈良県"],
    "山梨県府県週間天気予報": ["山梨", "山梨県"],
    "兵庫県府県週間天気予報": ["兵庫", "兵庫県"],
    "大東島地方府県週間天気予報": ["大東島地方"],
    "青森県府県週間天気予報": ["青森", "青森県", "津軽"],
    "佐賀県府県週間天気予報": ["佐賀", "佐賀県"],
    "京都府府県週間天気予報": ["京都", "京都府"],
    "福岡県府県週間天気予報": ["福岡", "福岡県"],
    "山口県府県週間天気予報": ["山口", "山口県"],
    "宮古島地方府県週間天気予報": ["宮古島地方"],
    "岩手県府県週間天気予報": ["岩手", "岩手県", "内陸"],
    "長崎県府県週間天気予報": ["長崎", "長崎県"],
    "大阪府府県週間天気予報": ["大阪", "大阪府"],
    "大分県府県週間天気予報": ["大分", "大分県"],
    "沖縄本島地方府県週間天気予報": ["沖縄", "沖縄本島地方"],
    "埼玉県府県週間天気予報": ["埼玉", "埼玉県"],
    "石狩・空知・後志地方府県週間天気予報": ["石狩・空知・後志地方"],
    "高知県府県週間天気予報": ["高知", "高知県"],
    "網走・北見・紋別地方府県週間天気予報": ["網走・北見・紋別地方"],
    "山形県府県週間天気予報": ["山形", "山形県"],
    "島根県府県週間天気予報": ["島根", "島根県"],
    "愛知県府県週間天気予報": ["愛知", "愛知県"],
    "釧路・根室・十勝地方府県週間天気予報": ["釧路・根室地方"],
    "愛媛県府県週間天気予報": ["愛媛", "愛媛県"],
    "福井県府県週間天気予報": ["福井", "福井県"],
    "渡島・檜山地方府県週間天気予報": ["渡島・檜山地方"],
    "宗谷地方府県週間天気予報": ["宗谷地方"],
    "広島県府県週間天気予報": ["広島", "広島県"],
    "徳島県府県週間天気予報": ["徳島", "徳島県"],
    "上川・留萌地方府県週間天気予報": ["上川・留萌地方"],
    "鹿児島県府県週間天気予報": ["鹿児島", "鹿児島県", "鹿児島県（奄美地方除く）"],
    "滋賀県府県週間天気予報": ["滋賀", "滋賀県"],
    "静岡県府県週間天気予報": ["静岡", "静岡県"],
    "富山県府県週間天気予報": ["富山", "富山県"],
    "宮城県府県週間天気予報": ["宮城", "宮城県", "東部"],
    "胆振・日高地方府県週間天気予報": ["胆振・日高地方"],
    "和歌山県府県週間天気予報": ["和歌山", "和歌山県"],
    "神奈川県府県週間天気予報": ["神奈川", "神奈川県"],
    "秋田県府県週間天気予報": ["秋田", "秋田県"],
    "香川県府県週間天気予報": ["香川", "香川県"],
}


def get_jma_xml_files():
    """
    気象庁の府県週間天気予報の電文XMLファイルを取得します。
    すでに取得済みで、取得日が現在の日付より12時間前の場合は取得はされません。
    """
    # xml保存のパスとディレクトリ生成を強制: ディレクトリ存在が面倒なのでこうしてるけど、Winで問題あったら変える
    JMA_WEEKLY_XMLFILESS_DIR.mkdir(exist_ok=True)
    latest_dt_filename = JMA_WEEKLY_XMLFILESS_DIR / "latest_dt.dat"

    # 取得日の日付の12時間経過してない場合は、そのまま終了。
    if latest_dt_filename.exists():
        with open(latest_dt_filename, "rb") as latest_dt_file:
            latest_dt = pickle.load(latest_dt_file)
            if latest_dt + timedelta(hours=12) > datetime.now(timezone("Asia/Tokyo")):
                print("12時間越してないので更新しません")
                return

    # 気象庁のatomフィードを取りに行く
    res_jma_feed = requests.get(
        "http://www.data.jma.go.jp/developer/xml/feed/regular_l.xml"
    )
    res_jma_feed.encoding = res_jma_feed.apparent_encoding

    soup_jma_feed = BeautifulSoup(res_jma_feed.content, "xml")

    # atomフィードのupdatedを取得日として記録する
    updated_iso_str = soup_jma_feed.updated.text.replace("Z", "")
    updated_dt = datetime.fromisoformat(updated_iso_str)

    # 週間予報のみのリストを作る
    weekly_weather_list = sorted(
        [
            e
            for e in soup_jma_feed.find_all("entry")
            if e.find("title", text="府県週間天気予報")
        ],
        key=lambda e: e.author.text,
    )

    # groupbyで地域事の週間天気予報の電文をまとめる
    kisyodai_by_weekly_weather_list = itertools.groupby(
        weekly_weather_list, lambda e: e.content.text
    )

    for kisyodai_name, g in kisyodai_by_weekly_weather_list:
        # ソートで最新の週間天気予報の電文を取りに行く
        g_latest_tag = sorted(list(g), key=lambda e: e.updated.text, reverse=True)[0]

        # 最新の電文xmlを気象台名で保存
        jma_weekly_weather_xml = requests.get(g_latest_tag.link["href"])
        jma_weekly_weather_xml.encoding = jma_weekly_weather_xml.apparent_encoding

        # 【＊＊気象台】とあるので、前後のカッコを削る
        xml_save_filepath = JMA_WEEKLY_XMLFILESS_DIR / "{}.xml".format(
            kisyodai_name[1:-1]
        )

        with open(xml_save_filepath, "w", encoding="utf-8") as xml_save_file:
            xml_save_file.write(jma_weekly_weather_xml.text)

    # 取得日をファイルに記載
    pickle.dump(updated_dt, open(latest_dt_filename, "wb"))


def get_weekly_weather(station_name: str) -> str:
    """

    Args:
        station_name: KISYODAI_STATION_MAPSにある地域名

    Returns:
        botに渡す文字列を返します

    station_nameで指定した地域名を元に、ダウンロード済みの気象庁週間予報XMLファイルをパースして、週間予報の結果を返します。

    """
    # KISYODAI_STATION_MAPSをループして、該当の地域かをチェック
    weekly_weather_xml_soup = None
    for kisyodai_name, station_list in KISYODAI_STATION_MAPS.items():
        # callbackの引数の文字列に、station_listから検索
        if station_name in station_list:
            xml_filepath = JMA_WEEKLY_XMLFILESS_DIR / "{}.xml".format(kisyodai_name)
            with open(xml_filepath, "r", encoding="utf-8") as weekly_weather_xml:
                weekly_weather_xml_soup = BeautifulSoup(weekly_weather_xml, "xml")
            break

    # 該当しない場合は何も返せなかったとして空文字を返す
    if not weekly_weather_xml_soup:
        return ""

    # 該当した場合は、気象台の情報をもとに、気象台のxmlを開いて予報を取得
    kuiki_yohou = weekly_weather_xml_soup.find("MeteorologicalInfos", type="区域予報")

    # 日付と予報をそれぞれ検索
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

    # 気象庁の週間天気予報電文XMLをDL
    get_jma_xml_files()

    return get_weekly_weather(arg)

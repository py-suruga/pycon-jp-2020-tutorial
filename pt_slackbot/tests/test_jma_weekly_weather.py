# coding:utf-8

from pathlib import Path
from botfunc import jma_weekly_weather
import pytest

# 気象庁xmlから天気予報を呼び出すbot機能のテスト

# TODO:2020-08-06 このテストだと雑すぎるので、気象台の名称までをちゃんと取れるようにする。
# 天気の結果もちゃんと見れるようにする。1日分で良し。改行コードでsplitすれば予報最初の文字列とれるし
station_and_result = [("静岡", "静岡地"), ("東京", "気象庁")]


@pytest.fixture()
def setup_xml_dir(monkeypatch):

    # 本来生成されているxmlが置かれているディレクトリをテスト用のディレクトリに置き換え
    monkeypatch.setattr(
        jma_weekly_weather,
        "JMA_WEEKLY_XMLFILESS_DIR",
        Path(__file__).parent / "./test_weekly_weather_xmls",
    )


@pytest.mark.parametrize("station, kisyodai", station_and_result)
def test_station(setup_xml_dir, station, kisyodai):
    """
    定義済みの地域からxmlをパースして正しく結果を返すかのテスト
    """
    result = jma_weekly_weather.get_weekly_weather(station)
    assert result[0:3] == kisyodai


def test_station_notfound(setup_xml_dir):
    """
    未定義の地域名はNoneを返すかのテスト
    """
    # 例えば北海道は非対応
    result = jma_weekly_weather.get_weekly_weather("北海道")
    assert result == None

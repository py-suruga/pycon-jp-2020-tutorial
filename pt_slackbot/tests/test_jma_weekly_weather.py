# coding:utf-8

from pathlib import Path
from botfunc import jma_weekly_weather
import pytest

# 気象庁xmlから天気予報を呼び出すbot機能のテスト

station_and_result = [("静岡", "静岡地方気象台発表、静岡の週間天気予報です。"), ("東京", "気象庁予報部発表、東京の週間天気予報です。")]


@pytest.fixture()
def setup_xml_dir(monkeypatch):
    """
    # 本来生成されているxmlが置かれているディレクトリをテスト用のディレクトリに置き換え
    """
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
    # 冒頭の文章で生成できているかをテストする（雑ではある）
    assert result.split("\n")[0] == kisyodai


def test_station_notfound(setup_xml_dir):
    """
    未定義の地域名はNoneを返すかのテスト
    """
    # 例えば北海道は非対応
    result = jma_weekly_weather.get_weekly_weather("北海道")
    assert result == ""

# coding:utf-8

from botfunc import jma_weekly_weather
import pytest

# 気象庁xmlから天気予報を呼び出すbot機能のテスト


# TODO:2020/08/05 条件分岐で使う情報を適当に置き換える必要あり
# - 更新日時
# - モジュール側で使うテスト用のxmlファイルを入れたフォルダ
# （ぐらい？


# jma_weekly_weather.get_weekly_weather: 複数の地方を聞いて問題ないか調べる
@pytest.mark.parametrize
def test_station_notfound(monkeypatch):
    # monkeypatch.setattr()
    # ない地方を聞いたらNoneがもどるか
    # assert
    pass


# jma_weekly_weather.get_weekly_weather: 複数の地方を聞いて問題ないか調べる
@pytest.mark.parametrize
def test_station_found(monkeypatch):
    pass


# bot callback自体のテストも書く


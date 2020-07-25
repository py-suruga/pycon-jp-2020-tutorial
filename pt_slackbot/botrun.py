# coding:utf-8
import os
import re
import sys
import json

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

import requests


# Livedoor Weather REST API
# code一覧
# <city title="静岡" id="220010" source="http://weather.livedoor.com/forecast/rss/area/220010.xml"/>
# <city title="網代" id="220020" source="http://weather.livedoor.com/forecast/rss/area/220020.xml"/>
# <city title="三島" id="220030" source="http://weather.livedoor.com/forecast/rss/area/220030.xml"/>
# <city title="浜松" id="220040" source="http://weather.livedoor.com/forecast/rss/area/220040.xml"/>
LD_TENKI_API_ENDPOINT = "http://weather.livedoor.com/forecast/webservice/json/v1"

# 取得する天気のコードとコードの地域名のマップ
LD_TENIKI_CITY_CODE_MAPS = {
    "中部": "220010",
    "伊豆": "220020",
    "東部": "220030",
    "西部": "220040",
}


# Flaskを作ってgunicornで動くようにする
app = Flask(__name__)

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events", app)

# Create a WebClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(slack_bot_token)


# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message_greeting(event_data):
    print("debug:handled function: {}".format(sys._getframe().f_code.co_name))
    print("debug:eventdata:{}".format(event_data))
    message = event_data["event"]

    message_pattern = "^hi.*"

    # subtypeがない場合=普通のメッセージ, 自分自身の内容を取得してもスルーするようにしておく必要がある
    if message.get("subtype") is None and message.get("bot_id") is None:
        # メッセージを適当にTrueで当たるものを探して
        matchobj = re.match(message_pattern, message.get("text"))
        if matchobj:
            print("hi receive")
            # 何かを返す
            channel = message["channel"]
            res_message = "Hi!!! :robot_face:I'm pysurugabot! :mount_fuji: :shrimp::fish:"
            slack_client.chat_postMessage(channel=channel, text=res_message)


@slack_events_adapter.on("message")
def handle_message_greeting_jp(event_data):
    print("debug:handled function: {}".format(sys._getframe().f_code.co_name))
    print("debug:eventdata:{}".format(event_data))
    message = event_data["event"]

    message_pattern = "^こんにちは.*"

    # subtypeがない場合=普通のメッセージ, 自分自身の内容を取得してもスルーするようにしておく必要がある
    if message.get("subtype") is None and message.get("bot_id") is None:
        matchobj = re.match(message_pattern, message.get("text"))
        if matchobj:
            print("hi jp receive")
            channel = message["channel"]
            res_message = "こんにちは！！:robot_face:私はpysurugabotです！賢くなれるように頑張ります！ :mount_fuji::shrimp::fish:"
            slack_client.chat_postMessage(channel=channel, text=res_message)


@slack_events_adapter.on("message")
def tenki(event_data):
    """
    # Livedoor 天気予報をきく
    # shizuokatenki [西部,中部,東部,伊豆,]
    # 今日の天気は ** 気温は**℃です！
    """

    # botが反応する正規表現パターン
    message_pattern = "shizuokatenki\\s(.{2})"

    print("debug:handled function: {}".format(sys._getframe().f_code.co_name))
    print("debug:eventdata:{}".format(event_data))
    message = event_data["event"]

    # subtypeがない場合=普通のメッセージ, 自分自身の内容を取得してもスルーするようにしておく必要がある
    if message.get("subtype") is None and message.get("bot_id") is None:
        # botのパターンとして認識する文字がある場合
        matchobj = re.match(message_pattern, message.get("text"))
        if matchobj:
            # 地域名が存在するか確認する
            city_name = matchobj.group(1)
            if city_name in LD_TENIKI_CITY_CODE_MAPS:
                print("debug:run tenki ")

                # API経由で天気を調べる
                city_code = LD_TENIKI_CITY_CODE_MAPS[matchobj.group(1)]

                payload = {"city": city_code}
                api_response = requests.get(LD_TENKI_API_ENDPOINT, params=payload)
                # http://weather.livedoor.com/forecast/webservice/json/v1?code=220010

                result = api_response.json()
                print("debug:result_obj:{}".format(result))
                # コマンド実行時の今日の天気予報を抽出
                weather_telop = result["forecasts"][0]["telop"]
                weather_temp = result["forecasts"][0]["temperature"]["max"]
                
                if weather_temp is None:
                    res_message = "静岡県{}の今日の天気は {} です！".format(city_name, weather_telop)
                else:
                    res_message = "静岡県{}の今日の天気は {} 気温は{}℃です！".format(city_name, weather_telop, weather_temp["celsius"])
                # メッセージを返す
                channel = message["channel"]
                
                slack_client.chat_postMessage(channel=channel, text=res_message)


# エラー時のイベントのハンドリング
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))


# botアプリを起動する:FlaskサーバーでEvent APIを待機する
if __name__ == "__main__":
    print("run slackbot")
    app.run(port=3000)

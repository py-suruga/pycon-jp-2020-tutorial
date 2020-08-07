# coding:utf-8
import os
import re
import sys
import json

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from botfunc import jma_weekly_weather

# import requests

# これをnamedtuple or dataclassesにする
BOT_FUNCTION_MAPS = [
    (r"^天気予報\s(.{1,4})", jma_weekly_weather),
]

# Flaskを作ってgunicornで動くようにする
app = Flask(__name__)

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events", app)

# Create a WebClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(slack_bot_token)


# TODO:2020-07-25 メッセージイベントのフックを共通関数にして、ワードと関数のセットを用意して、パターンマッチさせる（その方が複数のイベントのフック関数を書かずに済む。
# メッセージのパターンと返答の関数をセットにすれば、返答の関数のテストが可能になる
@slack_events_adapter.on("message")
def handle_message_and_botrun(event_data):

    # TODO:2020/08/05 できればdebugはlogging.debugにしたい。
    print("debug:eventdata:{}".format(event_data))
    message = event_data["event"]

    # subtypeがない場合=普通のメッセージ, botの返答メッセージはスルーする
    if message.get("subtype") is None and message.get("bot_id") is None:

        # 何も返せなかったときのメッセージ
        res_message = "メッセージを返すことができませんでした。"

        # ハンドルするワードパターンとcallするfucntionのリストをみて、
        for handle_map in BOT_FUNCTION_MAPS:
            print(handle_map)
            matchobj = re.match(handle_map[0], message.get("text"))
            if matchobj:
                # ワードパターンと一致するcall_functionを実行して、得られた結果を表示する
                # TODO:2020/08/05 ここの引数をどう入れるかを考える:
                # 引数というかグループ化した結果の文字を取りに行くだけで良いかなと
                bot_result = handle_map[1].bot_callback(matchobj.groups()[0])
                # bot_result = None
                # Noneの場合は返せなかったとして処理（エラーでも良いし、デフォルトの返答不可能機能を使うのも良い）
                if bot_result is None:
                    continue
                else:
                    res_message = bot_result
                    channel = message["channel"]
                    slack_client.chat_postMessage(channel=channel, text=res_message)
                    break


# エラー時のイベントのハンドリング
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))


# botアプリを起動する:FlaskサーバーでEvent APIを待機する
if __name__ == "__main__":
    print("run slackbot")
    app.run(port=3000)

# coding:utf-8
import os
import random
import re

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter


# Flaskを作ってgunicornで動くようにする
app = Flask(__name__)

# Events APIの準備
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events", app)

# Web Client APIの準備
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(slack_bot_token)


GREETING_LIST = [
    ("こんにちは！", ":jp:"),
    ("Hello!", ":us:"),
    ("ニーハオ!", ":cn:"),
]


# wgreet というワードでbotが返答する
BOT_PATTERN = r"^wgreet"


@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]

    # subtypeがない場合=普通のメッセージ/botの返答メッセージには反応させない/ワードパターンが一致
    if (
        message.get("subtype") is None
        and message.get("bot_id") is None
        and re.match(BOT_PATTERN, message.get("text"))
    ):

        greetword, kokki = random.choice(GREETING_LIST)
        channel = message["channel"]
        message = "{}ノアイサツデス :robot_face: 「{}」".format(kokki, greetword)
        slack_client.chat_postMessage(channel=channel, text=message)


# エラー時のイベントのハンドリング
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))


# botアプリを起動する:FlaskサーバーでEvent APIを待機する
if __name__ == "__main__":
    print("run slackbot")
    app.run(port=3000)

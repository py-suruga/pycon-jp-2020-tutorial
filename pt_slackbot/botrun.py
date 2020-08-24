# coding:utf-8
import os

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


# ref:https://github.com/slackapi/python-slack-events-api/blob/main/example/example.py
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]

    # 普通のメッセージかつテキスト内に"hi"がある場合に返答する
    if message.get("subtype") is None and "hi" in message.get("text"):
        channel = message["channel"]
        message = "Hello <@{}>! :tada:".format(message["user"])
        slack_client.chat_postMessage(channel=channel, text=message)


# エラー時のイベントのハンドリング
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))


# botアプリを起動する:FlaskサーバーでEvent APIを待機する
if __name__ == "__main__":
    print("run slackbot")
    app.run(port=3000)

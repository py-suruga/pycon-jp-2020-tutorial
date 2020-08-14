# coding:utf-8
import os
import re

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from botfunc import world_greeting, search_connpass_online

BOT_FUNCTIONS = [
    (r"^wgreet", world_greeting),
    (r"^connpassonline\s(\d{6})", search_connpass_online),
]

# Flaskを作ってgunicornで動くようにする
app = Flask(__name__)

# Events APIの準備
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events", app)

# Web Client APIの準備
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(slack_bot_token)


@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]

    # subtypeがない場合=普通のメッセージ/botの返答メッセージには反応させない
    if message.get("subtype") is None and message.get("bot_id") is None:
        # botが返す結果の入れ物
        bot_result = ""

        # botとして動作させるワードパターンを元にモジュールの決めてある関数を実行する
        for bot_pattern, bot_module in BOT_FUNCTIONS:

            matched_obj = re.match(bot_pattern, message.get("text"))

            if not matched_obj:
                continue

            if matched_obj.groups():
                bot_args = matched_obj.groups()[0]
            else:
                bot_args = None
            bot_result = bot_module.call_function(bot_args)

            # botが何かしら返答をしてくれた場合はその時点で終了
            if bot_result:
                break

        if bot_result:
            res_message = bot_result
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

# coding:utf-8
import os
import re
import logging


from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from botfunc import jma_weekly_weather

logging.basicConfig(level=logging.DEBUG)


# TODO:2020-08-08 これをnamedtuple or dataclassesにするほうがいいかな？
BOT_FUNCTION_MAPS = [
    (r"^tenki\s(.{1,4})", jma_weekly_weather),
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
def handle_message_and_botrun(event_data):

    # TODO:2020/08/05 できればdebugはlogging.debugにしたい。
    logging.debug("eventdata:{}".format(event_data))
    message = event_data["event"]

    # subtypeがない場合=普通のメッセージ, botの返答メッセージはスルーする
    if message.get("subtype") is None and message.get("bot_id") is None:

        # 何も返せなかったときのメッセージ
        bot_result = ""

        # ハンドルするワードパターンとcallするfucntionのリストをみて、
        for bot_pattern, bot_module in BOT_FUNCTION_MAPS:
            logging.debug("try matching bot:{}".format(bot_module))

            matched_obj = re.match(bot_pattern, message.get("text"))
            if not matched_obj:
                continue

            logging.info("matched_obj -> bot!:{}".format(bot_module))

            # TODO:2020/08/05 ここの引数をどう入れるかを考える:引数というかグループ化した結果の文字を取りに行くだけで良いかなと
            bot_result = bot_module.call_function(matched_obj.groups()[0])

            if bot_result is not None:
                break

        # botが見つからない場合の処理=なにも返答しないほうが良いのでは？
        if bot_result is None:
            res_message = "botが見つからずメッセージを返すことができませんでした。"
        else:
            res_message = bot_result
            # botが生成された/生成できない場合は出来なかったというメッセージを返す
            channel = message["channel"]
            slack_client.chat_postMessage(channel=channel, text=res_message)


"""
botの状態

- なにも返答しなくてもいい
- botらしい可能性があるものを調べてあたったらbotが返答
- botらしい可能性があるものを調べて当たらなければ返答しない
"""


# エラー時のイベントのハンドリング
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))


# botアプリを起動する:FlaskサーバーでEvent APIを待機する
if __name__ == "__main__":
    print("run slackbot")
    app.run(port=3000)

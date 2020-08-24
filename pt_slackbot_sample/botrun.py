# coding:utf-8
import os
import re


from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

from botfunc import world_greeting, search_connpass_online, jma_weekly_weather


BOT_FUNCTIONS = [
    (r"^wgreet", world_greeting),
    (r"^connpassonline\s(\d{6})", search_connpass_online),
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
def handle_message_and_botrun(event_data: dict):
    """
    args:
        event_data: SlackEventAdapterから取得するSlackのイベント情報

    Slack Events APIのイベントをハンドリングし、botを実行します。

    各botは botfuncモジュールに同梱し、 ``call_function`` 関数を実装する必要があります。
    """
    # print("debug: eventdata:{}".format(event_data))

    message = event_data["event"]

    # subtypeがない場合=普通のメッセージ かつ botの返答メッセージはスルーする
    if message.get("subtype") is None and message.get("bot_id") is None:

        # botが返す結果の入れ物
        bot_result = ""

        # botとして動作させるワードパターンを元にモジュールの決めてある関数を実行する
        for bot_pattern, bot_module in BOT_FUNCTIONS:
            # print("debug: try matching bot:{}".format(bot_module))

            matched_obj = re.match(bot_pattern, message.get("text"))
            if not matched_obj:
                continue

            print("info: found bot!:{}".format(bot_module))

            # TODO:2020-08-10 この部分は引数を複数取得できる方が理にかなってると思う->**argas
            # チュートリアルでは文字列だけ受け取る

            if matched_obj.groups():
                bot_args = matched_obj.groups()[0]
            else:
                bot_args = ""
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

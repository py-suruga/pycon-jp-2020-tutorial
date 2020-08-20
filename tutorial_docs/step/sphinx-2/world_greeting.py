# coding:utf-8
import random

# 並びは、挨拶, 国旗の絵文字
GREETING_LIST = [
    ("こんにちは！", ":jp:"),
    ("Hello!", ":us:"),
    ("ニーハオ!", ":cn:"),
]


def get_greeting() -> str:
    """
    Returns:
        botに渡す文字列を返します

    挨拶をすると世界の挨拶をランダムに返します。

    対応する挨拶一覧は GREETING_LISTから選びます。
    """
    greetword, kokki = random.choice(GREETING_LIST)
    return "{}ノアイサツデス :robot_face: 「{}」".format(kokki, greetword)


def call_function(arg: str = "") -> str:
    return get_greeting()

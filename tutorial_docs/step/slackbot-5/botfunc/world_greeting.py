# coding:utf-8

import random
from typing import Union

# 並びは、挨拶, 国旗の絵文字
GREETING_LIST = [
    ("こんにちは！", ":jp:"),
    ("Hello!", ":us:"),
    ("ニーハオ!", ":cn:"),
]


# TODO:2020-08-09 個々の引数は**argsにして自由に引数を受け取り、引数の位置で判断しよう
def call_function(match_group: Union[str, None]) -> Union[str, None]:
    """
    botの結果を返すfunction

    挨拶をすると世界の挨拶をランダムに返す
    """
    greetword, kokki = random.choice(GREETING_LIST)
    return "{}ノアイサツデス :robot_face: 「{}」".format(kokki, greetword)

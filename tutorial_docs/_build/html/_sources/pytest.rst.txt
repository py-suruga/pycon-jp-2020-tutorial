================================================================================
PyTest
================================================================================

.. botの実際に機能を関数にして、テストをする。botが返答する部分（Slackとのインターフェイス的な部分）は共通の処理で行えるのが理想、その予定で進める

Slackbotが返す結果をテストできるように、テストケースの導入を行います。

今回はサードパーティのテストツールである PyTest を利用します。PytestはPython標準ライブラリにあるUnittestより簡単にテストの記述が可能です。


pytestコマンドの使い方
================================================================================

pytestはすでにローカル開発環境を用意した段階でインストールされています。 ``pytest`` コマンドを実行することで確認できます。もしコマンドが存在しないというエラーがある場合はpipコマンドでインストールしてください

::

    pip install pytest

pytestを使ったテストケースはpytestコマンドでテストの実行と結果を確認できます。

``-v`` オプションを利用することで、各テストケースの
  - テストを実行する場所の位置指定

- pytestを扱ったテストの書き方

pytestを使ったテストケースの書き方を紹介します。

テストファイルは Pythonのパッケージ内にある ``tests`` モジュールや、``test_**.py``、``**_test.py`` という名前が認識されます。

.. todo:: 実行して失敗した状態からスタート。faild=>pass

テストの失敗
---------------------

まず初めに簡単なテストを作成してみます。

.. todo:: 2020-08-13 hello test的なコードをファイルに作って記載

 .. code-block:: python

  print("hello py")

特徴的な部分としては、 pythonのassert文を使ってテストケースを定義します。

.. note:: Assert式とは 
  Assert文は `assert [真偽判断ができる式]` と書くことで、式が偽となる場合はAssertErrorという例外を発生させます。簡易的なデバッグ用途に扱うことができます。
  https://docs.python.org/ja/3/reference/simple_stmts.html#assert

このテストは失敗します。pytestコマンドで実行してみましょう。

.. todo:: テスト結果を乗せる

失敗すると、どの部分で失敗したかが確認できます。

コード自体のエラーも同時に表示されます。

.. todo:: コード的に例外が発生する内容

.. todo:: 例外を使ったテストもpytest except機能でできるとnoteに記載する ->  with pytest.raises(ValueError):

.. todo:: with構文の説明を乗せる。コンテキストマネージャという、Pyhton側で決められたあるコンテキストをこのブロック内で制御したいときに使う
  - https://docs.python.org/ja/3/reference/datamodel.html#context-managers
  - https://docs.python.org/ja/3/reference/compound_stmts.html#the-with-statement

テスト関数やクラスの一覧を出したい場合は、 -vオプションを使います。

.. todo:: vオプションの結果を乗せる

テストの成功
---------------------

先ほどのサンプルをテストが通るように変更してみましょう

.. todo:: テストが成功する物にする

実行すると 成功した様子が確認できます。

先ほど扱った-vオプションでテスト関数やクラスの一覧も表示できます。

.. todo:: vオプションの結果を乗せる

PyTestの機能
===================================

Pytestはテストで良く扱う＊＊があらかじめ用意されています。これらはpytest

.. todo:: デコレーターを扱うときの簡単な説明を記載する

parametrize
--------------------------------

parametrizeは パラメータを一括で扱える機能です。

テストに入力する値と結果を用意して、複数回同じテストを実行するときに役に立ちます。

- parametrizeを扱った、テストパラメーターの導入 [Parametrizing fixtures and test functions — pytest documentation](https://docs.pytest.org/en/stable/parametrize.html)


- parametrizeでサンプルを書いてみる: リスト>タプルで作ったパラメーターをassert

fixture
------------------

fixtureは テストする機能を実行する前の準備, 終了処理を共通化したいときに利用します。必要なデータの用意や認証情報の設定、終了時に一時的に生成したデータの除去等がよくあるパターンです。

- fixtureによるテストデータの共通化（予定、使わないかも）[pytest fixtures: explicit, modular, scalable — pytest documentation](https://docs.pytest.org/en/stable/fixture.html)

- fixtureでjson(文字列)をロードして、複数のテストを書いてみる（適合する/適合しないレベル）

monkeypatch
----------------------

monkeypatchは pythonのUnittest.mockのような機能です。モックとなるオブジェクトを置き換える際に利用します。

置き換えるオブジェクト自体はテスト専用の機能を使ったオブジェクトではなく、戻り値や挙動が同等なオブジェクトを生成することで機能します。

- monkeypatch: オブジェクトの置き換えを行う: [Monkeypatching/mocking modules and environments — pytest documentation](https://docs.pytest.org/en/latest/monkeypatch.html)

  - monkeypatch: 公式にあるホームを返す機能を元にテストをしてみる -> https://docs.pytest.org/en/latest/monkeypatch.html#simple-example-monkeypatching-functions


SlackBotのテストケースを書いてみよう
======================================================================

チュートリアルで作成しているSlackbotのテストを書いてみましょう。

SlackbotはSlackワークスペースとの連携が必要になりますが、このテストはそういった外部サービスとの連携テストを想定していません。botとして返答する情報が正しいかの単体テストを作成します。

- 挨拶bot: 各国の挨拶を正しく返すかのテスト
- connpass bot: jsonの取得をmonkeypatchで置き換え
- 気象庁xmlの取得をmonkeypatchで置き換え、parametarizeで地域の追加
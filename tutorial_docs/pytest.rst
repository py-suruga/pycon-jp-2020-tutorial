================================================================================
PyTestでテストケースを導入する
================================================================================

Slackbotが返す結果をテストできるように、テストケースの導入を行います。

今回はサードパーティのテストツールである PyTest を利用します。PytestはPython標準ライブラリにあるUnittestより簡単にテストの記述が可能です。

`pytest: helps you write better programs — pytest documentation <https://docs.pytest.org/en/stable/>`_

pytestコマンドの使い方
================================================================================

pytestはすでにローカル開発環境を用意した段階でインストールされています。 ``pytest`` コマンドを実行することで確認できます。もしコマンドが存在しないというエラーがある場合はpipコマンドでインストールしてください

::

    pip install pytest

pytestを使ったテストケースは ``pytest`` コマンドでテストの実行と結果を確認できます。

まず初めに簡単なテストを作成して、テストの失敗と成功の様子を確認します。

テストの失敗
---------------------

.. literalinclude:: ./step/pytest-0/test_hello_pytest_1.py


特徴的な部分としては、 pythonのassert文を使ってテストケースを定義します。

.. note:: Assert式とは 
  Assert文は `assert [真偽判断ができる式]` と書くことで、式が偽となる場合はAssertErrorという例外を発生させます。簡易的なデバッグ用途に扱うことができます。
  https://docs.python.org/ja/3/reference/simple_stmts.html#assert

このテストは失敗します。pytestコマンドで実行してみましょう。

::

  PS C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\tutorial_docs> pytest .\step\pytest-0\test_hello_pytest.py
  ============================================================= test session starts =============================================================
  platform win32 -- Python 3.7.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
  rootdir: C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\tutorial_docs
  collected 1 item                                                                                                                                

  step\pytest-0\test_hello_pytest.py F                                                                                                     [100%]

  ================================================================== FAILURES =================================================================== 
  _________________________________________________________________ test_pytest _________________________________________________________________ 

      def test_pytest():
  >       assert 1 == 0
  E       assert 1 == 0

  step\pytest-0\test_hello_pytest.py:2: AssertionError
  =========================================================== short test summary info =========================================================== 
  FAILED step/pytest-0/test_hello_pytest.py::test_pytest - assert 1 == 0
  ============================================================== 1 failed in 0.11s ============================================================== 

失敗すると、どの部分で失敗したかが確認できます。

コード自体のエラーも同時に表示されます。


.. literalinclude:: ./step/pytest-0/test_hello_pytest_2.py

::

  PS C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\tutorial_docs> pytest .\step\pytest-0\test_hello_pytest_2.py
  ============================================================= test session starts =============================================================
  platform win32 -- Python 3.7.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
  rootdir: C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\tutorial_docs
  collected 1 item                                                                                                                                

  step\pytest-0\test_hello_pytest_2.py F                                                                                                   [100%]

  ================================================================== FAILURES =================================================================== 
  _________________________________________________________________ test_pytest _________________________________________________________________ 

      def test_pytest():

  >       test_val = 1 / 0
  E       ZeroDivisionError: division by zero

  step\pytest-0\test_hello_pytest_2.py:3: ZeroDivisionError
  =========================================================== short test summary info =========================================================== 
  FAILED step/pytest-0/test_hello_pytest_2.py::test_pytest - ZeroDivisionError: division by zero
  ============================================================== 1 failed in 0.14s ============================================================== 

テストの成功
---------------------

先ほどのサンプルをテストが通るように変更してみましょう


.. literalinclude:: ./step/pytest-0/test_hello_pytest_3.py

実行すると 成功した様子が確認できます。

::

  PS C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\tutorial_docs> pytest .\step\pytest-0\test_hello_pytest_3.py
  ============================================================= test session starts =============================================================
  platform win32 -- Python 3.7.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
  rootdir: C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\tutorial_docs
  collected 1 item                                                                                                                                

  step\pytest-0\test_hello_pytest_3.py .                                                                                                   [100%]

  ============================================================== 1 passed in 0.03s ==============================================================

pytestは ``-v`` オプションでテスト関数やクラスの一覧も表示できます。

::

  PS C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\tutorial_docs> pytest .\step\pytest-0\test_hello_pytest_3.py -v
  ============================================================= test session starts =============================================================
  platform win32 -- Python 3.7.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- c:\users\hiroshi\documents\workspace\personal\pycon-jp-2020-tutorial\.venv\scripts\python.exe
  cachedir: .pytest_cache
  rootdir: C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\tutorial_docs
  collected 1 item

  step/pytest-0/test_hello_pytest_3.py::test_pytest PASSED                                                                                 [100%]

  ============================================================== 1 passed in 0.09s ============================================================== 


PyTestの機能
===================================

Pytestはテストで良く扱う＊＊があらかじめ用意されています。これらはpytest

.. todo:: デコレーターを扱うときの簡単な説明を記載する

parametrize
--------------------------------

parametrizeは パラメータを一括で扱える機能です。

テストに入力する値と結果を用意して、複数回同じテストを実行するときに役に立ちます。

`Parametrizing fixtures and test functions — pytest documentation <https://docs.pytest.org/en/stable/parametrize.html>`_

.. todo:: parametrizeでサンプルを書いてみる: リスト>タプルで作ったパラメーターをassert

fixture
------------------

fixtureは テストする機能を実行する前の準備, 終了処理を共通化したいときに利用します。必要なデータの用意や認証情報の設定、終了時に一時的に生成したデータの除去等がよくあるパターンです。

`pytest fixtures: explicit, modular, scalable — pytest documentation <https://docs.pytest.org/en/stable/fixture.html>`_

.. todo:: fixtureでjson(文字列)をロードして、複数のテストを書いてみる（適合する/適合しないレベル）

monkeypatch
----------------------

monkeypatchは pythonのUnittest.mockのような機能です。モックとなるオブジェクトを置き換える際に利用します。

置き換えるオブジェクト自体はテスト専用の機能を使ったオブジェクトではなく、戻り値や挙動が同等なオブジェクトを生成することで機能します。

`Monkeypatching/mocking modules and environments — pytest documentation <https://docs.pytest.org/en/latest/monkeypatch.html>`_

.. todo:: monkeypatch: 公式にあるホームを返す機能を元にテストをしてみる
  -> https://docs.pytest.org/en/latest/monkeypatch.html#simple-example-monkeypatching-functions


SlackBotのテストケースを書いてみよう
======================================================================

チュートリアルで作成しているSlackbotのテストを書いてみましょう。

SlackbotはSlackワークスペースとの連携が必要になりますが、このテストはそういった外部サービスとの連携テストを想定していません。botとして返答する情報が正しいかの単体テストを作成します。

- 挨拶bot: 各国の挨拶を正しく返すかのテスト
- connpass bot: jsonの取得をmonkeypatchで置き換え
- 気象庁xmlの取得をmonkeypatchで置き換え、parametarizeで地域の追加
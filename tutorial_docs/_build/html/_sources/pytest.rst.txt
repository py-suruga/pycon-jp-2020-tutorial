================================================================================
pytestでテストケースを導入する
================================================================================

Slackbotが返す結果をテストできるように、テストケースの導入を行います。

今回はサードパーティのテストツールであるpytestを利用します。PytestはPython標準ライブラリにあるUnittestより簡単にテストの記述が可能です。

`pytest: helps you write better programs — pytest documentation <https://docs.pytest.org/en/stable/>`_

pytestコマンドの使い方
================================================================================

pytestはすでにローカル開発環境を用意した段階でインストールされています。 ``pytest`` コマンドを実行することで確認できます。もしコマンドが存在しないというエラーがある場合はpipコマンドでインストールしてください

::

    (.venv)> pip install -U pytest

pytestを使ったテストケースは ``pytest`` コマンドでテストの実行と結果を確認できます。

まず初めに簡単なテストを作成して、テストの失敗と成功の様子を確認します。

テストの失敗
---------------------

.. literalinclude:: ./step/pytest-1/test_hello_pytest_1.py


特徴的な部分としては、 pythonのassert文を使ってテストケースを定義します。

.. note::
  Assert文は `assert [真偽判断ができる式]` と書くことで、式が偽となる場合はAssertErrorという例外を発生させます。簡易的なデバッグ用途に扱うことができます。
  https://docs.python.org/ja/3/reference/simple_stmts.html#assert

このテストは失敗します。pytestコマンドで実行してみましょう。

::

  # Windows 10の場合
  (.venv)tutorial_docs> pytest .\step\pytest-1\test_hello_pytest.py

  # macOSの場合
  (.venv)tutorial_docs& pytest ./step/pytest-1/test_hello_pytest.py

  # テスト結果はWindows 10の例
  ============================================================= test session starts =============================================================
  platform win32 -- Python 3.7.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
  rootdir: C:\Users\hiroshi\Documents\pycon-jp-2020-tutorial\tutorial_docs
  collected 1 item

  step\pytest-1\test_hello_pytest.py F                                                                                                     [100%]

  ================================================================== FAILURES ===================================================================
  _________________________________________________________________ test_pytest _________________________________________________________________

      def test_pytest():
  >       assert 1 == 0
  E       assert 1 == 0

  step\pytest-1\test_hello_pytest.py:2: AssertionError
  =========================================================== short test summary info ===========================================================
  FAILED step/pytest-1/test_hello_pytest.py::test_pytest - assert 1 == 0
  ============================================================== 1 failed in 0.11s ==============================================================

失敗すると、どの部分で失敗したかが確認できます。

コード自体のエラーも同時に表示されます。


.. literalinclude:: ./step/pytest-1/test_hello_pytest_2.py

::


  # Windows 10の場合
  (.venv)tutorial_docs> pytest .\step\pytest-1\test_hello_pytest_2.py

  # macOSの場合
  (.venv)tutorial_docs& pytest ./step/pytest-1/test_hello_pytest_2.py

  # テスト結果はWindows 10の例
  ============================================================= test session starts =============================================================
  platform win32 -- Python 3.7.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
  rootdir: C:\Users\hiroshi\Documents\pycon-jp-2020-tutorial\tutorial_docs
  collected 1 item

  step\pytest-1\test_hello_pytest_2.py F                                                                                                   [100%]

  ================================================================== FAILURES ===================================================================
  _________________________________________________________________ test_pytest _________________________________________________________________

      def test_pytest():

  >       test_val = 1 / 0
  E       ZeroDivisionError: division by zero

  step\pytest-1\test_hello_pytest_2.py:3: ZeroDivisionError
  =========================================================== short test summary info ===========================================================
  FAILED step/pytest-1/test_hello_pytest_2.py::test_pytest - ZeroDivisionError: division by zero
  ============================================================== 1 failed in 0.14s ==============================================================

テストの成功
---------------------

先ほどのサンプルをテストが通るように変更してみましょう


.. literalinclude:: ./step/pytest-1/test_hello_pytest_3.py

実行すると成功した様子が確認できます。

::

  # Windows 10の場合
  (.venv)tutorial_docs> pytest .\step\pytest-1\test_hello_pytest_3.py

  # macOSの場合
  (.venv)tutorial_docs& pytest ./step/pytest-1/test_hello_pytest_3.py

  # テスト結果はWindows 10の例
  ============================================================= test session starts =============================================================
  platform win32 -- Python 3.7.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
  rootdir: C:\Users\hiroshi\Documents\pycon-jp-2020-tutorial\tutorial_docs
  collected 1 item

  step\pytest-1\test_hello_pytest_3.py .                                                                                                   [100%]

  ============================================================== 1 passed in 0.03s ==============================================================

pytestは ``-v`` オプションでテスト関数やクラスの一覧も表示できます。

::

  # Windows 10の場合
  (.venv)tutorial_docs> pytest -v .\step\pytest-1\test_hello_pytest_3.py

  # macOSの場合
  (.venv)tutorial_docs& pytest -v ./step/pytest-1/test_hello_pytest_3.py

  # テスト結果はWindows 10の例
  ============================================================= test session starts =============================================================
  platform win32 -- Python 3.7.3, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- c:\users\hiroshi\documents\pycon-jp-2020-tutorial\.venv\scripts\python.exe
  cachedir: .pytest_cache
  rootdir: C:\Users\hiroshi\Documents\pycon-jp-2020-tutorial\tutorial_docs
  collected 1 item

  step/pytest-1/test_hello_pytest_3.py::test_pytest PASSED                                                                                 [100%]

  ============================================================== 1 passed in 0.09s ==============================================================

.. note::
  pytestコマンドのオプションは様々な物があります。 例えば `-rA` は すべてのテスト結果のショートサマリーが見れます。テスト結果とテストの失敗やエラー情報がテストごとに1～2行で表されます。

  ::

    (.venv) \step\pytest-1> pytest -ra

    # テスト結果を割愛して最後のショートサマリの箇所を引用

    ================================================================= short test summary info ==================================================================
    PASSED test_fixture_load_json.py::test_check_val1
    PASSED test_fixture_load_json.py::test_check_val2
    PASSED test_hello_pytest_3.py::test_pytest
    PASSED test_monkeypatch_function.py::test_getssh
    PASSED test_parametrize.py::test_eval[3+5-8]
    PASSED test_parametrize.py::test_eval[2+4-6]
    FAILED test_hello_pytest_1.py::test_pytest - assert 1 == 2
    FAILED test_hello_pytest_2.py::test_pytest - ZeroDivisionError: division by zero
    FAILED test_parametrize.py::test_eval[6*9-42] - AssertionError: assert 54 == 42

  `Usage and Invocations — pytest documentation <https://docs.pytest.org/en/stable/usage.html#detailed-summary-report>`_

pytestの機能
===================================

Pytestはテストで良く扱う機能があらかじめ用意されています。チュートリアル内では3つの機能に絞って説明します。

.. note:: pytestで利用する機能はデコレーターでテスト関数やメソッドに適応します。
  デコレーターは糖衣関数と呼ばれる構文の1つです。既存の関数をオーバーラップして機能を追加するなど変化を与えることができます。

  ref: https://docs.python.org/ja/3/glossary.html#term-decorator


parametrize
--------------------------------

parametrizeはパラメーターを一括で扱える機能です。

テストに入力する値と結果を用意して、複数回同じテストを実行するときに役に立ちます。

`Parametrizing fixtures and test functions — pytest documentation <https://docs.pytest.org/en/stable/parametrize.html>`_

.. literalinclude:: ./step/pytest-1/test_parametrize.py

fixture
------------------

fixtureはテストする機能を実行する前の準備や終了処理を共通化したいときに利用します。必要なデータの用意や認証情報の設定、終了時に一時的に生成したデータの除去がよくあるパターンです。

`pytest fixtures: explicit, modular, scalable — pytest documentation <https://docs.pytest.org/en/stable/fixture.html>`_

.. literalinclude:: ./step/pytest-1/test_fixture_load_json.py

monkeypatch
----------------------

monkeypatchはpythonのUnittest.mockのような機能です。モックとなるオブジェクトを置き換える際に利用します。

置き換えるオブジェクト自体はテスト専用の機能を使ったオブジェクトではなく、戻り値や挙動が同等なオブジェクトを生成することで機能します。

公式の冒頭にあるサンプルコードを動かしてみましょう

.. literalinclude:: ./step/pytest-1/test_monkeypatch_function.py


pytestコマンドは自動的にテストファイルを探す
======================================================================

またpytestは自動的にテストとして実行可能なファイルを探します。プロジェクトのディレクトリ上でpytestコマンドを実行させるだけで簡単にテストの実行が出来ます。

``./tutorial_docs/step/pytest-1`` というディレクトリに上記までに扱ったテストファイルがありますが、ここではディレクトリにカレントディレクトリを移動させてpytestの実行をしてみましょう。

::


  # Windows 10の場合
  (.venv) tutorial_docs> cd .\tutorial_docs\step\pytest-1
  (.venv) pytest-1> pytest

  # macOSの場合
  (.venv) tutorial_docs$ cd ./tutorial_docs/step/pytest-1
  (.venv) pytest-1$ pytest


上記までの説明で利用したテストファイルが実行されます。成功、失敗するテストがいくつかあるか確認してみましょう。

確認が終わったら、 cdコマンドでtutorial_docsディレクトリまで移動してください。

::

  # Windows 10の場合
  (.venv) pytest-1> cd ..\..\..\
  (.venv) tutorial_docs>

  # macOSの場合
  (.venv) pytest-1$ cd ../../../
  (.venv) tutorial_docs$

休憩3🧘‍♂️
===============

pytestの基本的なコーディングと、便利な機能を紹介しました。情報量も多かったと思うので、このあたりで休憩しましょう。

おやつも良いのですが、一日中座りっぱなしも体に良くないです。立ち上がって背伸びをするなどストレッチをしましょう！🧘‍♂️


SlackBotのテストケースを書いてみよう
======================================================================

チュートリアルで作成しているSlackbotのテストを書いてみましょう。

SlackbotはSlackワークスペースとの連携が必要になりますが、このテストはそういった外部サービスとの連携テストを想定していません。botとして返答する情報が正しいかの単体テストを作成します。


下準備
-------------

- ``pt_slackbot`` ディレクトリ内に ``tests`` ディレクトリを作成します(作成はVS Codeやターミナル経由でも良いです）
- ``tests`` ディレクトリに ``__init__.py``　ファイルを作成します。これによりpytestはtestsディレクトリをテストが入っているディレクトリとして認識します

各botのテストケースについて
---------------------------------------

- 挨拶bot: ランダムな返答をする関数をmonkeypatchで置き換える
- connpass bot: jsonの取得をmonkeypatchで置き換え
- 天気bot: 気象庁xmlの取得をmonkeypatchで置き換え、parametarizeで地域の追加

この章で使う資料は以下のURL（パス）から参照できます。

`pycon-jp-2020-tutorial/tutorial_docs/step/pytest-2 <https://github.com/py-suruga/pycon-jp-2020-tutorial/tree/master/tutorial_docs/step/pytest-2>`_

休憩4🍪☕
===============

pytestを使ってbotのテストケースを作成しました。テストを作成することで作成や変更したコードに対しての信頼性を持たせることが出来ます。次は、Sphinxを使いドキュメントを作成します。

この辺で休憩です。そろそろコーヒーかお茶が飲みたい頃ですね。用意しておきましょう☕

.. image:: ./doc-img/oyatu-2.jpg
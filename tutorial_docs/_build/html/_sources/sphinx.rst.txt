================================================================================
Sphinxでドキュメントを書こう
================================================================================

SphinxはPythonの公式ドキュメントやサードパーティライブラリ、またほかの言語や書籍にも利用されるドキュメンテーションツールです。HTMLやPDFでドキュメントを生成できます。

公式サイト: `Overview — Sphinx 4.0.0+ documentation <https://www.sphinx-doc.org/en/master/>`_

日本語版の公式サイト: `概要 — Sphinx 4.0.0+/ba0e5d0ec ドキュメント <https://www.sphinx-doc.org/ja/master/>`_

Sphinxはドキュメントの書きやすさや豊富な拡張、テーマが利用できます。オープンソースプロジェクトのドキュメントや、企業内のドキュメントでも利用されています。

今回はSlackbotのドキュメントを作りましょう。以下のドキュメントの作成を体験します。

- Slackbotの使い方ドキュメントを用意する
- autodoc拡張機能を使って、bot関数のリファレンスを作成する

Sphinxの始め方
============================

Sphinxもローカル開発環境を作成した段階でインストールされています。もし ``sphinx-quickstart`` というコマンドが見つからない場合はpipコマンドでインストールします。

::

    (.venv)> pip install -U Sphinx

Sphinxはドキュメントを作成するひな形の環境を用意する ``sphinx-quickstart`` コマンドがあります。こちらを利用してひな形を作りましょう

.. code-block:: none

    # Windows10の例

    (.venv) pycon-jp-2020-tutorial> cd pt_slackbot
    \pt_slackbot> sphinx-quickstart.exe .\docs\

    # macOSの例

    (.venv) pycon-jp-2020-tutorial$ cd pt_slackbot
    pt_slackbot> sphinx-quickstart ./docs/

    # 以下Windowsの実行例

    Welcome to the Sphinx 3.1.2 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Selected root path: .\docs\

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]: n

    The project name will occur in several places in the built documentation.
    > Project name: pt_slackbot ドキュメント
    > Author name(s): Hiroshi Sano
    > Project release []: 2020.08.30

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
    > Project language [en]: ja

    Creating file C:\Users\hiroshi\Documents\pycon-jp-2020-tutorial\pt_slackboCreating file C:\Users\hiroshi\Documents\pycon-jp-2020-tutorial\pt_slackboCreating file C:\Users\hiroshi\Documents\pycon-jp-2020-tutorial\pt_slackbot\docs\Makefile.
    Creating file C:\Users\hiroshi\Documents\pycon-jp-2020-tutorial\pt_slackbot\docs\make.bat.

    Finished: An initial directory structure has been created.

    You should now populate your master file C:\Users\hiroshi\Documents\pycon-jp-2020-tutorial\pt_slackbot\docs\index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
    make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

    (pycon-jp-2020-tutorial) PS C:\Users\hiroshi\Documents\pycon-jp-2020-tutorial\pt_slackbot> cd .\docs\

今回のSlackbotのドキュメントは以下のような構造で作成します。チュートリアルで利用するディレクトリやファイルに付いて解説します。

::

    .\pt_slackbot\docs
    ├── Makefile # sphinxのドキュメント生成をmakeコマンドで行うときのmakefile
    ├── make.bat # makefileのWindowsバージョン
    ├── _build # ビルドされた結果が入るディレクトリ
    ├── conf.py # Sphinxの設定ファイル
    ├── index.rst # 最初に生成されるrstファイル。HTMLでビルドした場合のindex.html相当


Slackbotのドキュメントを書こう
==============================================================================================

それでは、Slackbotのドキュメントを書きましょう。あらかじめ用意してあるファイルをコピーして説明文を載せていきましょう。

Sphinxではドキュメントの作成に、reStructuredTextというプレーンテキスト形式の軽量マークアップ言語を利用します。短縮名として「reST」とも言われます。

reStructuredTextには、記法やディレクティブという概念があります。記法は見出しやリストやURLリンクなどの文章の装飾や意味合いの定義を付け加えます。ディレクティブも文章の意味合いを定義するものに使いますが、文章を書く上で便利な機能を提供しています。

Sphinxは標準でも多数の記法、ディレクティブに対応しています。またサードパーティが提供する拡張機能も利用できます。

Sphinxはじめの一歩
-------------------------------------

いくつかの記法を利用してindex.rstファイルへ試しに書いてみましょう。

見出し
~~~~~~~~~~

.. code-block:: none

    見出し1
    ==========

    見出し2
    ----------

.. note::
    見出し（セクション）を定義するときのライン（アンダーライン）は "``= - ` : ' " ~ ^ _ * + # < >``" が利用できます。見出しのレベルはアンダーライン記号の出現順で記号自体にレベルの概念はありませんが、Pythonドキュメントの慣例があります。詳しくはsphinxのドキュメントにて

    ref: `reStructuredText入門 — Sphinx 4.0.0+/5ade6b721 ドキュメント <https://www.sphinx-doc.org/ja/master/usage/restructuredtext/basics.html#sections>`_

リンク
~~~~~~~~~~

.. code-block:: none

    `Title <http://link>`_

リスト
~~~~~~~~~~

.. code-block:: none

  - 箇条書きは 「-」

画像
~~~~~~~~~~

.. code-block:: none

    .. image:: path


コードブロック
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

    .. code-block:: python

        >>>print("hello Sphinx!!")


そのほかの記法 : `早わかり reStructuredText — Quick reStructuredText 0.1 documentation <https://quick-restructuredtext.readthedocs.io/en/latest/>`_

ドキュメントの生成
----------------------------------

ドキュメントをhtmlで生成する場合は ``sphinx-quickstart`` コマンドが生成したmakeファイルを使うと簡単に生成できます。

::

    # Windows 10ならmake.bat
    (.venv) pt_slackbot> cd docs
    (.venv) docs> .\make.bat html

    # macOSならmakefileがそのまま扱えます
    (.venv)pt_slackbot$ cd docs
    (.venv)docs$ make html

生成されたhtmlはPythonの簡易httpサーバーを利用してブラウザで確認できます。別のターミナルを開いて実行してください。

::

    # 別のターミナルを開いて実行してください。VS Codeなら「ターミナルの分割」機能が便利です。
    # ポート指定することでhttpサーバーのポートを変更できます。今回は8080版を利用しています。

    # Windows 10
    (.venv) pt_slackbot> cd _build\html
    (.venv) html> python -m http.server 8080

    # macOS
    (.venv) pt_slackbot$ cd _build/html
    (.venv) html& python -m http.server 8080


.. image:: ./doc-img/sphinx_1.png

Windows 10の場合は、ファイヤーウォールの許可が表示されるので、適切な設定をしたうえで許可をしてください。（プライベートネットワークのみにすることをオススメします）

toctreeディレクティブ
--------------------------------------------------------

sphinxはドキュメントの構造を自動的に生成可能なツールです。ドキュメントの目次を作成したいときにはtoctreeディレクティブを利用します。

``index.rst`` には最初からtoctreeディレクティブが自動的に生成されます。

.. code-block:: none

    .. toctree::
        :maxdepth: 2
        :caption: Contents:

        # この行から目次に追加したいrstファイルの名称を追加する


Slackbotの説明文を書いてみよう
--------------------------------------------------------

このチュートリアルで作成しているSlackbotの使い方をドキュメントとして書いてみましょう。

``slackbot_usage.rst`` ファイルを作成して、botの使い方を書いていきます。

こちらの資料を見ながら写経したり、自由に記載してみてください。

`pycon-jp-2020-tutorial/tutorial_docs/step/sphinx-1 <https://github.com/py-suruga/pycon-jp-2020-tutorial/tree/master/tutorial_docs/step/sphinx-1>`_


最後に ``index.rst`` のtoctreeディレクティブに ``slackbot_usage`` を追加します。 rstファイルの拡張子を外したファイル名のみにしてください。

.. code-block:: none

    .. toctree::
        :maxdepth: 2
        :caption: Contents:

        slackbot_usage # .rst の拡張子はつけない


休憩5🍪☕
===============

以上まで、sphinxの環境用意とreStructuredTextの簡単な記法を扱いました。その他にも様々な機能が備わっているので、公式ドキュメントをぜひのぞいてみましょう。

...といっていると頭を使いすぎてしまうと思うので、ここで休憩にします。おやつとコーヒーでリフレッシュしましょう。

.. image:: ./doc-img/oyatu-3.jpg

autodoc拡張機能を使ったAPIリファレンス作成
==============================================================================================

Sphinxには、Pythonのdocstringからクラスや関数の使い方を半自動的にリファレンスとして取り込む、autodoc拡張機能があります。

`sphinx.ext.autodoc -- docstringからのドキュメントの取り込み — Sphinx 4.0.0+/ba0e5d0ec ドキュメント <https://www.sphinx-doc.org/ja/master/usage/extensions/autodoc.html>`_

ここからは、botで定義した関数のリファレンスを作成してみましょう。

docstirngを書こう
---------------------------

autodoc拡張を使うためには、pythonのクラスや関数にdocstringを追加する必要があります。

docstringはPythonのクラスや関数に書き込めるドキュメントです。文字列リテラルという ``"""クオーテーション3つでくくった文字列"""`` で表現します。

.. note::
    docstringはPython公式ドキュメントで厳密な定義があります。

    https://docs.python.org/ja/3/glossary.html?highlight=docstring

docstringの例は以下の通りです。

.. code-block:: python

    >>> def hello_docstring():
    ...     """
    ...     この部分に文字列を入れるとdocstringとして扱われます。
    ...     """
    ...     pass

docstringはPythonのドキュメンテーションに深くかかわる機能です。Python内でも呼び出すことが可能で、help関数を使うことで、関数やクラスのdocstringを参照できます。

.. code-block:: python

    >>> help(hello_docstring)
    Help on function hello_docstring in module __main__:

    hello_docstring()
        この部分に文字列を入れるとdocstringとして扱われます。

docstringのスタイル
----------------------------------------------------

docstringの記述方法にはいくつかのスタイルがあります。標準ではこのようなスタイルになります。

.. code-block:: python

    def search_online_event(ym):
        """
        :param ym: connpassのAPIに渡す ymパラメータ。 yyyymm の6文字で年月を表す
        :type str: str # 文字列
        :returns: botに渡す文字列を返します
        :rtype: str

        request_connpass_apiで受け取ったレスポンスを元にbotに渡す文字列を生成します
        """
        # 以降処理が続く..

この他にも、GoogleやNumpyプロジェクトが提唱するスタイルもあります。それぞれ特徴がありますが、このチュートリアルでは Googleスタイルを扱います。

`GoogleスタイルのPython Docstringsの例 — Sphinx 1.6.7 ドキュメント <https://www.sphinx-doc.org/ja/1.6/ext/example_google.html#example-google>`_

Googleスタイルはシンプルな表現であるため、docstringを最初に書く際にはオススメです。

.. code-block:: python

    def search_online_event(ym):
        """
        Args:
            ym : connpassのAPIに渡す ymパラメータ。 yyyymm の6文字で年月を表す
        Returns:
            botに渡す文字列を返します

        request_connpass_apiで受け取ったレスポンスを元にbotに渡す文字列を生成します
        """
        # 以降処理が続く..


.. note::
    Numpyスタイルの紹介もします。Numpyスタイルは縦に長くなりますが、テキストのみでも読みやすいのが特徴です。

    `NumPyスタイルPython Docstringsの例 — Sphinx 1.6.7 ドキュメント <https://www.sphinx-doc.org/ja/1.6/ext/example_numpy.html#example-numpy>`_

    .. code-block:: python

        def search_online_event(ym):
            """
            Parameters
            ----------
            ym : str
                connpassのAPIに渡す ymパラメータ。 yyyymm の6文字で年月を表す

            Returns
            -------
            str
                botに渡す文字列を返します

            request_connpass_apiで受け取ったレスポンスを元にbotに渡す文字列を生成します
            """
            # 以降処理が続く..

docstringと型アノテーション
----------------------------------------------------

docstringは、もともと関数/メソッドの引数（Args）の説明や戻り値（Returns）等に型の種類を宣言できます。この型宣言自体はPython側に直接影響は有りません（Pythonは動的型定義の言語です）。

しかし予め定義することでPythonに対応したIDEや型チェッカー( `Mypy <https://mypy.readthedocs.io/en/stable/index.html>`_ 等）を使うことで入力補完機能やチェッカーによる警告機能を使うことができます。

.. code-block:: python

    # Googleスタイルです
    def search_online_event(ym):
        """
        Args:
            ym (str): connpassのAPIに渡す ymパラメータ。 yyyymm の6文字で年月を表す
        Returns:
            str: botに渡す文字列を返します

        request_connpass_apiで受け取ったレスポンスを元にbotに渡す文字列を生成します
        """
        # 以降処理が続く..

Python3から型アノテーションという、定義時に型を明言する機能が追加されました。Python3.0から関数の引数や戻り値に対してのアノテーションが扱えます。

`PEP 3107 -- Function Annotations | Python.org <https://www.python.org/dev/peps/pep-3107/>`_

Sphinxの現行バージョンとautodoc拡張は型アノテーションを使うことで、宣言している型の種類を出力できるようになります。

.. code-block:: python

    # Googleスタイルです
    def search_online_event(ym: str) -> str:
        """
        Args:
            ym : connpassのAPIに渡す ymパラメータ。 yyyymm の6文字で年月を表す
        Returns:
            botに渡す文字列を返します

        request_connpass_apiで受け取ったレスポンスを元にbotに渡す文字列を生成します
        """

        # 以降処理が続く..

.. note::
    docstringの標準なスタイルでの型宣言, 型アノテーションを用いた例も紹介します。

    docstringに型宣言もありバージョン

    .. code-block:: python

        def search_online_event(ym):
            """
            :param ym: connpassのAPIに渡す ymパラメータ。 yyyymm の6文字で年月を表す
            :type str: str # 文字列
            :returns: botに渡す文字列を返します
            :rtype: str

            request_connpass_apiで受け取ったレスポンスを元にbotに渡す文字列を生成します
            """
            # 以降処理が続く..

    型アノテーションバージョン

    .. code-block:: python

        def search_online_event(ym: str) -> str:
            """
            :param ym: connpassのAPIに渡す ymパラメータ。 yyyymm の6文字で年月を表す
            :returns: botに渡す文字列を返します

            request_connpass_apiで受け取ったレスポンスを元にbotに渡す文字列を生成します
            """
            # 以降処理が続く..

botの関数にdocstringを用意する
---------------------------------------------------

botの各関数にdocstringを追加しましょう。例として挨拶botとconnpassbotのdocstringを書きます。

- 挨拶bot: ランダムに天気情報を返す関数
- connpassbot: jsonの取得関数、botが答える文字列生成の関数


こちらの資料を見ながら写経しましょう。説明文は自由に変更するのも良いでしょう。

`pycon-jp-2020-tutorial/tutorial_docs/step/sphinx-1 <https://github.com/py-suruga/pycon-jp-2020-tutorial/tree/master/tutorial_docs/step/sphinx-1>`_


.. note:: そのほかの関数は、模範解答からファイルをコピーしましょう。

    - 天気bot: xml取得関数、botが答える文字列生成の関数
    - botrunのメッセージハンドル（botの登録方法を記載する）


Sphinxの設定
---------------------------

autodoc拡張機能はSphinxの設定で有効にする必要があります。Sphinxの設定は ``sphinx-quickstart`` コマンドで作成したひな形にあるconf.pyを変更します。

.. code-block:: python

    # -- Path setup --------------------------------------------------------------

    # If extensions (or modules to document with autodoc) are in another directory,
    # add these directories to sys.path here. If the directory is relative to the
    # documentation root, use os.path.abspath to make it absolute, like shown here.
    #

    # import os
    # import sys

    # sys.path.insert(0, os.path.abspath('.'))

    # TODO:2020-08-15 この部分はsphinx-quickstartで生成されたコードから変更しています。
    # チュートリアル全体でpathlibを扱っているのでpathlibでパスを生成しています。
    from pathlib import Path
    import sys

    sys.path.insert(0, str(Path("../")))

次に、conf.pyのextensions（空のリスト）に、 ``"sphinx.ext.autodoc", "sphinx.ext.napoleon"`` の2つの文字列を追加します。

- ``sphinx.ext.autodoc``: autodoc拡張
- ``sphinx.ext.napoleon``: autodoc拡張でdocstringを扱うときのGoogle/Numpyスタイル対応


.. code-block:: python

    # -- General configuration ---------------------------------------------------

    # Add any Sphinx extension module names here, as strings. They can be
    # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
    # ones.
    # extensions = []
    extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]


autodoc拡張で半自動的にリファレンスを作成する: sphinx-apidocコマンド
------------------------------------------------------------------------------------------------------------------------------

docstringの用意と設定を変更したので、autodoc拡張を使ってリファレンスを生成してみましょう。

.. code-block:: none

    # /testsディレクトリは除外する指定をしています。
    # sphinx-apidoc -f（上書き） -o（出力先ディレクトリの指定） [出力先ディレクトリのパス] [autodocで生成したいPythonモジュールのパス] [除外するパス]

    # 現在位置が、pt_slackbot\docs のはずなので、pt_slackbotのディレクトリに戻ります

    # Windows 10の場合
    (.venv)docs> cd ..\
    (.venv)pt_slackbot> sphinx-apidoc.exe -f -o .\docs .\ .\tests

    # macOSの場合
    (.venv)docs& cd ../
    (.venv)pt_slackbot& sphinx-apidoc -f -o ./docs ./ ./tests

    # 以下に生成の結果が表示される

このコマンドで生成したリファレンスは ``botrun.rst``、``botfunc.rst``、``modules.rst`` の3つのファイルになります。このファイルは ``docs`` ディレクトリ内に生成されます。

.. image:: ./doc-img/sphinx_2.png

最後に、既存のSphinxドキュメントにapidocで生成したリファレンスの目次を追加しましょう。 toctreeディレクティブに ``modules`` を追加します。

.. code-block:: none

    目次
    =======

    .. toctree::
        :maxdepth: 2
        :caption: Contents:

        slackbot_usage
        modules  # 追加したリファレンスの目次

APIリファレンス入のドキュメントを生成する
------------------------------------------------------------------------------------------------------------------------------

sphinx-autodocコマンドでbotの関数にあるdocstringを含むリファレンスを作成しました。sphinxのビルドを行いリファレンスを含むドキュメントを生成しましょう。

.. image:: ./doc-img/sphinx_3.png

toctreeディレクティブに ``modules`` を追加した結果、モジュールの一覧の目次が作成されています。

テーマを変更しよう
=================================

最後に見栄えを自由に変更できるテーマについて説明します。

Sphinxは公式同梱のテーマ以外にも、サードパーティのテーマも充実しています。

今回はドキュメントホスティングサービスとして有名な、Read The Docsが提供しているSphinxテーマである ``sphinx-rtd-theme`` を適用してみましょう。

`Read the Docs Sphinx Theme — Read the Docs Sphinx Theme 0.5.0 documentation <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_

SphixnのテーマはPythonパッケージとして提供されています。

それではテーマを変更してみましょう。方法は公式サイトに掲載されているので、そちらを確認しつつ導入します。

変更すると以下のように、ドキュメントページのデザインが変わります。

.. image:: ./doc-img/sphinx_4.png
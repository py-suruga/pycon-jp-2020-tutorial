================================================================================
Sphinx
================================================================================

SphinxはPythonの公式ドキュメントやサードパーティライブラリ、またほかの言語や書籍にも利用されるドキュメンテーションツールです。

公式サイト: `Overview — Sphinx 4.0.0+ documentation <https://www.sphinx-doc.org/en/master/>`_

日本語版の公式サイト: `概要 — Sphinx 4.0.0+/ba0e5d0ec ドキュメント <https://www.sphinx-doc.org/ja/master/>`_

Sphinxはドキュメントの書きやすさや豊富な拡張、テーマが利用できます。オープンソースプロジェクトのドキュメントや、企業内のドキュメントでも利用されています。

今回はSlackbotのドキュメントを作りましょう。以下のドキュメントの作成を体験します。

- Slackbotの使い方ドキュメントを用意する
- autodoc拡張機能を使って、bot関数のリファレンスを作成する

Sphinxの始め方
============================

- sphinx-quickstartでひな形的なドキュメントの構成を用意する

Sphinxもローカル開発環境を作成した段階でインストールされています。もしsphinx-quickstartというコマンドが見つからない場合はpipコマンドでインストールします。

::

    pip install -U Sphinx

Sphinxはドキュメントを作成するひな形の環境を用意する ``sphinx-quickstart`` コマンドがあります。こちらを利用してひな形を作りましょう

.. code-block::

    (pycon-jp-2020-tutorial) PS C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\pt_slackbot> sphinx-quickstart.exe .\docs\
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
    > Project release []: 2020.07.24

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
    > Project language [en]: ja

    Creating file C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\pt_slackboCreating file C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\pt_slackboCreating file C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\pt_slackbot\docs\Makefile.
    Creating file C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\pt_slackbot\docs\make.bat.

    Finished: An initial directory structure has been created.

    You should now populate your master file C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\pt_slackbot\docs\index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
    make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

    (pycon-jp-2020-tutorial) PS C:\Users\hiroshi\Documents\workspace\personal\pycon-jp-2020-tutorial\pt_slackbot> cd .\docs\

- 用意したドキュメントひな形の紹介: 構造の作り方

今回のSlackbotのドキュメントは以下のような構造で作成します。

.. todo:: ファイルツリーを用意する。ファイルの後に意味をコメントする

Slackbotのドキュメントを書こう
==============================================================================================

それでは、Slackbotのドキュメントを書きましょう。あらかじめ用意してあるファイルをコピーして説明文を載せていきましょう。

Sphinxではドキュメントの作成に、RestructuredTextというプレーンテキスト形式の軽量マークアップ言語を利用します。短縮名として「reST」とも言われます。

RestructuredTextには、記法やディレクティブという概念があります。記法は見出しやリストやURLリンクなどの文章の装飾や意味合いの定義を付け加えます。ディレクティブも文章の意味合いを定義するものに使いますが、文章を書く上で便利な機能を提供しています。

Sphinxは標準でも多数の記法、ディレクティブに対応しています。またサードパーティが提供する拡張機能も利用できます。

Sphinxはじめの一歩
-------------------------------------

いくつかの記法を利用して index.rstファイルに試しに書いてみましょう。

.. todo:: rstの小さいチートシートをここに記載する

    - 見出し
    - リンク
    - リスト
    - コードブロック
    - 画像挿入

そのほかの記法 : `早わかり reStructuredText — Quick reStructuredText 0.1 documentation <https://quick-restructuredtext.readthedocs.io/en/latest/>`_

ドキュメントをhtmlで生成する場合は ``sphinx-quickstart`` コマンドが生成したmakeファイルを使うと簡単に生成できます。

::

    #win10ならmake.bat
    > make.bat html

    #macOSなら makefileがそのまま扱えます
    > make html

生成されたhtmlは pythonの簡易httpサーバーを利用してブラウザで確認できます。

::

    # ポート指定することでhttpサーバーのポートを変更できます。今回は8080版を利用しています。
    > cd _build/html
    > python -m http.server 8080

Windows 10の場合は、ファイヤーウォールの許可が表示されるので、適切な設定をしたうえで許可をしてください。（プライベートネットワークのみにすることをオススメします）

.. todo:: ブラウザの表示した結果をだす


Slackbotの説明文を書いてみよう
--------------------------------------------------------

このチュートリアルで作成しているSlackbotの使い方をドキュメントとして書いてみましょう。

.. todo::
    この章では、tutorial_docsにある文章や画像をコピペして作成してみる。
    入力の手間を減らしたり、ビルド時の失敗をある程度減らす狙いがある

    - 各botの見出し
    - botの簡単な説明: これは自由に決めてもらっても良し
      - 挨拶bot: 対応している国の一覧をリストで用意
      - connpass bot: 検索結果の概要を文章で載せる
      - 天気bot :追加した地域の一覧
    - 画像の挿入: tutorial_docs/slackbotの終盤にある画像ファイルをコピーしてpt_slackbot/docs内にコピー


autodoc拡張機能を使ったAPIリファレンス作成
==============================================================================================

Sphinxには、Pythonのdocstringからクラスや関数の使い方を半自動的にリファレンスとして取り込む、autodoc拡張機能があります。

`sphinx.ext.autodoc -- docstringからのドキュメントの取り込み — Sphinx 4.0.0+/ba0e5d0ec ドキュメント <https://www.sphinx-doc.org/ja/master/usage/extensions/autodoc.html>`_

ここからは、botで定義した関数のリファレンスを作成してみましょう。

docstirngを書こう
---------------------------

autodocを使うためには、pythonのクラスや関数にdocstringを追加する必要があります。

docstringはPythonのクラスや関数に書き込めるドキュメントです。文字列リテラルという ``"""クオーテーション三つでくくった文字列"""`` で表現します。

.. note::
    **docstring**
        クラス、関数、モジュールの最初の式である文字列リテラルです。
        そのスイートの実行時には無視されますが、コンパイラによって識別され、そのクラス、関数、モジュールの __doc__ 属性として保存されます。
        イントロスペクションできる（訳注: 属性として参照できる）ので、オブジェクトのドキュメントを書く標準的な場所です。

    https://docs.python.org/ja/3/glossary.html?highlight=docstring

docstringの例は以下の通りです。

.. code-block:: python

    >>> def hello_docstring():
    ...     """
    ...     この部分に文字列を入れるとdocstringとして扱われます。
    ...     """
    ...     pass
    ...

docstringはPythonのドキュメンテーションに深くかかわる機能です。Python内でも呼び出すことが可能で、help関数を使うことで、関数やクラスのdocstringを参照することができます。

.. code-block:: python

    >>> help(hello_docstring)
    Help on function hello_docstring in module __main__:

    hello_docstring()
        この部分に文字列を入れるとdocstringとして扱われます。


botの関数にdocstringを用意する
---------------------------------------------------

botの各関数にdocstringを追加しましょう。例として挨拶botとconnpassbotのdocstringを書きます。

- 挨拶bot: ランダムに天気情報を返す関数
- connpassbot: jsonの取得関数、botが答える文字列生成の関数

docstringは基本的

.. todo:: そのほかの関数は、終わりに模範解答からコピーして実行して生成された結果を見ていく

    - 天気bot: xml取得関数、botが答える文字列生成の関数
    - botrunのメッセージハンドル（botの登録方法を記載する）

.. todo::

    - noteにtype annotationの組み合わせ例を書く
    - docstringはGoogleスタイルで行うのでnapoleonの導入も必要: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html?highlight=google#type-annotations

Sphinxの設定
---------------------------

autodoc拡張機能はSphinxの設定で有効にする必要があります。Sphinxの設定は sphinx-quickstart コマンドで作成したひな形にあるconf.pyを変更します。

- apidocの設定(conf.pyでextentionsやsys.pathにpythonのモジュールパスを入れる）

autodocで半自動的にリファレンスを作成する: sphinx-apidocコマンド
------------------------------------------------------------------------------------------------------------------------------

docstringの用意と設定を変更したので、autodocを使ってリファレンスを生成してみましょう。

.. todo::
    - sphinx-apidocでapidocのひな形を作成
    - 生成したドキュメントの中身をVSCodeのツリーで見せる


APIリファレンスが入ったドキュメントを生成する
------------------------------------------------------------------------------------------------------------------------------

sphinx-autodocコマンドでbotの関数にあるdocstringを含むリファレンスを作成しました。最後にsphinxのビルドを行いリファレンスを含むドキュメントを生成しましょう。

.. todo::
    make htmlした結果を画像で乗せる


テーマを変更しよう
=================================

最後に見栄えを自由に変更できるテーマについて説明します。

Sphinxは公式同梱のテーマ以外にも、サードパーティのテーマも充実しています。

今回はドキュメントホスティングサービスとして有名な、Read The Docsが提供しているSphinxテーマである ``sphinx-rtd-theme`` を適用してみましょう。

`Read the Docs Sphinx Theme — Read the Docs Sphinx Theme 0.5.0 documentation <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_

SphixnのテーマはPythonパッケージとして提供されています。

それではテーマを変更してみましょう。方法は公式サイトに掲載されているので、そちらを確認しつつ導入します。

変更すると以下のように、ドキュメントページのデザインが変わります。

.. todo:: 変更したページをスクリーンショットで撮影
================================================================================
Sphinx
================================================================================
.. 
    sphinxによるドキュメンテーション: slackbotの使い方と、テストで利用した関数のリファレンスを乗せる予定）
    - sphinxのシステムの紹介: ドキュメントの構造を作る, pythonのdocstringからAPIリファレンス生成できる, プラグイン（扱う予定があれば）

SphinxはPythonの公式ドキュメントやサードパーティライブラリ、またほかの言語や書籍にも利用されるドキュメンテーションツールです。

公式サイト: `Overview — Sphinx 4.0.0+ documentation <https://www.sphinx-doc.org/en/master/>`_

日本語版の公式サイト: `概要 — Sphinx 4.0.0+/ba0e5d0ec ドキュメント <https://www.sphinx-doc.org/ja/master/>`_

Sphinxはドキュメントの書きやすさや豊富な拡張、テーマが利用できます。オープンソースプロジェクトのドキュメントや、企業内のドキュメントでも利用されています。

今回はSlackbotのドキュメントを作りましょう。以下のドキュメントの作成を体験します。

- Slackbotの使い方ドキュメントを用意する
- autodoc拡張機能を使って、bot関数のレファレンスを作成する

Sphinxの始め方
============================

- sphinx-quickstartでひな形的なドキュメントの構成を用意する

Sphinxもローカル開発環境を作成した段階でインストールされています。もしsphinx-quickstartというコマンドが見つからない場合はpipコマンドでインストールします。

::

    pip install -U Sphinx

Sphinxはドキュメントを作成するひな形の環境を用意する ``sphinx-quickstart`` コマンドがあります。こちらを利用してひな形を作りましょう

::

    sphinx-quickstart 
    # この先は実際に動作させた結果を用意する
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

::

    # ファイルツリーを用意する。ファイルの後に意味をコメントする

Slackbotのドキュメントを書こう
==============================================================================================



- ドキュメントの編集: slackbotの使い方についての足らない部分を書いてドキュメントのビルドを行う

  - 挨拶や天気の追加した情報を、各自思いのままに入れてもらう or いくつかパターンを用意する？


autodoc 拡張機能を使ったリファレンス作成
==============================================================================================

- docstringからリファレンスの生成: [sphinx.ext.autodoc -- docstringからのドキュメントの取り込み — Sphinx 4.0.0+/70d521ad9 ドキュメント](https://www.sphinx-doc.org/ja/master/usage/extensions/autodoc.html)


docstirngを書こう
---------------------------
- apidocの設定(conf.pyでextentionsやsys.pathにpythonのモジュールパスを入れる）
- sphinx-apidoc コマンド
- docstringの足らない部分を書いていく
- 挨拶bot: ランダムに天気情報を返す関数
- connpassbot: jsonの取得関数, botが答える文字列生成の関数
- 天気bot: xml取得関数, botが答える文字列生成の関数
- botrunのメッセージハンドル（botの登録方法を記載する）



    - type annotationの組み合わせで行う。(python3.7を必須にしたので問題ないはず）

    - docstringはGoogleスタイルで行うのでnapoleonの導入も必要: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html?highlight=google#type-annotations

autodocで半自動的にリファレンスを作成する
---------------------------------------------------------------

docstringを用意できたので、autodocを使ってリファレンスを生成してみましょう。

::
    - conf.pyを設定
    - sphinx-apidoc でapidocのひな形を作成
    - make htmlで生成しよう

実行したautodocの結果は***にあります。それをslackbotのドキュメントの一部として組み込みます。

テーマを変更しよう
=================================

最後に見栄えを自由に変更できるテーマについて説明します。

Sphinxは公式同梱のテーマ以外にも、サードパーティのテーマも充実しています。

今回はドキュメントホスティングサービスとして有名な、Read The Docsが提供しているSphinxテーマである ``sphinx-rtd-theme`` を適用してみましょう。

`Read the Docs Sphinx Theme — Read the Docs Sphinx Theme 0.5.0 documentation <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_

SphixnのテーマはPythonパッケージとして提供されています。

テーマの変更方法は公式サイトより参考にします


変更すると以下のように、ドキュメントページが大きく変わります。


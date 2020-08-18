================================================
VS CodeとLive Shareの設定
================================================

VS Codeの設定
================================

VS CodeでPythonを扱ったことがない方、はじめてVS Codeを利用する方の設定を説明します。

またLive Shareの設定方法も説明します。

利用する拡張機能
================================

このチュートリアル作成中に利用した拡張機能を紹介します。

- `Python - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
- `reStructuredText - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_


ワークスペースの設定
================================

VS Codeにはワークスペースという概念があります。ディレクトリを開くとそのディレクトリをワークスペースとして認識し、VS Codeのアプリとしての設定（ユーザー設定）とは別に、ワークスペースごとに設定を変更できます。

ワークスペースの設定は ``.vscode/settings.json`` を作成することで有効にできます。

- `Visual Studio Code User and Workspace Settings <https://code.visualstudio.com/docs/getstarted/settings>`_

Python拡張機能で利用できる設定を追加します。リンターやフォーマッターの有効化をしています。``.vscode/settings.json`` に以下の設定を追加します。

.. code-block:: json

  {
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true,
  }

この設定は、いくつかのPythonパッケージの依存があります。これらはpip経由でインストール可能で、 :doc:`/slackbot`  の「ローカル開発環境の用意」の仮想環境作成時にインストールしています。

- `psf/black: The uncompromising Python code formatter <https://github.com/psf/black>`_
- `PyCQA / flake8 · GitLab <https://gitlab.com/pycqa/flake8>`_

Live Shareによるチュートリアルサポート
================================================================

Visual Studio Live Shareは、Visual StudioやVS Codeでソースコードをリアルタイムに複数人で共有、編集しデバッグができます。

`概要 - Visual Studio Live Share - Visual Studio Live Share | Microsoft Docs <https://docs.microsoft.com/ja-jp/visualstudio/liveshare/>`_

チュートリアルでは、各参加者のVS Codeの状況を講師とTAがリアルタイムでコードのデバッグを手助けできます。

この章ではサポートを受けたい方向けに、Live Shareのセットアップ方法を紹介します。

Live Shareは参加者のVS Codeの状況を講師、TAがリアルタイムで見ることができ、操作して共同で作業が可能です。


LiveShare拡張のインストール
--------------------------------------------------------------

ストアからインストールします。

`Live Share - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare>`_

コラボレーションセッションの作成
------------------------------------------------------------

各参加者皆さんのVS Codeで、Live Shareのコラボレーションセッションに講師とTAは参加する必要があります。その時に必要な招待URLを作成していただく必要があります。

Live Share拡張をインストールすると、自動的にWelcomeタブが表示されますが閉じてもらって構いません

VS Codeウィンドウの下部にあるLive Shareマークをクリックして、GitHubアカウントでログインします。

.. image:: ./doc-img/vscode_1.png
.. image:: ./doc-img/vscode_2.png

その後自動的にコラボレーションセッションがスタート、クリップボードへ招待リンク（URL）がコピーされるので、控えてください。

.. image:: ./doc-img/vscode_3.png

最後に講師へURLを伝えてください。伝え方はチュートリアル当日に方法をお伝えします。

URLをブラウザで開くとこのようにブラウザでの参加方法が表示されます。

.. image:: ./doc-img/vscode_4.png

.. todo:: 2020-08-16

  - コラボレーションセッションスタート時にRead-Onlyにして、そのあとに書き込み許可できるか調べてみる
  - 招待リンクの有効期限、コラボレーションセッションがどのぐらいの時間まで有効かを調べる
  - （招待リンクは何度も参加可能かを調べる）

チュートリアル当日の流れ
================================

当日は 8/30 9:30 から環境構築の相談時間を設けます。その時に「セッションの作成」の作業をしてもらい、コラボレーションの招待リンクを伝えてください。


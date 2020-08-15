========================
VSCodeとLive Shareの設定
========================

VS Codeの設定
================================

VS CodeでPythonを扱ったことがない方、初めてVS Codeを利用する方の設定を説明します。

またLive Shareの設定方法も説明します。

利用する拡張機能
================================

このチュートリアル作成中に利用した拡張機能を紹介します。

- `Python - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
- `reStructuredText - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_


ワークスペースの設定
================================

VS Codeにはワークスペースという概念があります。

.. todo:: ワークスペースの公式ヘルプ

Python拡張機能にも専用の設定があり、ワークスペース内で設定を行うことで＊＊＊

``.vscode/settings.json`` に以下の設定を追加します。

.. code-block:: json

  {
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true,
  }

この設定は、いくつかのPythonパッケージの依存があります。これらはpip経由でインストール可能です。

.. todo:: 

- `psf/black: The uncompromising Python code formatter <https://github.com/psf/black>`_
- `PyCQA / flake8 · GitLab <https://gitlab.com/pycqa/flake8>`_


Live Share
================================

Visual Studio Live Shareは、Visual StudioやVS Codeでソースコードをリアルタイムに複数人で共有、編集しデバッグをすることが出来ます

`概要 - Visual Studio Live Share - Visual Studio Live Share | Microsoft Docs <https://docs.microsoft.com/ja-jp/visualstudio/liveshare/>`_

このチュートリアルでは、各参加者のVS Codeの状況を講師, TAがリアルタイムでコードのデバッグを手助けできます。

この章ではサポートを受けたい方向けに、Live Shareのセットアップ方法を紹介します。

.. todo:: 2020-08-10 ここセットアップ記述必要
  - VS CodeとLiveshareについて解説
  - このチュートリアルでどのように利用するかを説明
  - Liveshareが利用できるまでをステップで用意（もしくは公式のリンクのどこまでを行うかを指示する）
  - Live Share拡張インストール
  - 拡張からアカウント登録
  - ゲスト（この場合はレビューを行う講師、TAのこと）を呼ぶ方法
  - 当日の流れ: 当日にセッションを講師TA側に提供する

================================================================================
チュートリアル開始前の準備
================================================================================

この項目は、チュートリアルを行う前に確認や準備する必要がある情報や方法を扱います。

環境の確認
================================================================================

このチュートリアルでは以下のOSをサポートしています。そのほかのOSでは主にPythonのセットアップで違いがあります。

- Windows 10 May 2020 Update :version 2004（チュートリアル作成環境）
- macOS 10.14 Catalina

Pythonのセットアップ
================================================================================

この項目ではPythonのセットアップを扱います。今回のチュートリアルで推奨するPythonのバージョンは3.7以上です。マイナーバージョンもできる限り最新をおすすめします。

Pythonは各OSによってインストール方法が違いますが、基本的にはPython.orgからの公式バイナリインストーラーの利用をお勧めしています。python.jpからダウンロードリンクを元にDLしてください。

`非公式Pythonダウンロードリンク - Python downloads <https://pythonlinks.python.jp/ja/index.html>`_

インストール方法は `環境構築ガイド（python.jp） <https://www.python.jp/install/install.html>`_ を参照ください。

- Win10: `Windows 環境のPython - python.jp <https://www.python.jp/install/windows/index.html>`_
  
  - Windows 10では公式インストーラーの利用をおすすめします

- macOS: `macOS環境のPython - python.jp <https://www.python.jp/install/macos/index.html>`_
  
  - macOSではCatalinaでは標準のpython, または（そのほかのOSバージョンでは）Homebrewというパッケージマネージャを用いてのインストールをおすすめします。

※: そのほかのOSの場合も公式のインストーラーや、OSが提供するパッケージマネージャーからのインストールが利用できます。
kome: Anacondaは今回のチュートリアルはサポートしていません（動作確認しません）

利用するサービスの登録方法
================================================================================

チュートリアルで課題となるSlackbotを作成する上で必須となるサービスや、開発時に利用するサービスの登録が必要になります。

主にSlackのワークスペース, ngrok、Githubアカウントの3つとなります。

GitHUbアカウントは後に開設するVSCode LiveShareでも必要となります。

Slackワークスペースの新規作成
--------------------------------------------------------------------------------

Slackbotを作成するときには、開発用のSlackワークスペースを新規作成することをおすすめします。Slack公式でもアナウンスされています。

`Slack を始める | Slack <https://slack.com/get-started#/create>`_

.. slackワークスペースを作ったほうがいいというアナウンスが入った引用元を記載

ngrokのアカウント作成と利用準備
--------------------------------------------------------------------------------

`ngrok <https://ngrok.com/>`_ とは、ローカルサーバーを一時的に外部公開するプロキシサービスです。SlackBotはコールバックURLが必要となるため、ローカル開発環境で作成したサーバーアプリを一時的にSlack側にアクセスできるようにします。

- 登録: `ngrok - secure introspectable tunnels to localhost <https://dashboard.ngrok.com/signup>`_

登録後は、サーバーを公開する際に利用するCLIツールをインストールします。

ツールのDL先: `ngrok - download <https://ngrok.com/download>`_

zipファイルをDLして、チュートリアルの作業用のディレクトリに配置します。

.. 作業ディレクトリに配置する様子を画像で載せる

Windows 10で ``C:\Users\[Username]\Document\pyconjp-2020-tutorial`` というディレクトリで作業をする場合、DLしたZipファイルをディレクトリ内で展開し、 ``ngrok.exe`` という実行ファイルを配置します。

そのあとに以下のように操作します。

::

  # ngrokのアカウント認証を行い、コマンド経由でサービスへ接続できるようにします。
  >　ngrok.exe authtoken <your_auth_token>

slackbot作成時に作業をするコマンドは、該当のセッションで説明します。

GitHubアカウント作成
--------------------------------------------------------------------------------

Githubアカウントの作成も必須としています。今回操作で利用するエディタであるVSCodeの共有機能LiveShare拡張を利用するときに、アカウントが必要となりますので、こちらも作成します。

`Join GitHub · GitHub <https://github.com/join>`_

エディタの設定:Visual Studio Code
================================================================================

今回利用するエディタであるVisual Studio Code（VSCode）は様々な拡張機能をインストールすることで、便利に扱うことができます。

Python向けの拡張機能もあり、Microsoftが公開しているものやOSSで開発されているものもあります。

このチュートリアル作成中に利用した拡張機能を紹介します。

- `Python - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
- `reStructuredText - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_

.. 
  - python for vscodeだけではなく必要な拡張機能も指示する

Liveshareの設定
------------------------------

..
  - vscodeとLiveshareについて解説
  - このチュートリアルでどのように利用するかを説明
  - Liveshareが利用できるまでをステップで用意（もしくは公式のリンクのどこまでを行うかを指示する）
  
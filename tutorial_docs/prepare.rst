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

この項目ではPythonのセットアップを扱います。チュートリアルで推奨するPythonのバージョンは3.7以上です。マイナーバージョンもできる限り最新をおすすめします。

Pythonは各OSによってインストール方法が違いますが、基本的にはPython.orgからの公式バイナリインストーラーの利用をお勧めしています。python.jpからダウンロードリンクを元にDLしてください。

`非公式Pythonダウンロードリンク - Python downloads <https://pythonlinks.python.jp/ja/index.html>`_

インストール方法は `環境構築ガイド（python.jp） <https://www.python.jp/install/install.html>`_ を参照ください。

- Win10: `Windows 環境のPython - python.jp <https://www.python.jp/install/windows/index.html>`_
  
  - Windows 10では公式インストーラーの利用をおすすめします

- macOS: `macOS環境のPython - python.jp <https://www.python.jp/install/macos/index.html>`_
  
  - macOSではCatalinaでは標準のpython, または（そのほかのOSバージョンでは）Homebrewというパッケージマネージャを用いてのインストールをおすすめします。

※: そのほかのOSの場合も公式のインストーラーや、OSが提供するパッケージマネージャーからのインストールが利用できます。

※: Anacondaはチュートリアルはサポートしていません（動作確認しません）

Pythonの動作確認
--------------------------------------------------------------------------------

pythonコマンドが実行できるか確認します。Windows10ならPowershellかコマンドプロンプト、macOSならターミナルアプリを起動して以下のコマンドを実行しましょう。ここではPowershellを利用して確認します。

TODO:2020-08-13 Python古いので当日までに新しいバージョンにして確認しなおす

::

  PS ...\pycon-jp-2020-tutorial> python --version
  Python 3.7.3


チュートリアル資料を取得する
================================================================================

ＳlackbotチュートリアルはGitHub上のリポジトリで作成しています。以下のURLからDLしてください。

gitリポジトリ: https://github.com/py-suruga/pycon-jp-2020-tutorial.git

リポジトリのZip: https://github.com/py-suruga/pycon-jp-2020-tutorial/archive/master.zip

チュートリアル資料の展開先は、普段お使いのユーザーディレクトリのどこかで構いません。例として 

利用するサービスの準備
================================================================================

チュートリアルで課題となるSlackbotを作成する上で必須となるサービスや、開発時に利用するサービスの登録が必要になります。

主にSlackのワークスペース, ngrok、GitHubアカウントの3つとなります。

GitHubアカウントはオプションとして利用するVSCode Live shareでも利用します。

Slackワークスペースの新規作成
--------------------------------------------------------------------------------

Slackbotを作成するときには、開発用のSlackワークスペースを新規作成することをおすすめします。

`Slack を始める | Slack <https://slack.com/get-started#/create>`_


ngrokの利用準備
--------------------------------------------------------------------------------

`ngrok <https://ngrok.com/>`_ とは、ローカルサーバーを一時的に外部公開するプロキシサービスです。SlackBotはSlackワークスペース上で起きた出来事（メッセージやメンション、リアクションなど、イベントと呼ばれる）をBot側が受け取るURLが必要となるため、ローカル開発環境で作成したサーバーアプリを一時的にSlack側にアクセスできるようにします。

サーバーを公開する際に利用するCLIツールをインストールします。

ツールのDL先: `ngrok - download <https://ngrok.com/download>`_

zipファイルをDLして、チュートリアルの作業用のディレクトリに配置します。

.. image:: ./doc-img/ngrok_1.png


Windows 10で ``C:\Users\[Username]\Document\pyconjp-2020-tutorial`` というディレクトリで作業をする場合、DLしたZipファイルをディレクトリ内で展開し、 ``ngrok.exe`` という実行ファイルを配置します。

ngrokはアカウント作成をしなくても利用することが出来ます。その時には8時間の限定的なURLが割り振られます。チュートリアルでは8時間を超える利用を想定していないのですが、後ほど継続して試したい場合は、ngrokのサービス登録をすることをおススメします。

- 登録: `ngrok - secure introspectable tunnels to localhost <https://dashboard.ngrok.com/signup>`_

登録後は、``ngrok authtoken`` コマンドを使いngrokコマンドのアカウント認証を行うことで、アカウントに紐づいたサービスが利用できます。

詳細: https://ngrok.com/docs#getting-started-authtoken

GitHubアカウント作成
--------------------------------------------------------------------------------

GitHubアカウントの作成も必須としています。

操作で利用するエディタであるVSCodeの共有機能LiveShare拡張を利用するときに、アカウントが必要となりますので、こちらも作成します。

`Join GitHub · GitHub <https://github.com/join>`_

エディタの設定:Visual Studio Code
================================================================================

今回利用するエディタであるVisual Studio Code（VSCode）は様々な拡張機能をインストールすることで、便利に扱うことができます。

Python向けの拡張機能もあり、Microsoftが公開しているものやOSSで開発されているものもあります。

このチュートリアル作成中に利用した拡張機能を紹介します。

- `Python - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
- `reStructuredText - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_

Visual Studio Live Shareの設定
------------------------------

別ページに記載します。

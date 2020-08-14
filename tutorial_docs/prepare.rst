================================================================================
チュートリアル開始前の準備
================================================================================

この項目は、チュートリアルを行う前に確認や準備する必要がある情報や方法を扱います。

環境の確認
================================================================================

このチュートリアルでは以下のOSをサポートしています。そのほかのOSでは主にPythonのセットアップで違いがあります。

- Windows 10 May 2020 Update :version 2004（チュートリアル作成環境）
- macOS 10.15 Catalina

Pythonのセットアップ
================================================================================

この項目ではPythonのセットアップを扱います。チュートリアルで推奨するPythonのバージョンは3.7以上です。マイナーバージョンもできる限り最新をオススメします。

Pythonは各OSによってインストール方法が違いますが、基本的にはPython.orgからの公式バイナリインストーラーの利用をオススメしています。python.jpからダウンロードリンクを元にDLしてください。

`非公式Pythonダウンロードリンク - Python downloads <https://pythonlinks.python.jp/ja/index.html>`_

インストール方法は `環境構築ガイド（python.jp） <https://www.python.jp/install/install.html>`_ を参照ください。

- Win10: `Windows 環境のPython - python.jp <https://www.python.jp/install/windows/index.html>`_
  
  - Windows 10では公式インストーラーの利用をオススメします

- macOS: `macOS環境のPython - python.jp <https://www.python.jp/install/macos/index.html>`_
  
  - macOS Catalinaでは標準のpython, またHomebrewというパッケージマネージャーを用いてのインストールをオススメします。

※: その他OSの場合でも、公式のインストーラーやパッケージマネージャーからのインストールできます。

※: Anacondaについてはサポートしていません（動作確認していません）

Pythonの動作確認
--------------------------------------------------------------------------------

pythonコマンドが実行できるか確認します。Windows 10ならPowerShellかコマンドプロンプト、macOSならターミナルアプリを起動して以下のコマンドを実行しましょう。ここではPowerShellを利用して確認します。

::

  PS pycon-jp-2020-tutorial> python --version
  Python 3.7.8


チュートリアル資料を取得する
================================================================================

SlackbotチュートリアルはGitHub上のリポジトリで作成しています。以下のURLからDLしてください。

gitリポジトリ: https://github.com/py-suruga/pycon-jp-2020-tutorial.git

リポジトリのZip: https://github.com/py-suruga/pycon-jp-2020-tutorial/archive/master.zip

チュートリアル資料の展開先は、普段お使いのユーザーディレクトリのどこかで構いません。

今回のチュートリアルでは ``C:\Users\[Username]\Document\pyconjp-2020-tutorial`` を作業するディレクトリ位置として説明します。

利用するサービスの準備
================================================================================

チュートリアルで課題となるSlackbotを作成する上で必須となるサービスや、開発時に利用するサービスの登録が必要になります。

- Slackワークスペース
- ngrok
- GitHubアカウント

GitHubアカウントはGitHubを扱うときに使うほか、オプションとして利用するVS Code Live shareでも利用します。

Slackワークスペースの新規作成
--------------------------------------------------------------------------------

SlackBotを作成するときには、開発用のSlackワークスペースを新規作成することをオススメします。

`Slack を始める | Slack <https://slack.com/get-started#/create>`_

ngrokの利用準備
--------------------------------------------------------------------------------

`ngrok <https://ngrok.com/>`_ は、ローカルサーバーを一時的に外部公開するプロキシサービスです。

SlackBotはSlackワークスペース上で起きた出来事（メッセージやメンション、リアクションなど、イベントと呼ばれる）を、Bot側で受け取るURLが必要となります。ローカル開発環境で作成したBotアプリを一時的にSlack側からアクセスできるようにします。

サーバーを公開する際に利用するCLIツールをインストールします。

ツールのDL先: `ngrok - download <https://ngrok.com/download>`_

各OS向けのダウンロードリンクからzipファイルをDLして、zipファイル内にある``ngrok.exe`` という実行ファイルをチュートリアルの作業用のディレクトリへ配置します。

.. image:: ./doc-img/ngrok_1.png


.. note:: ngrokはアカウント作成をしなくてもURLを発行できます。その時には8時間の限定的なURLが割り振られます。

  チュートリアルでは8時間を超える利用を想定していないのですが、後ほど継続して試したい場合は、ngrokのサービス登録をすることをおススメします。

  - 登録: `ngrok - secure introspectable tunnels to localhost <https://dashboard.ngrok.com/signup>`_

  登録後は、``ngrok authtoken`` コマンドを使いngrokコマンドのアカウント認証を行うことで、アカウントに紐づいたサービスが利用できます。

  詳細: https://ngrok.com/docs#getting-started-authtoken

GitHubアカウント作成
--------------------------------------------------------------------------------

GitHubアカウントの作成も必須としています。

操作で利用するエディターであるVS Codeの共有機能LiveShare拡張を利用するときに、アカウントが必要となりますので、こちらも作成します。

`Join GitHub · GitHub <https://github.com/join>`_

エディターの設定:Visual Studio Code
================================================================================

今回利用するエディターであるVisual Studio Code（VS Code）はさまざまな拡張機能をインストールすることで、便利に扱うことができます。

Python向けの拡張機能もあり、Microsoftが公開しているものやOSSで開発されているものもあります。

このチュートリアル作成中に利用した拡張機能を紹介します。

- `Python - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
- `reStructuredText - Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_

Visual Studio Live Shareの設定
------------------------------

こちらのページで追記します: :doc:`/vscode_liveshare` 

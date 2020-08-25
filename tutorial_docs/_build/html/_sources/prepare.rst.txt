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

Windows 10の場合は以下のコマンドを実行します。

::

  PS pycon-jp-2020-tutorial> python --version
  Python 3.7.8

macOSの場合は以下のコマンドを実行します。macOS標準のPythonを使用する場合は ``python`` コマンドの代わりに ``python3`` コマンドを使います。

::

  $ python3 --version
  Python 3.8.5

.. note:: pythonコマンドについて

  pythonコマンドは、システム内にPython実行環境が一つのみの場合、その実行環境を利用します。

  しかし、複数のPythonのマイナーバージョンをインストールした場合、OSやインストール方法によって呼び出し方が少し違います。そのため、Pythonを始めようとしたときには、インストールするPythonのバージョンは最新のものを一つのみにすることをオススメします。

  - python2系がある場合はpython2, python3系がある場合はpython3 といったコマンド名で実行できます。
  - （注意: Windowsで公式インストーラー版をインストールした場合、python3コマンドはありません。ですがpython3.exeが実行でき、MicrosoftStore版のインストールをアナウンスされます）

  Windowsの場合はpy.exeというランチャーからシステムにインストールしたpythonのバージョンを指定して起動できます。（インストールの方法によりpy.exeランチャーがインストールされない場合があります）

  `3. Windows で Python を使う — Python 3.8.5 ドキュメント <https://docs.python.org/ja/3/using/windows.html#python-launcher-for-windows>`_

  macOSやLinux系では、マイナーバージョンまで含めたPythonコマンドを実行できます。python3.7 python3.8 といった指定でpythonのバージョンごとに実行が可能です。

チュートリアル資料を取得する
================================================================================

Slackbotチュートリアルは `GitHub上のリポジトリ <https://github.com/py-suruga/pycon-jp-2020-tutorial>`_  を使い作成しています。以下のURLからDLしてください。

- gitリポジトリ: https://github.com/py-suruga/pycon-jp-2020-tutorial.git
- リポジトリのZip: https://github.com/py-suruga/pycon-jp-2020-tutorial/archive/master.zip

チュートリアル資料の展開先は、普段お使いのユーザーディレクトリのどこかで構いません。

今回のチュートリアルでは、Windowsでは ``C:\Users\[Username]\Document\pyconjp-2020-tutorial`` 、macOSでは ``~/document/pyconjp-2020-tutorial`` を作業するディレクトリ位置として説明します。

各ディレクトリ、ファイルの意味
-----------------------------------------------------------

GitHubから取得したチュートリアルの資料には多数のディレクトリがあります。チュートリアルで利用するディレクトリやファイルの意味を解説します。

::

    pycon-jp-2020-tutorial/
    ├── dev_requirements.txt # チュートリアルで利用した開発用のPythonパッケージリスト
    ├── requirements.txt # Slackbotで利用するPythonパッケージリスト
    ├── pt_slackbot # チュートリアルで作成するSlackbotパッケージの置き場所
    ├── pt_slackbot_sample # pt_slackbotの最終完成版。講師が困ったときの資料用です
    └── tutorial_docs # チュートリアルドキュメントの中身
        └── step # チュートリアルで順を追ってハンズオンをするときのステップごとに使う資料

Pythonの仮想環境を用意する
================================================================================

Slackbotを作成するために、Pythonの仮想環境を用意します。

Pythonはシステムにインストールされた実行環境以外の仮想環境を用意できます。仮想環境を作ることでシステム側環境と分離することができます。

仮想環境はWindows 10の場合は以下のコマンドで作成します。

::

  cd C:\Users\[Username]\Document\pyconjp-2020-tutorial
  python -m venv .venv

macOSの場合は以下のコマンドで作成します。ここで仮想環境を作成すると、以後は ``python3`` コマンドの代わりに ``python`` コマンドでPythonを実行できます。

::

  $ cd ~/document/pyconjp-2020-tutorial
  $ python3 -m venv .venv

仮想環境を利用するときには、以下のコマンドを実行します

.. code-block:: none

  # Windows:Powershellで仮想環境を利用する
  > .\.venv\Scripts\activate.ps1

  # Windows:コマンドプロンプトで仮想環境を利用する
  > .\.venv\Scripts\activate.bat

  # macOSで仮想環境を利用する
  $ source .venv/bin/activate

  # 以下Ｗindows, Mac共通
  # 仮想環境上に必要なパッケージをインストールします
  (.venv)> pip install -r requirements.txt

  # Slackbotを開発するときに利用したパッケージのインストールも行います。
  (.venv)> pip install -r dev_requirements.txt

.. note::
  WindowsとPowershellでvenvを利用するときに、activate.ps1（Powershellのスクリプト）を実行するときにはユーザー実行ポリシーの変更が必要になります。この変更は一度変更することでその先は実行する必要はありません。

  以下を実行した後に ``Windows:Powershellで仮想環境を利用する`` の部分を実行してください。

  .. code-block:: none

    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

  参考: `6. サードパーティ製パッケージと venv — Python Boot Camp Text 2016.04.28 ドキュメント <https://pycamp.pycon.jp/textbook/6_venv.html#id12>`_


仮想環境を終了する場合は以下のコマンドを実行します。

.. code-block:: none

  (.venv)> deactivate

.. note::
  このチュートリアルを用意するためにPipenvを利用したので、Pipenvでの環境作成も行えます。
  このハンズオンでは利用しませんが、普段利用されている方はPipfileも同梱しているのでご利用ください。

  `Pipenv: Python Dev Workflow for Humans — pipenv 2020.8.13.dev0 documentation <https://pipenv.pypa.io/en/latest/#install-pipenv-today>`_

.. note::
  Windowsでは利用できませんが、macOSやLinux系ではpyenvという、pythonの複数バージョンを管理するツールがあります。複数バージョンを扱う必要がある場合には便利ですが、Pythonを初めて使う場合には必要とは言えません。

  詳しくはpython.jpの `Pythonのインストール方針 <https://www.python.jp/install/docs/install_plan.html>`_ にて解説されています。


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

SlackBotはSlackワークスペース上で起きた出来事（メッセージやメンション、リアクションなど、イベントと呼ばれる）を、Bot側で受け取るURLが必要となります。ローカルで作成したBotアプリを一時的にSlack側からアクセスできるようにします。

サーバーを公開する際に利用するCLIツールをインストールします。

ツールのDL先: `ngrok - download <https://ngrok.com/download>`_

各OS向けのダウンロードリンクからzipファイルをDLして、zipファイル内にある ``ngrok.exe`` という実行ファイルをチュートリアルの作業用のディレクトリへ配置します。

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

VS CodeとLive Shareの設定
------------------------------

こちらのページで追記します: :doc:`/vscode`

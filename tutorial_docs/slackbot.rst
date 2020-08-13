================================================================================
Slackbotの作成
================================================================================

チュートリアルで扱うSlackbotを実装します。

ローカル開発環境の用意
================================================================================

Slackbotを作成する上

Pythonはシステムにインストールされた実行環境以外の仮想環境を用意できます。仮想環境を作ることでシステム側の環境を汚すこと無く開発環境の構築ができます。

仮想環境は以下のコマンドで作成します

::

  cd C:\Users\[Username]\Document\pyconjp-2020-tutorial
  python -m venv .venv

仮想環境を利用するときには、以下のコマンドを実行します


::

  .\.venv\Scripts\activate.bat
  rem 仮想環境上に必要なパッケージをインストールします
  (.venv) > pip install -r requirements.txt

仮想環境を終了する場合は以下のコマンドを実行します。

::

  (.venv)deactivate

::

    ※:コラム
    Pipenvでの環境作成もできます。このハンズオンでは利用しませんが、普段利用されている方はPipfileも同梱しているのでご利用ください。



Slackアプリの作成と設定
================================================================================

まず初めにBotとなるSlackアプリをSlack上で作成します。

「Create a Slack App」からApp Nameにアプリ名を入力します。

.. image:: ./doc-img/slackbot_1-1.png

Slack WorkSpaceはハンズオン用に新たに取得したワークスペースを利用してください。

アプリが作成できたら、「OAuth & Permissions」の「Scopes」>「Bot Token Scopes」にスコープの設定を行います。

.. image:: ./doc-img/slackbot_1-2.png

「Bot Token Scope」はBotとなるSlackアプリがSlackワークスペースに利用できる権限の範囲（スコープ）です。

この時点では ``chat:write`` のみで、botがSlackへメッセージを送るためのスコープのみを設定していますが、後ほどの設定で、いくつか追加されます。

.. image:: ./doc-img/slackbot_1-3.png

追加したら、ページの上にある「Install App to Workspace」をクリックし、SlackアプリをSlackワークスペースへ追加します。

.. image:: ./doc-img/slackbot_1-4.png

.. image:: ./doc-img/slackbot_1-5.png

追加が終わると、「Bot User OAuth Access Token」が表示されます。このトークンをまず控えてください。

.. image:: ./doc-img/slackbot_1-6.png

次に、右上の「Basic Information」へ戻り、「App Credentials」の中にある「Signing Secret」を控えます。

.. image:: ./doc-img/slackbot_1-7.png


次にngrokコマンドを使い、slackbotを外部公開します。

.. code-block:: bash

    ngrok http 3000
    python ./pt_slackbot/botrun.py

ngrokコマンドを起動すると以下のような情報が表示されます。ngrokのサービスへサインアップしていない場合は外部公開のセッションは8時間の限定公開になります。

.. code-block:: 

  ngrok by @inconshreveable                                                                                                                       (Ctrl+C to quit)
                                                                                                                                                                
  Session Status                online                                                                                                                            
  Session Expires               7 hours, 58 minutes                                                                                                               
  Version                       2.3.35                                                                                                                            
  Region                        United States (us)                                                                                                                
  Web Interface                 http://127.0.0.1:4040                                                                                                             
  Forwarding                    http://df702078ccde.ngrok.io -> http://localhost:3000                                                                             
  Forwarding                    https://df702078ccde.ngrok.io -> http://localhost:3000                                                                            
                                                                                                                                                                  
  Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                       
                                0       0       0.00    0.00    0.00    0.00        

Web InterfaceのURLへアクセスすると、公開したURLのアクセス履歴が見れるようになります。

.. image:: ./doc-img/slackbot_1-8.png


slackbotがSlackワークスペースへのやりとりをおこなうURLを生成したので、Slackアプリの設定を続けます。

Slack Event APIを使い、Slackワークスペース上に起きたイベントを、Slackbotが動作するサーバー(ここではngrokで公開しているローカル環境)へ伝えることができます。

ここで2つの設定を行います。

1. Slack Event APIが起きたイベントをサーバーに伝えるためのエンドポイントURL
2. イベントの種類

Slack Event APIが起きたイベントをサーバーに伝えるためのエンドポイントURLを設定します。

「Event Subscriptions」ページの「Enable Events」にある、右上のボタンをOnにします。

「Request URL」にエンドポイントURLを設定します。ngrokのアプリ上でbotアプリが待機しているアドレスを入力します。

.. image:: ./doc-img/slackbot_1-9.png

:: 
    
    https://[ngrokが自動的に割り振るランダムな文字列].ngrok.io/slack/events

次に、イベントの種類を登録します。イベントには種類があり、あらかじめアプリで取得したいイベントの種類を登録する必要があります。

Slackアプリのスコープを扱ったときに、イベントによるスコープの決定もあると書きましたが、このイベントを登録することでスコープの変化があります。

「Event Subscriptions」の「Subscribe to bot events」内に ``message.channels`` イベントを登録します。

.. image:: ./doc-img/slackbot_1-10.png

登録後はSlackワークスペースへアプリの再インストールを指示されるので行います。

.. image:: ./doc-img/slackbot_1-11.png

再インストール時の認証画面を見ると、権限が追加されていることがわかります。先ほどはチャンネルにメッセージを送信するだけでしたが、それに加えてチャンネル内のメッセージを見ることができます。

.. TODO:2020/08/07 権限追加の画像を取り直す

デプロイとSlackアプリの権限の設定が終わると、Slackbotが利用できます。最後にSlackワークスペース上でbotを呼び出してみます。

最初に、チャンネルにbotユーザーを追加します。

.. image:: ./doc-img/slackbot_1-12-0.png

.. image:: ./doc-img/slackbot_1-12-1.png

ここまででslackbotを動作させる準備が整いました。

slackbotのフロー
---------------------------------------------------------------------------------

ここでは、slackbotがどのようにslackワークスペースとやり取りを行うか解説します。

..
    - slackbotのシステム概要を説明: どんな技術が利用されているか。ざっくりで。(pysuruga-13-handsonの資料流用）

SlackbotはWEBで扱われている技術でサービスとbotのアプリがやり取りを行います。今回のはSlack公式で提供されているEvents APIとWeb APIの二つを利用します。

Events APIはSlack側がbotアプリに声をかけるイメージで、Slackワークスペース内で起きたイベントを伝えます。

Web APIはSlackワークスペースに対して何らかのアクションを起こすために使います。botならbot側が何らかのメッセージを送ります。

PythonではEvents API, Web API どちらとも対応した公式パッケージがあります。今回のチュートリアルではどちらとも利用しています。

- Events API: https://github.com/slackapi/python-slack-events-api
- Web API: https://github.com/slackapi/python-slackclient

チュートリアル中ではどちらとも利用しています。またBotはSlack側からのイベント内容を随時受け取るためにAPIサーバーのような挙動を取ります。そのため、slackeventsapiパッケージをインストールするとFlaskもインストールされます。

Slackbotのコード内ではFlaskのインスタンスを作成して、サーバーとして動作するようになり、Slack側にはエンドポイントURLを教えることで、botがSlackのイベントを知ることができるようになります。

※:コラム

:: 

    SlackのAPIはほかにもあります。incoming webhook（URLにパラメータを付与するとslackワークスペースにメッセージを送れる）, RealTime Messeging API(websocketを利用したリアルタイムにSlackワークスペースとアプリがやり取り可能）が代表例になります。それらについては解説しませんが、参考情報を残します。

    - incoming webhook
    - RTM API

チュートリアルで実装するslackbotについて
================================================================================

このチュートリアルでは、三つのslackbotを実装します。人口無能的な挨拶を返すbotから、APIを利用してインタラクティブな結果を返すようにします。

世界の挨拶を返すbot
--------------------------------------------------------------------------------

.. image:: ./doc-img/slackbot_1-13.jpg

- **wgreet** 挨拶を返すbot:

  - -> 目的:人口無能をまずは試してもらう
  - 国旗、挨拶の言葉、のテーブルを用意してテーブルからランダムに挨拶をかえす
  - 英語、中国、など5つぐらいの言語の挨拶をコメントアウトで用意。参加者に選んで実装してもらう
  - もちろん自由に言葉を変えてもらっても良し

- 挨拶botの実装ステップ

  1. まずslackevetsapiのexampleをそのまま乗せておいて、そのbotで受け答えできるか調べてみる
  2. 次に、その中でテーブルを作って、ランダムで返す関数を用意
  3. 最後に挨拶をかえす部分をモジュール化する -> 伏線:テストとレファレンスを書きやすくする

connpass APIを利用してオンラインイベントを検索するbot
--------------------------------------------------------------------------------

何らかのイベントを開催しようとしたときにイベント運営サービスを利用します。ここではconnpassを例に、connpassが公開している、イベント検索用のREST APIを使ってイベントの検索を行います。

.. image:: ./doc-img/slackbot_1-14.jpg


- **connpass [yyyymm]** connpass API でオンラインイベント検索を行うbot:

  - -> 目的:ITエンジニアに身近なサービス（少なくとも参加者全員知っているはず）で体験する
  - connpass 202008 と打つと、8月のイベントの20件分を取得可能
  - requests + jsonでAPIから取得したjsonのパースを体験する
  - 検索ワードはハードコートしている。検索結果も20件でハードコード

- connpassbotの実装ステップ

  1. 共通化した手法を元に、connpassbotを作る。最初は1関数にすべてのせる
  2. APIリクエストとbotの答えを返す関数を別途作り、分離していく


気象庁のXML電文を使って地域の天気を返すbot
--------------------------------------------------------------------------------

.. image:: ./doc-img/slackbot_1-15.jpg

最後に、よくあるbotで、スマートスピーカーでも尋ねる率が高い機能として天気予報を教えてくれるbotを作りましょう。

今回は誰でも無料で利用可能な、気象庁のXML電文を利用した週間天気予報を返すbotを作ります。XMLを扱うため、XMLのパーサーを使いながら、知りたい地域の週間天気予報を実装しましょう。

- **tenki [地域名]** 気象庁電文XMLを使って週間天気予報を答える天気bot

  -  -> 目的:最後に実用的なbotを作成する
  - 説明的にはxmlのパース周りに絞る（気象庁のサービスとしての話はプログラムの流れ説明の時ぐらいに絞る）
  - requests + bs4を使ってxmlのパースをする
  - 対応地域は絞っておいて（減らしておいて）追加してbotの拡張をしてもらう

- 天気botの実装ステップ

  1. （既にxmlのDLはやっておいた状態）
  2. xmlのパースを進める
================================================================================
PyTest
================================================================================

.. 
    pytestによる、bot機能のユニットテスト: botの実際に機能を関数にして、テストをする。botが返答する部分（Slackとのインターフェイス的な部分）は共通の処理で行えるのが理想、その予定で進める
    - pytestコマンドの使い方
    - pytestを扱ったテストの書き方
    - parametrizeを扱った、テストパラメータの導入 [Parametrizing fixtures and test functions — pytest documentation](https://docs.pytest.org/en/stable/parametrize.html)
    - botのin / outのデータをここで指定することを予定
    - fixtureによるテストデータの共通化（予定、使わないかも）[pytest fixtures: explicit, modular, scalable — pytest documentation](https://docs.pytest.org/en/stable/fixture.html)
    - テストデータの共通化?
    - APIのモックを用意してみる？: 

        - ~~jsonを返すAPIを仮実装して返す。jsonの内容は利用するAPIからとった生データ~~-> この作業は作業量としては重過ぎるし、APIを扱う機能のテストを書くわけではないから不必要
        - もしくは、json.loadsで読み込む部分だけを共通にしてみる（parametrize側でモック用のjsonも指定するとかで）

    - 挨拶bot: 各国の挨拶を正しく返すかのテスト
    - （API利用のテストは、利用APIの負荷を考慮して行わない, モックの検討）-> APIのモックが用意できそうなら考えたい
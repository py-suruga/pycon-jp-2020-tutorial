from botfunc import world_greeting
import pytest


@pytest.fixture()
def setup_non_random(monkeypatch):

    # ランダムで返す結果を固定にする

    pass


@pytest.mark.parametrize()
def test_greeting_result():
    """
    アイサツの文章が決めたとおりに出力されるかを確認
    """

    pass

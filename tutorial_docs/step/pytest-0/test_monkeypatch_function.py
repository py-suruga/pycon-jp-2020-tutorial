# ref:https://docs.pytest.org/en/6.0.1/monkeypatch.html#simple-example-monkeypatching-functions
from pathlib import Path


# テスト対象の関数
def getssh():
    return Path.home() / ".ssh"


# テスト本体
def test_getssh(monkeypatch):
    # 置き換える関数を用意する
    def mockreturn():
        return Path("/abc")

    # pathlib.Pathのhomeメソッドを置き換えます
    monkeypatch.setattr(Path, "home", mockreturn)

    # getssh関数内のpathlib.Path.home -> mockreturnに置き換えて実行されます
    x = getssh()
    assert x == Path("/abc/.ssh")


# ※monkeypathc.setattrで置き換える物は関数でなければいけない（内部でsetattr関数を使っているため）
# ref:https://github.com/pytest-dev/pytest/blob/303030c14130a5777bdaace678b9f4adb07416ab/src/_pytest/monkeypatch.py#L209

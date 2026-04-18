import subprocess

import pytest

from lycoris.utils.system import command_exists, is_root, run


def test_is_root_returns_bool():
    assert isinstance(is_root(), bool)


def test_command_exists_with_existing_command():
    assert command_exists("ls") is True


def test_command_exists_with_missing_command():
    assert command_exists("__comando_que_no_existe__") is False


def test_run_returns_output():
    result = run(["echo", "lycoris"])
    assert result == "lycoris"


def test_run_raises_on_failure():
    with pytest.raises(subprocess.CalledProcessError):
        run(["false"])


def test_run_no_capture_returns_none():
    result = run(["echo", "lycoris"], capture=False)
    assert result is None

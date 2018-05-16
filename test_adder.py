import pytest
from click.testing import CliRunner
from adder import main

@pytest.fixture
def runner():
    return CliRunner()

def test_add(runner):
    result = runner.invoke(main, ['--lhs', 1, '--rhs', 2])
    assert result.exit_code == 0
    assert result.output == '3\n'


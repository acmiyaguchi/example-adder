# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
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


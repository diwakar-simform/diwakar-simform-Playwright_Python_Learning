# Question17: 01:04:55 - How do you apply a custom marker to a test case in pytest?

import pytest

@pytest.mark.sanity
def test_Example():
    assert True
    return True

# to run only the above file you have to use: pytest -m sanity

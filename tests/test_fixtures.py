import pytest


@pytest.mark.check
def test_change_name(user):
    assert user.name == 'Viktor'

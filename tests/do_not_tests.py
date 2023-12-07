"""These tests are failing in several ways on purpose."""

import pytest


def test_will_fail():
    """This test will fail."""
    assert 1 == 2


@pytest.mark.skip()
def test_will_be_skipped():
    """This test will be skipped."""
    assert 1 == 1


@pytest.mark.xfail()
def test_will_fail_as_expected():
    """This test will fail as expected due to its decorator."""
    assert 1 == 2


@pytest.mark.xfail()
def test_will_pass_but_should_fail():
    """This test will pass but should fail due to its decorator."""
    assert 1 == 1

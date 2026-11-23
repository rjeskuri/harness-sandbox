"""stamp() returns a string; each loop smoke ticket pins the exact value it sets."""

from harness_sandbox.stamp import stamp


def test_stamp_is_a_string():
    assert isinstance(stamp(), str)


def test_stamp_is_the_pinned_value():
    assert stamp() == "20261123T124135Z"

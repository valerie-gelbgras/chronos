import pytest

from src.chronos.components import fields

@pytest.mark.parametrize("interval_count, interval_size_in_milliseconds, expected", 
    [(0, 10, '00:00:00.000'),
     (5, 11, '00:00:00.055'),
     (5000, 11, '00:00:55.000')]
)
def test_update_interval(interval_count, interval_size_in_milliseconds, expected):
    actual = fields.update_interval(interval_count, interval_size_in_milliseconds)
    assert expected == actual

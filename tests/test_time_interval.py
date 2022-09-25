# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

import pytest
from src.chronos.time_interval import TimeInterval

def test_initialization():
    time_interval = TimeInterval(hours=1, minutes=2, seconds=3, milliseconds=4)
    assert time_interval.hours == 1
    assert time_interval.minutes == 2
    assert time_interval.seconds == 3
    assert time_interval.milliseconds == 4


def test_negative_hours_must_be_given_as_integer():
    with pytest.raises(TypeError):
        TimeInterval(hours=1.1, minutes=2, seconds=3, milliseconds=4)
        

def test_negative_minutes_must_be_given_as_integer():
    with pytest.raises(TypeError):
        TimeInterval(hours=1, minutes=2.1, seconds=3, milliseconds=4)


def test_positive_seconds_must_be_given_as_integer():
    with pytest.raises(TypeError):
        TimeInterval(hours=1, minutes=2, seconds=3.1, milliseconds=4)


def test_positive_milliseconds_must_be_given_as_integer():
    with pytest.raises(TypeError):
        TimeInterval(hours=1, minutes=2, seconds=3, milliseconds=4.1)


def test_addition_basic():
    t1 = TimeInterval(hours=1, minutes=2, seconds=3, milliseconds=4)
    t2 = TimeInterval(hours=3, minutes=5, seconds=37, milliseconds=54)
    sum = t1 + t2
    assert sum.hours == 4
    assert sum.minutes == 7
    assert sum.seconds == 40
    assert sum.milliseconds == 58


def test_addition_advanced():
    t1 = TimeInterval(hours=1, minutes=2, seconds=43, milliseconds=990)
    t2 = TimeInterval(hours=3, minutes=59, seconds=37, milliseconds=50)
    sum = t1 + t2
    assert sum.hours == 5
    assert sum.minutes == 2
    assert sum.seconds == 21
    assert sum.milliseconds == 40


def test_substraction_basic():
    t1 = TimeInterval(hours=3, minutes=5, seconds=37, milliseconds=50)
    t2 = TimeInterval(hours=1, minutes=2, seconds=3, milliseconds=40)
    difference = t1 - t2
    assert difference.hours == 2
    assert difference.minutes == 3
    assert difference.seconds == 34
    assert difference.milliseconds == 10
    
    
def test_substraction_advanced():
    t1 = TimeInterval(hours=3, minutes=5, seconds=37, milliseconds=40)
    t2 = TimeInterval(hours=1, minutes=29, seconds=43, milliseconds=50)
    difference = t1 - t2
    assert difference.hours == 1
    assert difference.minutes == 35
    assert difference.seconds == 53
    assert difference.milliseconds == 990
    

def test_string_representation():
    t1 = TimeInterval(hours=3, minutes=55, seconds=31, milliseconds=50)
    assert str(t1) == '03:55:31.050'
    
    t2 = TimeInterval(hours=13, minutes=5, seconds=31, milliseconds=980)
    assert str(t2) == '13:05:31.980'
    
    t3 = TimeInterval(hours=3, minutes=55, seconds=1, milliseconds=5)
    assert str(t3) == '03:55:01.005'

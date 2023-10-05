import pytest

from my_stats import my_median


def test_my_median_basic():
    data = [1, 2, 3, 4, 5]
    result = my_median(data)
    assert result == 3

    data = [1, 2, 3, 4, 5, 6]
    result = my_median(data)
    assert result == 3.5

    # test case when median is not equal to mean
    data = [1, 6, 17]
    result = my_median(data)
    assert result == 6

    # test case when data are not sorted
    data = [1, 6, 17, 2, 3]
    result = my_median(data)
    assert result == 3


def test_my_median_empty():
    # if the list is empty, my_median should raise a ValueError exception
    data = []
    with pytest.raises(ValueError) as exc_info:
        my_median(data)
    assert "input_data must not be empty" in str(exc_info.value)


def test_my_median_not_list():
    # if the input_data is not a list of numbers, my_median should raise a ValueError exception
    data = "this is not a list of numbers"
    with pytest.raises(ValueError) as exc_info:
        my_median(data)
    assert "input_data must be a list-like object of numbers" in str(exc_info.value)

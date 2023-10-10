import random
from statistics import median
import pytest

from my_stats.my_stats import my_median


@pytest.fixture
def my_test_dataset():
    return [1, 2, 3, 4, 5, 6]


@pytest.mark.parametrize("data, expected", [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5, 6], 3.5),
    ([1, 6, 17], 6),
    ([1, 6, 17, 2, 3], 3),
])
def test_my_median_basic(data, expected):
    result = my_median(data)
    assert result == expected


def test_my_median_on_my_test_dataset(my_test_dataset):
    result = my_median(my_test_dataset)
    assert result == 3.5


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


def test_my_median_compare_with_math():
    # compare the results of my_median with math.median
    for i in range(100):
        # generate random data
        data = [random.random() for _ in range(random.randint(1, 100))]
        assert my_median(data) == median(data)

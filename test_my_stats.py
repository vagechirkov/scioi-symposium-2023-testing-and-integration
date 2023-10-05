from my_stats import my_median


def test_my_median_basic():
    data = [1, 2, 3, 4, 5]
    assert my_median(data) == 3

    data = [1, 2, 3, 4, 5, 6]
    assert my_median(data) == 3.5

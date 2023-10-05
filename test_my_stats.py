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

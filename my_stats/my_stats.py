def my_median(input_data):
    # make a copy of the list so that the sort does not modify the original list
    # this is a good practice to check the input data
    try:
        my_list = [float(x) for x in input_data]
    except ValueError:
        raise ValueError("input_data must be a list-like object of numbers")

    # if the list is empty, raise a ValueError exception
    if len(my_list) == 0:
        raise ValueError("input_data must not be empty")

    # sort the list
    my_list.sort()
    # get the length of the list
    length = len(my_list)
    # if the length is odd
    if length % 2 == 1:
        # return the middle element
        return my_list[length // 2]
    # if the length is even
    else:
        # return the average of the middle two elements
        return (my_list[length // 2 - 1] + my_list[length // 2]) / 2


def my_mean(my_list):
    raise NotImplementedError


def my_variance(my_list):
    raise NotImplementedError

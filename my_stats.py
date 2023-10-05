def my_median(my_list):
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

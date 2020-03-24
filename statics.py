def mean(arr):
    return sum(arr) / len(arr)


def variance(arr):
    mu = mean(arr)
    counter = 0
    for x in arr:
        counter += (x - mu) ** 2

    return counter / len(arr)


def standard_deviation(arr):
    return variance(arr) ** .5

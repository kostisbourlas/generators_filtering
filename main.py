import itertools


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def chunk(iterable, chunk_size=10):
    for first in iterable:
        yield itertools.chain([first], itertools.islice(iterable, chunk_size - 1))


def filter_even(iterable):
    for item in iterable:
        if item % 2 == 0:
            continue
        yield item


def results():
    for element in my_list:
        yield element


for iterator in chunk(filter_even(results()), 5):
    batch = list(iterator)
    print(batch)

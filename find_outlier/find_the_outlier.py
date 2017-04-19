"""
created on 16/04/2017
author: Amartya Gupta
"""
from collections import Counter as C


def find_outlier(integers):
    tag = ['e', 'o']
    result = [tag[i % 2] for i in integers]
    count_result = C(result)
    index_result = [i for i in count_result if count_result[i] == 1]
    return integers[result.index(index_result[0])]


# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))

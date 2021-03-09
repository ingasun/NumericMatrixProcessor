import numpy as np


def custom_sum(arg1, arg2):
    if type(arg1) == list and type(arg2) == list:
        return 'Both arguments are lists, not arrays'
    elif type(arg1) == list or type(arg2) == list:
        return 'One argument is a list'
    else:
        return arg1 + arg2

# list1 = [1,2,2]
# list2 = [1,2,2]
# array1 = np.array(list1)
# array2 = np.array(list2)
#
# print(custom_sum(array1, list2))
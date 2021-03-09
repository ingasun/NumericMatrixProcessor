# X = [[1,7,5],
#     [4,5,5],
#     [3,3,3]]
# print(len(X[0]))
#
# result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))  ]
#
# for r in result:
#     print(r)
import numpy as np

bla = [['333'], ['222'], ['555']]
#nextbla = bla.split()
#print(nextbla)
list_with_seperated_ints = []
i = 0
for nestlist in bla:
    inner_list = []
    for elem in nestlist:
        for i in elem:
            inner_list.append(i)
        list_with_seperated_ints.append(inner_list)


result = [[list_with_seperated_ints[j][i] for j in range(len(list_with_seperated_ints))] for i in range(len(list_with_seperated_ints[0]))]
print(result)
for elem in result:
    print(*elem, sep=" ")


matrix = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
n_matrix = np.array(matrix)

bla = n_matrix[::-1,::-1].T
print(bla)

for elem in bla:
    print(*elem, sep=" ")
#a = n_matrix.ravel('F')[::-1].reshape(matrix.n_shape)
#print(a)
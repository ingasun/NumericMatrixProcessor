number_string = input()

num_list = [float(num) for num in number_string]
#print(num_list)
summed = sum(num_list)
print(summed / len(num_list))
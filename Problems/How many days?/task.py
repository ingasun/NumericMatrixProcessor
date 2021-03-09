seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
day_list = [int(item // (60 * 60 * 24)) for item in seconds]
print(day_list)

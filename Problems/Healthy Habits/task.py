# the list "walks" is already defined
# your code here
# walks = [
#     {"day": "Monday", "distance": 2000},
#     {"day": "Tuesday", "distance": 3000},
#     {"day": "Wednesday", "distance": 3500},
#     {"day": "Thursday", "distance": 2500},
#     {"day": "Friday", "distance": 2500},
#     {"day": "Saturday", "distance": 1000},
#     {"day": "Sunday", "distance": 5600}]

sum_ = 0
counter = 0
for days in walks:
    for key, value in days.items():
        if key == 'distance':
            sum_ += value
            counter += 1

print(sum_ // counter)

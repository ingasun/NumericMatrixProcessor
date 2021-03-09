# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, ple
marks = OrderedDict(json.loads(input()))

# marks = {"Tom": 98, "Lina": 92, "Natalie": 81}
marks['Max'] = 100
# ordD = OrderedDict(marks)
marks.move_to_end('Max', last=False)
# your code here

print(marks)

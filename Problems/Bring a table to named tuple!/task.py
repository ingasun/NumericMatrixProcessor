from collections import namedtuple

student = namedtuple('Student', ['name', 'age', 'department'])

alina = student('Alina', '22', 'linguistics')
alex = student('Alex', '25', 'programming')
kate = student('Kate', '19', 'art')

print(alina)
print(alex)
print(kate)
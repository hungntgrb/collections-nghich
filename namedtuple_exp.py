from collections import namedtuple

Person = namedtuple('Person', 'name class age age', rename=True)
# print(Person._fields)
# ('name', '_1', 'age', '_3')

Task = namedtuple('Task', ['text', 'done', 'key'])
task1 = Task('Learn Django', False, 'acb321')
print('Task1:', task1)

# Convert to OrderedDict
print('As Dict:', task1._asdict())

# 'Replace' creates a new instance
task2 = task1._replace(text='Learn JavaScript')
print('Task2:', task2)
print('Same? ', task2 is task1)

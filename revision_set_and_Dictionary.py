# disctionary pop, popitem, clear

my_set= {
    'name' : 'vicky',
    'Age' : 17,
    'Marks' : [20,30,20,19,30],
    'percent' : 98.9,
    'pass' : True
}

my_set.pop('Age')
print("pop",my_set)

my_set2 = {
    'name' : 'vicky',
    'Age' : 17,
    'Marks' : [20,30,20,19,30],
    'percent' : 98.9,
    'pass' : True
}
my_set2.popitem()
print("Popitem",my_set2)

my_set3 = {
    'name' : 'vicky',
    'Age' : 17,
    'Marks' : [20,30,20,19,30],
    'percent' : 98.9,
    'pass' : True
}
my_set3.clear()
print("Clear",my_set3)
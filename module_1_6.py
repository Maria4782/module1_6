my_dist= {'Alex':2000, 'Victoria':1999, 'Sindi':2005}
print(my_dist)
print(my_dist['Alex'])
print(my_dist.get('Regina', 'тю-тю'))
my_dist['Maria']= 1989
my_dist['Alina']= 2003
my_dist.update({'Maria':1989, 'Alina':2003})
print(my_dist)
del my_dist['Alex']
print(my_dist)

my_set = {1, 1, 2, 'Груша', 4, 4, 5, False}
print(my_set)
print(my_set.add(6))
print(my_set.add(7))
print(my_set.discard(2))
print(my_set)





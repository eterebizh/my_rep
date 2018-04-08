
# -*- coding: utf-8 -*-
'''
Задание 4.5

Список VLANS это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.

Из списка нужно получить уникальный список VLANов,
отсортированный по возрастанию номеров.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

VLANS = set(VLANS)
print VLANS

my_list = list (VLANS)
my_list.sort()
print "Result using simple set/list conversion:"
print my_list

#The most obvious to solve this is to use recursion
print "Check result using alternate solution:"
output = []

for i in VLANS: 
	if i in output: 
		pass
	else: output.append(i)

output.sort()
print output

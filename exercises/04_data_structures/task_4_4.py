
# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'


array1 = []
array2 = []

array1 = command1.replace ('switchport trunk allowed vlan ', '').strip().split(',')
array2 = command2.replace ('switchport trunk allowed vlan ', '').strip().split(',')

vlans1 = set(array1) #define 'SET1' from 'list'
vlans2 = set(array2) #define 'SET2' from 'list'

array_net = list (vlans1.intersection(vlans2)) # find an intersection of two SETs, create a list out of the result 
print (array_net) # print result

'''
#First solution is to use for-i. Though this violates the rule
that I should use only those topics that i've gone through

list1 = []
vlan1 = []

list2 = []
vlan2 = []

vlancr = []

list1 = command1.strip().split()
vlan1 = list1[-1].split(',')

list2 = command2.strip().split()
vlan2 = list2[-1].split(',')

print vlan1
print vlan2

for i in vlan1:
	if i in vlan2: 
		vlancr.append (i)

print vlancr

'''
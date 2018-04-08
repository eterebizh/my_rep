# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки CONFIG список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100' # <type 'str'>

commands = [] # Create <type 'list'> variable 
vlans = [] # This list is going to store the VLANs

commands = CONFIG.strip().split() 

print (commands)

vlans = commands[-1].split(',') 

'''Pick last entry from the list,
split entries using ',' charecter, output result into vlan 'list' variable
'''

print (vlans)







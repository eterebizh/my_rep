# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import re

def todec(x):
	return int(x,2) # convert binary to decimal

prefix = input ('Please enter IP subnet using a.b.c.d/x format: ')

network, mask = prefix.split('/') # use Multiple variable assignment

array = []
array = network.split ('.') # create an array of decimal octets
array = list(map(int, array)) # fire int () function for each iterable in the list

maskb = "1" * int(mask) + "0" * (32 - int(mask)) # binary representation of mask <'string'>

arraym = [ maskb[0:8], maskb[8:16], maskb[16:24], maskb[24:32] ] # create a list of octets, type 'string'

arrayd = list(map(todec, arraym)) # fire 'todec' function for every iterable in the list 
arraym = list(map(int, arraym)) # fire 'int' function for every iterable in the list 

access_template = ['Network:',
				   '{:<8} {:<8} {:<8} {:<8}',
				   '{:08b} {:08b} {:08b} {:08b}',
				   '\nMask:\n/{}',
				   '{:<8} {:<8} {:<8} {:<8}',
				   '{:08} {:08} {:08} {:08}']

print ('\n' + '-'*30)
print ('\n'.join(access_template).format (
	*array, # an array of octets
	*array, # an array of ofctets; changed to binary through .format()
	mask, # subnet mask, initially get through .split() function
	*arrayd, # decimal representation of the mask
	*arraym)) # binary representation of the mask
print ('\n' + '-'*30)

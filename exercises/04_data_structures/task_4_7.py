
# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


def todec (x):
	return int (x,16) # Return Hex->Dec conversion result

MAC = 'AAAA:BBBB:CCCC'

#0 - adds leading zeroes
#8 - defines a column width
#b - converts integer to boolean  

mylist = []
mylist = MAC.split (':')


mylist = list (map(todec,mylist)) # Map function is fired for each iterable in the list

#array = list(map(int, array)) # convert list components (string->interger)

ip_template = '''
MAC address in boolean notation:
{:08b} {:08b} {:08b}
'''

print (ip_template.format (*mylist)) # Dec to Boolean using format()




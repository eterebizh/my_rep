
# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'

'''
mylist = []
mylist = MAC.split (':')

dec1 = int(mylist[0], 16) # Hex-> Dec
bin1 = bin (dec1) # Dec->Binary

dec2 = int(mylist[1], 16)
bin2 = bin (dec2)

dec3 = int(mylist[2], 16)
bin3 = bin (dec3)

mystring =  bin1[2:]+':'+bin2[2:]+':'+bin3[2:] #trim two leading characters
print (mystring)
'''

#0 - adds leading zeroes
#8 - defines a column width
#b - converts integer to boolean  

mylist = []
mylist = MAC.split (':')

ip_template = '''
MAC address in boolean notation:
{:08b} {:08b} {:08b}
'''

print (ip_template.format (int(mylist[0],16),int(mylist[1],16),int(mylist[2],16)))




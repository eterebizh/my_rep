
# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace ('O','OSPF').replace('via','').replace(',','')

mylist = []
mylist = ospf_route.split()


text_template = '''
{:26} {:8}		
{:26} {:8}
{:26} {:8}
{:26} {:8}
{:26} {:8}
{:26} {:8}
'''

#0 - adds leading zeroes
#8 - defines column width
#b - converts integer to boolean  

print (text_template.format ('Protocol', mylist[0],'Prefix:', mylist[1],'AD/Metric',mylist[2].strip('[]'),'Next-Hop:',mylist[3],'Last update:',mylist[4],'Outbound Interface:',mylist[5]))
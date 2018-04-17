# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1

2. Определить какому классу принадлежит IP-адрес.

3. В зависимости от класса адреса, вывести на стандартный поток вывода:
  
+  'unicast' - если IP-адрес принадлежит классу A, B или C
+   'multicast' - если IP-адрес принадлежит классу D

+   'local broadcast' - если IP-адрес равен 255.255.255.255
+   'unassigned' - если IP-адрес равен 0.0.0.0

+   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''



while True:

	address = input ("Please enter an IP address: ")

	if address.lower() == 'quit' or address.lower() == 'exit':
		break

	octets = []
	octets = address.strip().split('.')

	first = int(octets[0])

	cls, typ = "", ""

	if address == '0.0.0.0':
		print ("This is unassigned IP address")
	
	elif address == '255.255.255.255':
		print ("This is local broadcast	address")

	else: 
		if first >= 1 and first <= 127:  
			cls = "A"
		elif first >= 128 and first <= 191:  
			cls = "B"
		elif first >= 192 and first <= 223:
			cls = "C"
		elif first >= 224 and first <= 239:
			cls = "D"
		else: 
			print ("This is unused IP address")

	if len (cls) > 0: # don't run this block, if class hasn't been determined 
		if cls in ['A','B','C']:
			typ = 'Unicast'
		elif cls == 'D': 
			typ = 'Multicast'

		print ("This is {} IP address that belongs to class {}".format(typ,cls))



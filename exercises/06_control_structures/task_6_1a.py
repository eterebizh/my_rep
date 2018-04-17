# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


while True:

	address = input ("Please enter an IP address: ")

	if address.lower() == 'quit' or address.lower() == 'exit':
		break

	octets = []
	octets = address.strip().split('.')

	brk = False 

	try: 
		CNT = 0
		for i in octets:
			val = int(i)
			CNT+=1
			if val >=0 and val<=255: 
				pass
			else: 			
				print ("Incorrect IP address, Please try again")			
				brk = True
				break

		if CNT < 4: 
			print ("Incorrect format. Make sure 4 octects are entered")
			brk = True
			continue

	except ValueError: 
		print ("Incorrect format")			
		continue

	if brk == True: # indicates that incorrect IP address has been issued and we're about to return call next while cycle
		continue

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



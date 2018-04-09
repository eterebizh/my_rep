
# -*- coding: utf-8 -*-
'''
Задание 5.2c

Переделать скрипт из задания 5.2b таким образом, чтобы, при запросе параметра,
которого нет в словаре устройства, отображалось сообщение 'Такого параметра нет'.

> Попробуйте набрать неправильное имя параметра или несуществующий параметр,
чтобы увидеть какой будет результат. А затем выполняйте задание.

Если выбран существующий параметр,
вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
$ python task_4_5c.py
Enter device name: r1
Enter parameter name (ios, model, vendor, location, ip): io
Такого параметра нет

Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if.
'''

london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

keys1 = london_co.keys()

device = input ("Enter device name (" + ','.join(keys1) + "):" )

while device not in keys1:  # if value doesn’t exist in the dictionary keys, then start all over again
    print ("You typed something wrong")
    device = input ("Enter device name (" + ','.join(keys1) + "):" )

keys2 = london_co[device].keys()

parameter = input ("Enter paramater name (" + ','.join(keys2) + "):")

while parameter not in keys2:  # if value doesn’t exist in the dictionary keys, then start all over again
    print ("You typed something wrong")
    parameter = input ("Enter paramater name (" + ','.join(keys2) + "):" )

print (london_co[device][parameter])




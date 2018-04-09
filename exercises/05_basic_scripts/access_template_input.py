from sys import argv

interface = input ('Please enter interface name: ')
vlan = input ('Please enter vlan-id: ')

access_template = ['switchport mode access',
				   'switch port access vlan {}', # Curly brackets indicate parameters that should be substituted using format()
				   'switchport nonegotiate',
				   'spanning-tree portfast',
				   'spanning-tree bpduguard enable']

print ('\n' + '-' * 30)

print ('interface {}'.format(interface))
print ('\n'.join (access_template).format(vlan))

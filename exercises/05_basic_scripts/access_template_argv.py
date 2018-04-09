from sys import argv

interface, vlan = argv[1:]

#print argv[0::] 

print '##################################################'
access_template = ['switchport mode access',
				   'switch port access vlan {}', # Curly brackets indicate parameters that should be substituted using format()
				   'switchport nonegotiate',
				   'spanning-tree portfast',
				   'spanning-tree bpduguard enable']

print ('interface {}').format(interface)
print ('\n'.join (access_template).format(vlan))
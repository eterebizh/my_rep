#

access_template = ['switchport mode access',
				   'switchport access vlan',
				   'spanning-tree portfast',
				   'spanning-tree bpduguard enable']

fast_int = {'access': { # define a dictionary
'0/12' :1012,
'0/14' :1050,
'0/16' :2001,
'0/17' :3001}}



for iface, vlan in fast_int['access'].items():
	print ('Interface FastEthernet{}'.format(iface))

	for command in access_template:
		if command.endswith('access vlan'):
			print (' {} {}'.format(command,vlan))
		else:			
			print (' {}'.format(command))

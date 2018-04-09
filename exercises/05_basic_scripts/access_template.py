#!/usr/bin/env python3

access_template = ['switchport mode access',
				   'switch port access vlan {}', # Curly brackets indicate parameters that should be substituted using format()
				   'switchport nonegotiate',
				   'spanning-tree portfast',
				   'spanning-tree bpduguard enable']

print ('\n::'.join (access_template).format('778'))


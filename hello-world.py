import sys
from getpass import getpass
from jnpr.junos import Device

hostname = "172.17.0.3"
junos_username = "root"
junos_password = getpass("Junos OS password: ")

try:
    with Device(host=hostname, user=junos_username, passwd=junos_password, port=22) as dev:   
        print (dev.facts)
except Exception as err:
    print (err)
    sys.exit(1)

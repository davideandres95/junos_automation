from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell
import time

dev = Device(host='crpd01', user='root', passwd='lab123')
ss = StartShell(dev)

with StartShell(dev) as ss:
  for x in range(0, 17):
    output=ss.run('cli -c "clear bgp neighbor 192.168.60.2"')
    print (output)
    time.sleep(10)

print("180 seconds have elapsed. END")


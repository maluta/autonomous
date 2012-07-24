#!/usr/bin/python
import ssh

scripts = [ "./test_cpustress.py", "./test_wireless.py"  ]

address = [ "10.0.0.1", "10.0.0.1" ] # should be getG100ip() 

machines = [ ssh.Connection(address[i]) for i in range(len(address)) ]

print g100s

#s = ssh.Connection('10.0.0.1')
for index,script in enumerate(scripts):
    print ":",script
    machines[index].put('%s' % script)
    print machines[index].execute('python %s' % script)[0]

for machine in machines:
    machine.close()


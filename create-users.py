#!/usr/bin/python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        
        #Check to see if match found the # sign, if so skip the input
        if re.match("#",line):
            continue
        #Match takes in the current line and processes it
        match = re.match(" ",line)
        
        #Put values separated by : into the fields list
        fields = line.strip().split(':')
        
        #Make sure each value has a len() of 5
        if match or len(fields) !=5:        
            continue

        #Insert specifc values in each variable
        username = fields[0]
        password = fields[1]

        gecos = "%s %s,,," % (fields[3], fields[2])

        groups = fields[4].split(',')
        
        #Send each value to the cmd prompt to fill in fields
        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        
        print(cmd)
        os.system(cmd)
        
        print("==> Setting the password for %s" % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        print(cmd)
        os.system(cmd)

        #Put users in groups if specificed in their input
        for group in groups: 
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                os.system(cmd)


if __name__== '__main__':
    main()

# Port knocking sequencer by @willc.
#
# This script will take a list of ports and use them to knock against a host in all possible orders/sequences.
# You will need to have a list of ports that you've presumably obtained from your prior enumeration efforts. If you don't know in which order to
# use them for port knocking, this script is for you.
#
# Idea modified from a blog post I found here: https://leonjza.github.io/blog/2014/10/14/knock-knock-whos-there-solving-knock-knock/
#
# To run, just do this: $> python knock-sequencer.py and follow the instructions.
#
# Use at your own risk, only on or against a computer you own and have permissions to target!
#
#!/usr/bin/python

import socket
import itertools
import sys

def main():
    print "[+] Enter IP of target to knock. Don't knock unless you have permission!"
    ipaddr = raw_input('Target IP: ')
    print "[+] Enter ports to sequence, separated by commas, like so: 8080,443,2150"
    inputlist = input ('Ports: ')

    print "[+] Knocking on the door using all possible combinations...\n"

   # Lets knock all of the possible combinations of the ports list
    for port_list in itertools.permutations(inputlist):
        
        print "[+] Knocking with sequence: %s" % (port_list,)
        for port in port_list:
            print "[+] Knocking on port %s:%s" % (ipaddr,port)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            sock.connect_ex((ipaddr, port))
            sock.close()

        print "[+] Finished sequence knock\n"
       
if __name__ == '__main__':
    print "[+] Knock knock. Who's there?"
    main()
    print "[+] Done. You should go run nmap on the target host to see if any new ports have been made available to you."

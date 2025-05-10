# Created by: Michael Johnson - 05-09-2025
# Leveraging f5py module
# Code to ping and show image based on results

# import required module
# import os
# import json
# import pprint
# import sys
import subprocess
import time

# subprocess.run(["ls", "-l"]) 

def test_network_ip(test_ip:str='8.8.8.8') -> None:
    """
    Takes IP provided and runs ping, printing results.
    """
    # Run shell commands to get test in byte form
    ping_results = subprocess.Popen(f'ping -c 5 -i .2 {test_ip} | grep -e statistics -e received', shell=True, stdout=subprocess.PIPE).stdout.read()
    #'ping -c 5 -t 1 {test_ip} | grep'
    
    # Add logic to key in on 
    # "100.0% packet loss" is a failure, anything else is good. 
    # Loop with x amount of pings.

    #if ping_result

    ping_success = True
    
    # Add actual image call and trigger logic
    while ping_success:
        print("THIS IS AN IMAGE!!!!")
        print(ping_results)
        time.sleep(1)



if __name__ == "__main__":
    # Obtain ip
    test_ip = input('Please provide an IP to test eg. 8.8.8.8 )\n')

    # Remove all dot files recursivly found under directory
    #test_network_ip(test_ip)
    test_network_ip(test_ip)

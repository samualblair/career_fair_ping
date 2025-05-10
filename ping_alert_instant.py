# Created by: Michael Johnson - 05-09-2025
# Leveraging f5py module
# Example script to ping and show results

# import required module
#import os
# import json
# import pprint
# import sys
import subprocess

# subprocess.run(["ls", "-l"]) 

test_ip = "8.8.8.8"

ping_results = subprocess.Popen(f'ping -c 5 -i .2 {test_ip} | grep -e statistics -e received', shell=True, stdout=subprocess.PIPE).stdout.read()

print(ping_results)

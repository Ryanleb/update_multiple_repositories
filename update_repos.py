'''
Author: Ryan LeBon
Description:
A simple script that allows for pulling from a text document for multiple repositories.
'''

import config
import subprocess
import os
import time

with open(config.PROJECT_NAMES,'r') as infile:
    data = infile.read()

new_list = data.splitlines()


for i in range(len(new_list)):
    try:
        BACKUP_LOCATION = config.BACKUP_LOCATION
        BACKUP_LOCATION += str(new_list[i].strip())
        if os.path.isdir(BACKUP_LOCATION):			
                cmd = 'cd {0} && git pull'.format(BACKUP_LOCATION)
                subprocess.Popen((cmd),shell=True)
    except:
        print('failed')
    time.sleep(2)

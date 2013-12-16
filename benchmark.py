#!/usr/bin/env python

import os
import subprocess
import time

def benchmark_miner():

    command = [os.path.expanduser('~/minerd'),
                '--benchmark']
    process = subprocess.Popen(command,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE)
    time.sleep(30)
    process.kill()
    lines = process.stderr.readlines()
    for line in lines[::-1]:
        if 'Total:' in line:
            total = line.split(' ')[-2]

    print total

if __name__ == '__main__':
    benchmark_miner()

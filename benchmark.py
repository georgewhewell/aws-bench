#!/usr/bin/env python

import subprocess
import time

# expects minerd in ~/
def benchmark_miner():
    command = ['~/minerd', '--benchmark']
    process = subprocess.Popen(command,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=True)
    time.sleep(30)
    process.kill()
    lines = process.stderr.readlines()
    for line in lines[::-1]:
        if 'Total:' in line:
            total = line.split(' ')[-2]

    print total

if __name__ == '__main__':
    benchmark_miner()

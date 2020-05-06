#!/usr/bin/python
import subprocess
import time

while True:
    output = subprocess.check_output(['acpi'])
    print(output.decode().split(' ')[4])
    time.sleep(10)
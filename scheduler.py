import subprocess
import threading
import datetime

p = subprocess.Popen(
	["python", "target.py"], 
	stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

for line in iter(p.stdout.readline, b''):
	print(">>> " + line.rstrip().decode('utf-8'))

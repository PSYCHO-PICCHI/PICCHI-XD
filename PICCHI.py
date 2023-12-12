import os, sys
os.system('git pull')
try:
    __import__("PSYCHO").bnsreg()
except Exception as e:
    exit(str(e))

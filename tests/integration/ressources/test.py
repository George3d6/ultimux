import sys
import time

print(f'I am a python script named {sys.argv[0]} arguments: {sys.argv[1]} and {sys.argv[2]} ')
with open('/tmp/2', 'w') as fp:
    fp.write(sys.argv[1])
# Increase for debugging purposes
time.sleep(2)

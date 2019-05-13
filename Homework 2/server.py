#CS351 -- HW2
# Nicholas Rahbany

import subprocess

def process(files):
    for f in files:
        subprocess.call(['wc', '-l', f])
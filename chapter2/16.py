import subprocess
import math
import os

lineCount = int(subprocess.check_output("wc -l popular-names.txt".split()).decode().split()[0])
inputCount = int(input())

os.system('split -l ' + str(math.ceil(lineCount / inputCount)) + ' popular-names.txt split_')

import os

os.system('cat popular-names.txt | tr " " "\t" | cut -f 1 -d "\t" > col1.txt')
os.system('cat popular-names.txt | tr " " "\t" | cut -f 2 -d "\t" > col2.txt')

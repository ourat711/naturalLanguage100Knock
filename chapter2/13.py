import os

os.system('cat popular-names.txt | tr " " "\t" | cut -f 1 -d "\t" > col1.txt')
os.system('cat popular-names.txt | tr " " "\t" | cut -f 2 -d "\t" > col2.txt')
os.system('paste -d "\t" col[1-2].txt')

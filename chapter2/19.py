import os

os.system('cut -f1 popular-names.txt | sort | uniq -c | sort -nr')

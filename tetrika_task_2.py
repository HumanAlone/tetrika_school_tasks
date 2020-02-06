from collections import Counter

counter = Counter()
try:
    with open(r"C:\Users\HumanAlone\Downloads\hits.txt\hits.txt", 'r', encoding='utf-8') as f_inp:
        for line in f_inp:
            counter[line.split('\t')[1]] += 1
except FileNotFoundError as err:
    print(err.args[1])
else:
    for ip in counter.most_common(5):
        print(ip[0])

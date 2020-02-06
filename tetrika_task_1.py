try:
    with open(r"C:\Users\HumanAlone\Downloads\names.txt", 'r', encoding='utf-8') as f_inp:
        names = f_inp.read().split(',')
except FileNotFoundError as err:
    print(err.args[1])
else:
    names = list(map(lambda x: x.strip('"'), names))
    names.sort()


    def alph_sum(name):
        return sum(list(map(lambda x: ord(x) % 65 + 1, list(name))))


    i = 1
    res_sum = 0
    for name in names:
        res_sum += alph_sum(name) * i
        i += 1

    print(res_sum)

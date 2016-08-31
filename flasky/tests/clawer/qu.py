
with open('splits.txt', 'r', encoding="utf-8") as f:
    for x in f.readlines():
        s = x.split()[1].split(',')
        for y in s:
            if len(y) == 1:
                print(y,s)
                break

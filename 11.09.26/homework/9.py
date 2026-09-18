# -*- coding: utf-8 -*-

with open("input.txt", "r") as f:
    sogl = 'יצךםדרשחץתפגןנכהזקסלעüב'; gl = 'ףוûאמ‎ÿט‏¸'
    for line in f.read():
        l = line.strip(); l_copy = ''; l_copy += l[0]
        for i in range(1, len(l)):
            if l[i - 1] in sogl and l[i] in gl:
                l_copy += l[i] + l[i - 1] + l[i]
            else:
                l_copy += l[i]
        print(l_copy)
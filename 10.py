with open("input.txt", "r", encoding="utf-8") as f:
    sogl = 'йцкнгшщзхъфвпрлджчсмтьб'; gl = 'уеыаоэяиюё'
    for line in f.readlines():
        l = line.strip(); l_copy = ''; l_copy += l[0]
        for i in range(1, len(l)):
            if l[i - 1] in sogl and l[i] in gl:
                l_copy += l[i] + 'c' + l[i]
            else:
                l_copy += l[i]
        print(l_copy)
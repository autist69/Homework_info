with open("input.txt", "r") as f:
    text = f.read().replace(' ', '').replace('.', ' ').replace('!', ' ').replace('?', ' ').split();
    cnt = 0
    for line in text:
        l = line.strip()
        if len(line) > 0:
            cnt += 1
    print(cnt)
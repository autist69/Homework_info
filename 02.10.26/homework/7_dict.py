import string
from pathlib import Path

with Path(r"C:\Games\VS Code\Python\text.txt").open("r", encoding="utf-8") as text:
    f = text.read().strip().lower()
    for symb in f:
        if symb in string.punctuation:
            f = f.replace(symb, "")

    f = f.split()

    Dict = {}
    for word in f:
        if word in Dict:
            Dict[word] += 1
        else:
            Dict[word] = 1

    max_count = 10
    for n, pairs in enumerate(sorted(Dict.items(), key = lambda p: p[1], reverse=True)):
        if n >= max_count:
            break
        else:
            print(pairs[0], pairs[1])

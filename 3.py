# 3

alph = dict(); alph["A"] = "A"; alph["H"] = "H"; alph["I"] = "I"; alph["M"] = "M"
alph["O"] = "O"; alph["T"] = "T"; alph["U"] = "U"; alph["V"] = "V"; alph["W"] = "W"
alph["X"] = "X"; alph["Y"] = "Y"; alph["1"] = "1"; alph["8"] = "8"; alph["E"] = "3"
alph["J"] = "L"; alph["S"] = "2"; alph["Z"] = "5"
line = str(input()); pal = True; mir = True;
if len(line) % 2 == 0:
    for i in range(len(line) // 2):
        if line[i] != line[-(i + 1)]:
            pal = False
        if line[i] in "AHIMOTUVWXY18E3JLS2Z5":
            if alph[line[i]] != line[-(i + 1)]:
                mir = False
        else:
            mir = False
        
else:
    for i in range(len(line) // 2 + 1):
        if line[i] != line[-(i + 1)]:
            pal = False
        if line[i] in "AHIMOTUVWXY18E3JLS2Z5":
            if alph[line[i]] != line[-(i + 1)]:
                mir = False
        else:
            mir = False

if pal:
    if mir:
        print(f"\"{line} is a mirrored palindrome.\"")
    else:
        print(f"\"{line} is a regular palindrome.\"")
else:
    if mir:
        print(f"\"{line} is a mirrored string.\"")
    else:
        print(f"\"{line} is not a palindrome.\"")
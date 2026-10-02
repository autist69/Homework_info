list1 = {24, 56, 64, 116, 192, 216, 264, 268, 312, 320}
list2 = {48, 56, 88, 120, 140, 204, 216, 220, 280, 312}

print(*(list1^list2))
print(*(list1|list2))
print(*(list1&list2))

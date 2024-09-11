set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

diff1_set = set1 - set2
diff2_set = set2 - set1

union_set = set1 | set2

symmdiff1_set = set2 ^ set1
symmdiff2_set = set1 ^ set2

intersection1_set = set1 & set2
intersection2_set = set2 & set1

print("Set Difference of set1 - set2:", diff1_set)
print("Set Difference of set2 - set1: ", diff2_set, "\n")

print("Union of Sets: ", union_set, "\n")

print("Symmetric Difference of set2 ^ set1: ", symmdiff1_set)
print("Symmetric Difference of set1 ^ set2: ", symmdiff2_set, "\n")

print("Set Intersection of set1 & set2: ", intersection1_set)
print("Set Intersection of set2 & set1: ", intersection2_set)




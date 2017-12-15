import itertools


test = [[5,9, 2, 8],
[9, 4, 7, 3],
[3, 8, 6, 5]]

spreadsheet = []

#file = test.splitlines()
#print(file)

checksum = 0


comb = list(itertools.combinations(test, 2))
print(comb)

print(spreadsheet)
print(checksum)


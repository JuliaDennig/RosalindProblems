input = input("Input:\n")
bases = ["A", "C", "G", "T"]
basecount = []
for i in range(len(bases)):
    count = input.count(bases[i])
    basecount.append(count)
print(basecount[0], basecount[1], basecount[2], basecount[3])
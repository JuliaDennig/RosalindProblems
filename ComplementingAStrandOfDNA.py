input = input("Input:\n")
complement = input.replace("T", "X").replace("A", "T").replace("X","A").replace("G","Y").replace("C","G").replace("Y","C")
print(complement[::-1])
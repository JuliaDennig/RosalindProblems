file_lines, labels = [], []
sequence_dict, GC_dict = {}, {}
input = input(".fasta file location\n")
file = open(input, "r")
file_lines = file.readlines()
seqcount = [d for d, w in enumerate(file_lines) if '>' in w]
for i in range(len(seqcount)):
    labels.append(file_lines[seqcount[i]])
    if i < len(seqcount)-1:
        sequence = ''.join(file_lines[seqcount[i]+1:seqcount[i+1]]).replace("\n","")
        sequence_dict.update({file_lines[seqcount[i]]:sequence})
    else:
        sequence = ''.join(file_lines[seqcount[i]+1:len(file_lines)]).replace("\n","")
        sequence_dict.update({file_lines[seqcount[i]]:sequence})
highest_GC = 0
for j in range(len(labels)):
    GC = round((sequence_dict[labels[j]].count("G")+sequence_dict[labels[j]].count("C"))/len(sequence_dict[labels[j]])*100, 6)
    GC_dict.update({labels[j]:GC})
    if GC > highest_GC:
        highest_GC = GC
        result = ({labels[j]:GC})
        label_result = labels[j]
print(label_result.replace(">","").replace("\n",""))
print(result[label_result])

def findingORFS(s):
    ATGs = []
    StoppTriplets = ["UGA", "UAA", "UAG"]
    ORFs = []
    proteinlist = []
    import re
    for m in re.finditer("AUG", s):
        ATGs.append(str(m.start() + 1))
    for i in range(len(ATGs)):
        ORFTriplets = []
        ORF = s[int(ATGs[i]) - 1:]
        ORFTriplets.append(ORF[0:3])
        for j in range(int(len(ORF) / 3)):
            ORFTriplets.append(ORF[int((j + 1) * 3):int((j + 2) * 3)])
        index = -1
        var = False
        for k in range(3):
            if StoppTriplets[k] in ORFTriplets and var is False:
                index = ORFTriplets.index(StoppTriplets[k])
                var = True
            if StoppTriplets[k] in ORFTriplets and ORFTriplets.index(StoppTriplets[k]) < index and var is True:
                index = ORFTriplets.index(StoppTriplets[k])
        if index != -1:
            ORFs.append(ORFTriplets[0:index])
    for m in range(len(ORFs)):
        prot = []
        aminoacids = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                      "UCU": "S", "UCC": "S",
                      "UCA": "S", "UCG": "S", "AGC": "S", "AGU": "S", "UAU": "Y", "UAC": "Y", "UGU": "C", "UGC": "C",
                      "UGG": "W", "CCU": "P",
                      "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R",
                      "CGC": "R", "CGA": "R",
                      "CGG": "R", "AGG": "R", "AGA": "R", "AUA": "I", "AUC": "I", "AUU": "I", "AUG": "M", "ACU": "T",
                      "ACA": "T", "ACC": "T",
                      "ACG": "T", "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "GUU": "V", "GUC": "V", "GUA": "V",
                      "GUG": "V", "GCU": "A",
                      "GCA": "A", "GCG": "A", "GCC": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G",
                      "GGC": "G", "GGA": "G",
                      "GGG": "G", "UGA": "", "UAA": "", "UAG": ""}
        if ORFs[m] is not None:
            for n in range(int(len(ORFs[m]))):
                triplet = ORFs[m][n]
                prot.append(aminoacids[triplet])
            protein = "".join(prot)
            proteinlist.append(protein)
    return proteinlist


s = """AGTTTCAACGGCATGGGGGTCGGGTAGTTATCTTCCTGCCCGGCTGTGTTCTGGGGCCCT
TTAATCCCTTGAACTCGGCAATTCTGACTGGGACACGGTTCGTCATAAACTCGGGGCGAA
GCATCCCGTCGCCGGGTGTCAGGTCTTGGGTCGTTGTGGCTTCGCTCCAGCCTGAATGTC
TAGATCGTTGGATCACTGAGGCTTCGGAGGTAAAATCCTCGCCCAACCGGATGACACAGG
GAATAGTCCCCTAAGATTAGGATTAATTGCGGGATTTGGGCATATAGAGGGATCACCAGG
CGCACGTGACTTTGGTAGGATTTAGGTAAGGTCGCGGCAGAGTTGTCAGCATAGCAAGAG
ACAAGCACCCTACCCGACGCGTGTAGTTCCACGAAGAGGAACCGCCCCGGGTTGCTCATC
AATACCATTGATGGGACTCTTTTGATGGAATAACGTCAAGTGCGGTATGACTAGCTAGTC
ATACCGCACTTGACGTTATTCCATCCCCGGAAGGCCCGGACTCCGATGATTGCAGAAGCT
GGTCCCCCGTGAGATGCGGCGGGAACGTGAGTTATAACAGCATAAACCTTAGTTAAATTG
AGAGCAAAAGTTCTCATATCACACGTATTTATTGGAGGCATGAGGGACCTTGTCACAAGG
TCATGTTTGGGCAGCAACATGCCGTTACAATAGTCCTGCCCTCCCAAGTGGGCTTACCGT
CCGTAGCATGTAACGCCACAACGACGGAGGATATGGAGTTCGTCTGGGTGACGTACAGCT
AGGAACAACGATCTTAGGCCCTGACTTAGGTGTGACAATGATGCTCATCGCGCGGGTCGA
TAGCCCTAGCATTAGATCTTTAGAATCCCTTCACCACTTAAGTTCGATTATTAATTCCTA
GGTTCAGCCGTCCCCACTGTCGGACTAGCTTACAAATAAAGGTTAGCC"""
s = s.replace("T", "U").replace("\n", "")
complement = s.replace("U", "X").replace("A", "U").replace("X", "A").replace("G", "Y").replace("C", "G").replace("Y",
                                                                                                                 "C")
reversecomplement = complement[::-1]
proteinlist = findingORFS(s)
proteinlist2 = findingORFS(reversecomplement)
results = []
for q in range(len(proteinlist)):
    if proteinlist[q] not in results:
        results.append(proteinlist[q])
for o in range(len(proteinlist2)):
    if proteinlist2[o] not in results:
        results.append(proteinlist2[o])
for p in range(len(results)):
    file = open("orfs.txt", "a")
    file.write(results[p])
    file.write("\n")
    file.close()

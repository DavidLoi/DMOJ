letters = int(input())

base = input()

molecule = False
dna = False
rna = False

for i in range(letters):
    if base[i] == "A" or base[i] == "C" or base[i] == "G":
        molecule = True
    elif base[i] == "T":
        dna = True
    elif base[i] == "U":
        rna = True
    else:
        molecule = False
        dna = False
        rna = False
        break

if not dna and not rna:
    if molecule:
        print("both")
    elif not molecule:
        print("neither")
elif dna and rna:
    print("neither")
elif dna:
    print("DNA")
elif rna:
    print("RNA")
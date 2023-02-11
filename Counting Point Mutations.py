#Point Mutations
count = 0
x = 0

dna1 = input("sequence:\n")
dna2 = input("sequence:\n")

while (count < len(dna1)):
    if (dna1[count] != dna2[count]):
        x = x + 1
    count = count + 1
    
print(x)

print("\n---\n")

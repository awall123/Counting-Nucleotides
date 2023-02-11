#GC content
DNA=input("Enter sequence:\n")
gc_count = DNA.count("G")+ DNA.count("C")
total=len(DNA)
print((gc_count/total)*100)

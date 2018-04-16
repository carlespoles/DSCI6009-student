# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Sequencing example from .fasta file. We convert .fasta file to .txt file format.
# Downloaded BRAC1 data from https://www.ncbi.nlm.nih.gov/nuccore/NC_008802.1?report=fasta

# Set value of each nucleotide to 0.
a, g, c, t = 0, 0, 0, 0;

with open("../Data/brac1.txt", "r") as f:
    gene = f.read()
    for line in gene.lower():
        for char in line:
            if char == "a":
                a+=1
            if char == "g":
                g+=1
            if char == "c":
                c+=1
            if char == "t":
                t+=1 


print("Adenines: {:,.2f}".format(a))
print("\nThynines: {:,.2f}".format(t))
print("\nGuanines: {:,.2f}".format(g))
print("\nCytosines: {:,.2f}".format(c))

gc_ratio = (g+c)/(g+c+a+t)
at_ratio = (a+t)/(g+c+a+t)

print("\nAT ratio: {:.2%}".format(at_ratio))
print("\nGC ratio: {:.2%}".format(gc_ratio))


            
        
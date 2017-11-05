# -*- coding: utf-8 -*-
from challenge_5 import read_infile

list_of_str = read_infile("input.txt")

for n in [50000000]:
    output_filename = "input_" + str(n) + ".txt"
    with open(output_filename, 'w') as o_f:
        o_f.write(" ".join(n*list_of_str))

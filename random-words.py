import random
from sys import argv

if len(argv) == 2:
    script, x = argv
    x = int(x)
else:
    x = 1

file = "words.txt"

#def random_line_l(lines):
    #'''Returns a random line from a series of lines'''
    #myline = random.choice(lines)
    #return myline


def random_line_f(file, x):
    lines = open(file).read().splitlines()
    print("\n")
    for i in range(x):
        print(random.choice(lines))
    print("\n")

random_line_f(file, x)

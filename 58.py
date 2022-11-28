# write a python program to read a random line from a file.



'''import random

def random_line(fname):
    lines=open(fname).read().splitlines()
    return random.choice(lines)
print(random_line("sagar123.txt"))'''



            #OR
import random
file=open("sagar.txt", "r")
a=(file.read()).split(".")[:-1]
print(random.choice(a))

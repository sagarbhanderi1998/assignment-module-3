# write a python program to print all unique values in a dictionary.


p={'a':32, 'b':33, 'c':75, 'd':33, 'e':42, 'f':32, 'g':32, 'h':65, 'i':65}
i=set(p.values())
print(list(i))

# write a python program to find the highest 3 values in a dictionary.


p={'a':3, 'b':313, 'c':755, 'd':254, 'e':22, 'f':93, 'g':53, 'h':444, 'i':115,"j":12,"k":9}
r=list(p.values())
r.sort(reverse=True)
print(r)
print(r[0:3])

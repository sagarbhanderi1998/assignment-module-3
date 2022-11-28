# Write a Python program to replace last value of tuples in a list. 
l=[(5,3,5), (8,5,3), (9,7,4)]
o=[]
for r in l:
   i=r[:-1]+(100,)
   o.append(i)
print(o)

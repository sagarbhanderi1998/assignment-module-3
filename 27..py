# Write a Python program to find the repeated items of a tuple. 
p=(3,6,8,0,7,5,3,5,8,0,9,6,4)
c=[]
for i in p:
    if p.count(i)>1:
        if i not in c:
         c.append(i)
print(c)

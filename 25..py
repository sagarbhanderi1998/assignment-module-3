# write a python program to reverse a tuple.


tup=(1,2,3,4,5,6,7,8,9,0)
p=list(tup)
p.reverse()
t=tuple(p)
print(t)


                #OR


tup=(1,2,3,4,5,6,7,8,9,0)
x=reversed(tup)
y=tuple(x)
print(y)

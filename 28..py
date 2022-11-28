# Write a Python program to remove an empty tuple(s) from a list of tuples
p=[(1,5,6),4,67,(),(5,4,68,49),(),[],{},(),(), (23,45,7,2,67,89) (),{}]
for i in p[::-1]:
    if type(i)==tuple and len(i)==0:
        p.remove(i)
print(p)

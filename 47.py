# write a python program to create a dictionary from a string.


str="w3resorce"
dict={}
for i in str:
    dict[i]=dict.get(i,0)+1
print(dict)


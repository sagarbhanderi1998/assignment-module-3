# write a python program to create and display all combination of letters,
# selecting each letter from a different key in a dictionary.


p={"1":["a","b"],"2":["c","d"]}
r=list(p.values())
for i in r[0]:
    for j in r[1]:
        s=i+j
        print(s,end=" ")

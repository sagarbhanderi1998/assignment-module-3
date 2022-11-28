# Write a Python script to concatenate following dictionaries to create a new one.
p={3: 'Naresh', 2: 'Deepak', 5: 'Mayank', 4: 'Satish'}
r={1:"Suthar", 6:"Hitesh"}
s={7:"Ritesh", 8:"Haresh", 9:"Malin"}
g={10:"Shankar", 11:"Sunil"}
j={}
for i in [p,r,s,g]:
    j.update(i)
print(j)




                #OR

p={3: 'Naresh', 2: 'Deepak', 5: 'Mayank', 4: 'Satish'}
q={1:"Suthar", 6:"Hitesh"}
r={7:"Ritesh", 8:"Haresh", 9:"Malin"}
s={10:"Shankar", 11:"Sunil"}

print(p|q|r|s)

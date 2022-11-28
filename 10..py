# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.


list=[]
for i in range(1,31):
    list.append(i*i)
p=list[:5]
p.extend(list[-5:])
print(p)





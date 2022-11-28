# Write a Python program to split a list into different variables. 
n= int(input("number of spliting element:"))
o=[]
m=-1
p= ['Naresh', 'Suthar', 'Deepak', 'Prajapati', 'Hello', 'World']
for i in range(len(p)):
    if i%n!=0:
        o[m].append(p[i]) 
    else:
        m=m+1
        o.append([])
        o[m].append(p[i])
print(o)

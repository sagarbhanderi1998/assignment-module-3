# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.  


list2=["naresh", 'suthar', 'nayan', 'amar', 'aliya', 'asha','sagar','naman']
b=0
for i in list2:
    if len(i)>=2 and i[0]==i[-1]:
        b=b+1
print(b)

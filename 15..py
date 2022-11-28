#Write a Python program to get unique values from a list 


list1=[2,4,7,9,6,4,5,2,6,8,9,6,4,3]
def fun(l):
     f=[]
     for i in l:
         if l.count(i)==1:
           f.append(i)
     print(f)
fun(list1)

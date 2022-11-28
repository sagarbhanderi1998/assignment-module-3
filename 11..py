#  Write a Python function that takes a list and returns a new list with unique elements of the first list.


list1=[2,4,4,3, 'sagar', 4,6,8,7,"bhanderi"]
def fun(l,p):
    f=[]
    for i in l:
        if type(i)!=p:
            f.append(i)
    print(f)
fun(list1,int)

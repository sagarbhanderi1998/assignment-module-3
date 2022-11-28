# write a python function to check wheather a number is perfect or not.


n=int(input("enter a given number:"))


def perfect_num(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum == n
print(perfect_num(n))

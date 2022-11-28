#  write a python function to check a number is in a given range.

n=int(input("Enter a number :"))


def number(n):
    if n  in range (1,50):
        print ("Given number is available in range:")
    else:
        print("Given number is not a available in range:")
print(number(n))



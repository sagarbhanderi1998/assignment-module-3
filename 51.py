#  write a python function that checks wheather a passed string is palidrone or not.



def is_palidrom(word):
    if word==word[::-1]:
        return True
    else:
        return False

print(is_palidrom("sagar"))
print(is_palidrom("nayan"))
print(is_palidrom("naman"))


            #OR
word=input("Enter a Name:")

def palidrom(word):
    if word==word[::-1]:
        return True
    else:
        return False
print(palidrom(word))

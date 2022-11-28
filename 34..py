# write a python script to concatenate following dictionaries to create a new one.


s=int(input("Enter the key:"))
p={ 1: 'urjit', 2: 'sagar', 3: 'samir', 4: 'vivek', 5: 'Satish',8:'mayank',10:'ravi'}
if s in p.keys():
    print(s, "is allready exist.")
else:
    print(s, "is not exist in given dictionary.")


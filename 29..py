#Write a Python program to unzip a list of tuples into individual lists. 


l = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)]
print(list(zip(*l)))
print(tuple(zip(*l)))

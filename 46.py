# write python program to combine values in python list of dictionaries.

from collections  import counter
sample=[{"item":"item1","amount":400}],[{"item":"item2","amount":300}],[{"item":"item1","amount":750}]


result= counter()

for i in sample:
    result[i["item"]]=[i["item"]]+[i["amount"]]
print(result)

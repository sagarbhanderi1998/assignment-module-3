# Write a Python script to merge two Python dictionaries.


s1={1.:"sagar",2.:"jigar",3.:"vivek",4.:"ravi"}
s2={5.:"dhruvin",6.:"urjit",7.:"jenik",8.:"jay"}
s=s1.copy()
s.update(s2)
print(s)


                #OR


s1={1.:"sagar",2.:"jigar",3.:"vivek",4.:"ravi"}
s2={5.:"dhruvin",6.:"urjit",7.:"jenik",8.:"jay"}
s1.update(s2)
print(s1)


                #OR

s1={1.:"sagar",2.:"jigar",3.:"vivek",4.:"ravi"}
s2={5.:"dhruvin",6.:"urjit",7.:"jenik",8.:"jay"}
print(s1|s2)

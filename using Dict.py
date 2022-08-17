d1 = {'USA':100,'UK':200,'INDIA':300}
d2 = {'USA':'AMERICA','UK':'United Kingdom','CHINA':'CORONA','INDIA':'Delhi'}


print(d1)
print(d2)
print(len(d1))
print(len(d2))
print(d1['USA'])

print(d2['UK'])

print(d1.values())
print(d1.keys())
print(d2.values())
print(d2.keys())

for i in d1:
    print(i,d1[i])


print ('UK' in d2)
print ('UUU' in d1)

#functions will work on keys on the dict


 




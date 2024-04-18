def merge(dict1,dict2):
    return dict1.update(dict2)
d1={1:20,2:30,4:50}
d2={5:60,7:80,8:90}
merge(d1,d2)
print("updated d1 is:",d1)

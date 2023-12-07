
# to removing  duplicate  values  by  using if condition
l1={10,20,30,40,10,20,50,60,70,80,70,60}

for i in l1:
    if  i  not in l1:
        l1.remove(i)
print(l1)        




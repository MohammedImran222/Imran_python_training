li =  [1,2,3,4,5,6,7,8,9]
o,e=0,0
for i in li:
    if i%2==0:
        e+=1
    else:
        o+=1
print("Number of even numbers :",e)
print("Number of odd numbers :",o)
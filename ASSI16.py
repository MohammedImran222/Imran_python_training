def edigit(x):
    if  x in [0,2,4,6,8]:
        return 1
    return 0
print('numbers between 100 and 400 where each digit of a number is an even number : ')
for i in range(100 , 401):
    bool1 = True
    x = i
    while(x!=0):
        if edigit(x%10)  == 0:
            bool1 = False
        x=x//10
    if bool1 :
        print(i , end= ', ')            
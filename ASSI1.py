def ToFindnum(start,end):
    li=[]
    for i in range(start,end+1):
        if i%7==0 and i%5==0:
            li.append(i)
    return li
x = int(input('enter the start number :'))
y = int(input('enter the end number :'))
lis=ToFindnum(x, y)
print('The number divisible by 7 and multiple of 5 B/W  '+str(x)+'and ' +str(y)+': ',end=' ')
print(lis)
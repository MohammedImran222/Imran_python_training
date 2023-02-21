li=[]
x = int(input('Enter no of rows:'))
y = int(input('Enter no of cols:'))
for i in range(x):
    lis= []
    for  j in range(y):
        lis.append(i*j)
    li.append(lis)
print(li)
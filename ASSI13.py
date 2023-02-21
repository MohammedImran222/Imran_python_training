from test.ann_module import dec
def bintodec(x):  
    powe=3
    n=0
    for i in x:
        if i == '1':
            n+=(2**powe)
        powe-=1
    return(n)
def dectobin(x):
    s=''
    while(x!=0):
        if (x%2==0):
            s+='1'
        else:
            s+='0'
        x=x//2
    return s
x = input("DATA IN NEED : ")
li = x.split(',')
li = [bintodec(i) for i in li]
for i in li:
    if i % 5== 0:
        print(dectobin(i),end=' ')
        
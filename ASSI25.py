x=5
for i in range(7):
    if i==0 or i==6:
        print('*'*7)
    else:
        print(' '*x,'*')
        x-=1
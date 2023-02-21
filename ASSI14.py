st1 =input('String in need as aplphanumeric : ')
c1,c2=0,0
for i in st1:
    if i.isalpha():
        c1+=1
    elif i.isalnum():
        c2+=1
print('Count of Letters : ',c1)
print('Count of digits : ',c2)
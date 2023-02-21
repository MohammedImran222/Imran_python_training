temp = input("Enter the  temperature eg: 100F or 100C : ")
if 'C' in temp:
    x = temp.split('C')
    faren = (int(x[0]) * (9//5))+32
    print(temp+' is ' +str(faren)+" in Fahrenheit")
elif 'F' in temp:
    x = temp.split('F')
    cel = (int(x[0])-32)*5//9
    print(temp+' is ' +str(cel)+" in Celsius")
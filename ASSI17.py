str1="";    
for r in range(0,7):    
    for c in range(0,7):     
        if (((c == 1 or c == 5) and r != 0) or ((r == 0 or r == 3) and (c > 1 and c < 5))):    
            str1=str1+"*"    
        else:      
            str1=str1+" "    
    str1=str1+"\n"    
print(str1)
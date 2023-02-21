import re
def couna(str1):
    c,c2,c3,c4 = 0,0,0,0
    for i in str1:
        if i.isupper():
            c+=1
        elif i.islower():
            c2+=1
        elif i.isnumeric():
            c3+=1
        elif i in ['$','#','@']:
            c4+=1
    return [c,c2,c3,c4]
pasw = input('enter ur password : ')
if len(pasw)>=6 and len(pasw) <= 16:
    li = couna(pasw) 
    if li[0]>0 and li[1]>0 and li[2]>0 and li[3]>0:
        print('valid Password')
    else:
        print('Invalid Password')
else:
    print('Your password must contain more than 6 wrd and less than or equal to 16 wrd')
M_LIS={'January':31, 'February':'28/29', 'March':31, 'April':30, 'May':31,'June':30, 'July':31, 'August':30, 'September':30, 'October':31, 'November':30, 'December':31}
x = input('Enter the month name to get no days :')
print(x+': '+str(M_LIS[x]))
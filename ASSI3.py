import random
def guess(x):
    user = int(input('enter guess the number 1-9 :'))
    if user == x:
        return True
    return  guess(x)
x = random.randint(1,9)
if guess(x) == True:
    print('Well Guessed ! ')
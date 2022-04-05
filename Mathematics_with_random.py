"""Text Based Mathematics Game"""

import random

def multiplication(password):
    """Produces 2 random numbers, muliplies them and compares it to the users input"""
    while password == 'yes':
        dif = input('Choose a difficulty hard(h) or easy(e):')
        if dif == 'h':
            a = list(range(21))
            b = list(range(21))
            hardnum = random.choice(a)
            hardnum2 = random.choice(b)
            def hard(a, b, usrans):
                i = hardnum * hardnum2
                usrans = int(input(':'))
                if usrans == i:
                    print('Good Multiplication')
                else:
                    print('Incorrect')
                    return
            print('What is', hardnum, 'X', hardnum2)
            z = ('Answer here:')
            hard(a, b, z)
            password = input('wanna play again types yes to continue no to cancel?:')
        if dif == 'e':
            a2 = list(range(10))
            b2 = list(range(10))
            easynum = random.choice(a2)
            easynum2 = random.choice(b2)
            def easy(a2, b2, usrans2):
                i = easynum * easynum2
                usrans = int(input(':'))
                if usrans == i:
                    print('Good job you got it right! Go a little harder next time.')
                else:
                    print('Incorrect')
                    return 
            print('What is',easynum, 'X', easynum2)
            z2 = ('Answer here:')
            easy(a2, b2, z2)
            password = input('wanna play again types yes to continue no to cancel?:')
            return
def addition(password):
    """Produces 2 random numbers, adds them and compares it to the users input"""
    while password == 'yes':
        dif = input('Choose a difficulty hard(h) or easy(e):')
        if dif == 'h':
            a = list(range(100))
            b = list(range(100))
            hardsub = random.choice(a)
            hardsub2 = random.choice(b)
            def hard(a, b, usrans):
                i = hardsub + hardsub2
                usrans = int(input(':'))
                if usrans == i:
                    print('Good addition')
                else:
                    print('Incorrect')
                    return
            print('What is', hardsub, '+', hardsub2)
            z = ('Answer here:')
            hard(a, b, z)
            password = input('wanna play again types yes to continue no to cancel?:')
        if dif == 'e':
            a2 = list(range(100))
            b2 = list(range(100))
            easynum = random.choice(a2)
            easynum2 = random.choice(b2)
            def easy(a2, b2, usrans2):
                i = easynum + easynum2
                usrans = int(input(':'))
                if usrans == i:
                    print('Good job you got it! Go a little harder next time.')
                elif usrans != i:
                    print('Incorrect')
                    return 
            print('What is',easynum, '+', easynum2)
            z2 = ('Answer here:')
            easy(a2, b2, z2)
            password = input('wanna play again types yes to continue no to cancel?:')
            return
def subtraction(password):
    """Produces 2 random numbers, subtracts them and compares it to the users input"""
    while password == 'yes':
        dif = input('Choose a difficulty hard(h) or easy(e):')
        if dif == 'h':
            a = list(range(1001 ,4001))
            b = list(range(1001))
            hardsub = random.choice(a)
            hardsub2 = random.choice(b)
            def hard(a, b, usrans):
                i = hardsub - hardsub2
                usrans = int(input(':'))
                if usrans == i:
                    print('Good subtraction')
                else:
                    print('Incorrect')
                    return
            print('What is', hardsub, '-', hardsub2)
            z = ('Answer here:')
            hard(a, b, z)
            password = input('Wanna play again types yes to continue no to cancel?:')
        if dif == 'e':
            a2 = list(range(10, 20))
            b2 = list(range(10))
            easynum = random.choice(a2)
            easynum2 = random.choice(b2)
            def easy(a2, b2, usrans2):
                i = easynum - easynum2
                usrans = int(input(':'))
                if usrans == i:
                    print('Good job you got it! Go a little harder next time.')
                else:
                    print('Incorrect')
                    return 
            print('What is',easynum, '-', easynum2)
            z2 = ('Answer here:')
            easy(a2, b2, z2)
            password = input('wanna play again types yes to continue no to cancel?:')
            return
def division(password):
    """Produces 2 random numbers, divides them and compares it to the users input"""
    while password == 'yes':
        dif = input('Choose a difficulty hard(h) or easy(e):')
        if dif == 'h':
            a = list(range(2, 50, 2))
            b = list(range(2, 50, 2))
            hardsub = random.choice(a)
            hardsub2 = random.choice(b)
            def hard(a, b, usrans):
                i = hardsub // hardsub2
                usrans = int(input(':'))
                if usrans == i:
                    print('Good subtraction')
                else:
                    print('Incorrect')
                    return
            print('What is', hardsub, '//', hardsub2)
            z = ('Answer here:')
            hard(a, b, z)
            password = input('wanna play again types yes to continue no to cancel?:')
        if dif == 'e':
            a2 = list(range(0, 100, 2))
            b2 = list(range(0, 100, 2))
            easynum = random.choice(a2)
            easynum2 = random.choice(b2)
            def easy(a2, b2, usrans2):
                i = easynum // easynum2
                usrans = int(input(':'))
                if usrans == i:
                    print('Good job you got it! Go a little harder next time.')
                else:
                    print('Incorrect')
                    return 
            print('What is',easynum, '//', easynum2)
            z2 = ('Answer here:')
            easy(a2, b2, z2)
            password = input('wanna play again types yes to continue no to cancel?:')
            return
     
kind = input('What type of math would you like to do: Multipliaction(1), Division(2), Addition(3), Subtraction(4):')
if kind == '1':
    multiplication('yes')
elif kind == '2':
    division('yes')    
elif kind == '3':
    addition('yes')
elif kind == '4':
    subtraction('yes')

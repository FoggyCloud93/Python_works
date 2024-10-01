def conjuction(a,b):
    return a & b
def disjunction(a,b):
    return a | b
def implication(a,b):
    return not(a) or b
def equivalent(a,b):
    return a == b
def nott(a,b):
    return not(a) or not(b)
def xor(a,b):
    return a^b
def ravnosil1(a):
    return a & a
def ravnosil2(a,b):
    return a & b
def ravnosil22(a,b):
    return b & a
def ravnosil3(a,b,c):
    return (a&b)&c
def ravnosil33(a,b,c):
    return a&(b&c)
inp=input('введите название любой из функций или равносильности xor,nott,equivalent,implication,disjunction,conjuction,ravnosil1/2/3 :')
for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            if inp == 'disjunction':
                print(a , b ,disjunction(a,b))
            elif inp == 'conjuction':
                print(a, b, conjuction(a, b))
            elif inp == 'implication':
                print(a, b, implication(a, b))
            elif inp == 'equivalent':
                print(a, b, equivalent(a, b))
            elif inp == 'nott':
                print(a, b, nott(a, b))
            elif inp == 'xor':
                print(a, b, xor(a, b))
            elif inp == 'ravnosil1':
                print('a - f ,функция a & a')
                print(a," ", ravnosil1(a))
            elif inp == 'ravnosil2':
                print('a b f1 f2, функция a & b, b & a')
                print(a ,b,'' ,ravnosil2(a,b),'' ,ravnosil22(a,b))
            elif inp == 'ravnosil3':
                print('a b f1 f2, функция (a&b)&c, a&(b&c) ')
                print(a, b,'', ravnosil3(a,b,c), '',ravnosil33(a,b,c))

            else:
                print('error')

# 1 коммит





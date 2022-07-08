
def sum(a, b) :
    return a + b

def dif(a, b) :
    return a - b

def mul(a, b) :
    return a * b

def div(a, b) :
    if b != 0 :
        return a / b
    else :
        return 'try again'

def exp(a, b) :
    return a ** b

def root(a, b) :
    if a >= 0 :
        return a ** (1 / b)
    else :
        return 'try again'

def fac(a, _) :
    fact = 1
    if a > 0 and a % 1 == 0 :
        for i in range(1, int(a) + 1) :
            fact = fact * i
        return fact, 'b is not used'
    else :
        return 'try again'


dict = {'+' : sum,
        '-' : dif,
        '*' : mul,
        '/' : div,
        '**' : exp,
        '^' : exp,
        '√' : root,
        '!' : fac}

if __name__ == '__main__' :
    print(fac(3,5))
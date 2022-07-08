import dictionary
import os

def main() :
    
    com = input('1 - run, else - break : ')
    while com == '1' :
        os.system("clear")
        a = float(input('a : '))
        b = float(input('b : '))
        print(dictionary.dict[input('sign : ')](a, b))
        com = input('1 - run, else - break : ')

if __name__ == '__main__' :
    main()
import time
import os
import random

os.system('clear')

a = int(input())
b = int(input())

os.system('clear')

list = []

for i in range(a+2) :
    if i == 0:
        list.append(['*'] * (b+2))
        continue
    if i == a+1:
        list.append(['*'] * (b+2))
        continue
    list.append([' '] * (b+2))
    list[i][0] = '*'
    list[i][b+1] = '*'
    
m_x = random.randint(1,a)
m_y = random.randint(1,b)
c_x = random.randint(1,a)
c_y = random.randint(1,b)

while c_x == m_x and c_y == m_y :
    m_x = random.randint(1,a)
    m_y = random.randint(1,b)
    c_x = random.randint(1,a)
    c_y = random.randint(1,b)

list[c_x][c_y] = 'c'
list[m_x][m_y] = 'm'

for row in list:
    for elem in row:
        print(elem, end=' ')
    print()

while True:
    dir = random.randint(1,8)
    list[m_x][m_y] = ' '
    if dir == 1 :
        m_x = m_x + 2
        m_y = m_y
    elif dir == 2 :
        m_x = m_x - 2
        m_y = m_y
    elif dir == 3 :
        m_x = m_x
        m_y = m_y + 2
    elif dir == 4 :
        m_x = m_x
        m_y = m_y - 2
    elif dir == 5 :
        m_x = m_x + 2
        m_y = m_y + 2
    elif dir == 6 :
        m_x = m_x + 2
        m_y = m_y - 2
    elif dir == 7 :
        m_x = m_x - 2
        m_y = m_y - 2
    elif dir == 8 :
        m_x = m_x - 2
        m_y = m_y + 2

    while 1 >= m_x >= b and 1 >= m_y >= a :
        dir = random.randint(1,8)
        if dir == 1 :
            m_x = m_x + 2
            m_y = m_y
        elif dir == 2 :
            m_x = m_x - 2
            m_y = m_y
        elif dir == 3 :
            m_x = m_x
            m_y = m_y + 2
        elif dir == 4 :
            m_x = m_x
            m_y = m_y - 2
        elif dir == 5 :
            m_x = m_x + 2
            m_y = m_y + 2
        elif dir == 6 :
            m_x = m_x + 2
            m_y = m_y - 2
        elif dir == 7 :
            m_x = m_x - 2
            m_y = m_y - 2
        elif dir == 8 :
            m_x = m_x - 2
            m_y = m_y + 2

    list[c_x][c_y] = 'c'
    list[m_x][m_y] = 'm'

    for row in list:
        for elem in row:
            print(elem, end=' ')
        print()

    time.sleep(1)
    os.system('clear')
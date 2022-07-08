print(print)

el = input()
a = []
b = {}



while el != '0' :
    a.append(el)
    el = input()

for i in range(len(a)) :
    if a[i] in b :
        b[a[i]] += 1
    else :
        b[a[i]] = 1

print(b)
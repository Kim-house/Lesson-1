x = 12
if x == 0:
    print(x, "is zero")
elif x<0:
    print(x, "is negative number")
elif x>10: 
    print(x, "over ten")

for a in [1,3,5,8]:
    print(a*2, end=' ')

list (range(3,9))

b = 5
while b<10:
    print(b, end=' ')
    b += 1

for c in range (12):
    if c%2 == 0:
        continue
    print(c, end=' ')

d,e = 1,2
fx = 40
G = []
while True:
    (d,e) = (e, d+e)
    if d>fx:
        break
    G.append(d)
print(G)

max = 30
J = []
for h in range(2,max):
    for i in J:
        if h%i == 0:
            break
    else:
        J.append(h)
print(J)

tops = 25
Z = []
for x in range(2,tops):
    for y in Z:
        if x%y == 0:
            break
    else:
        Z.append(x)
print(Z)

def add(k,l):
    "function that adds 2 numbers"
    print(k+l)
add (5,6)

def multy(m,n,o):
    "function that multiplies 3 numbers"
    return(m*n*o)
print(multy(2,3,4))

def sum(p,q):
    r = p+q
    print(r)
sum(7,8)

def prime(s):
    for t in range(2,s):
        if s%t == 0:
            print (s, "is not a prime number")
            break
        else:
            print(s,"is a prime number")
        break
print(prime(5))

def fibo(u):
    y = []
    v, w = 0, 1
    while len(y)<u:
        v, w = w, v+w
        y.append(v)
    return(y)
print(fibo(10))

def fiboseq(aa, bb, dd):
    cc = []
    # bb, dd = 0, 1
    while len(cc)<aa:
        bb,dd = dd, bb+dd
        cc.append(bb)
    print(cc)

fiboseq(10, 1, 2)


add = lambda x, y: x + y
print(add(1, 2))


data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper', 'YOB':1906},
        {'first':'Alan',  'last':'Turing', 'YOB':1912}]
print(sorted(data, key=lambda item: item['first']))


def key(item):
    "function that sorts by key which is first name"
    item = ['first']
    # return (item ['first'])
    data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper', 'YOB':1906},
        {'first':'Alan', 'last':'Turing', 'YOB':1912}]
print(key)


data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper', 'YOB':1906},
        {'first':'Alan', 'last':'Turing', 'YOB':1912}]

item = 'first'

def key(item):
    "function that sorts by key which is first name"
    # item = ['first']
    # sorted(data)
    return (sorted(data, 0))

print(key(item))


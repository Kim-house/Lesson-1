def add(a, b):
    "function that adds 2 numbers"
    print(a + b)
add (2,5)

def mult(c, d, g):
    "function to multiply 3 numbers"
    return(c*d*g)
print(mult (4,3,6))

def divd(e, f):
    "function that divides 2 numbers"
    return(e/f)
print(divd (10,2))

def addnum(z, y):
    v = z+y
    return (v)
print(addnum (5,3))

def prime(m):
    J=[]
    for l in J:
       if m%l == 0:
           break
    else:
        print("is a prime number")
print(prime(5))

# def prime()
def prime_num(n):
    for i in range(2,n):
        if n%i == 0:
            print(n, "is not a prime number")
            break
        else:
            print(n, "is a prime number")
        break

prime_num(7)

add(3,4)

prime_num(17)

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


def catchall(*args, **kwargs):
    print("args=", args)
    print("kwargs=", kwargs)

catchall(3,4,5, a=6,b=7)


add = lambda x, y: x + y
print(add(1, 2))

print(sorted([4,6,7,3,1,9]))


data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper',     'YOB':1906},
        {'first':'Alan',  'last':'Turing',     'YOB':1912}]
print(sorted(data, key=lambda item: item['first']))

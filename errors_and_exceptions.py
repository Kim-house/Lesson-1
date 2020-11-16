L = [1,2,3]
print(L[4])

try:
    # print("this gets executed first")
    print(3/1)
except:
    print("this gets executed only if there is an error")

print(3/0)

def div (a, b):
    try:
        return (a/b)
    except:
        return ("not divisible")
print(div(4,0))

try:
    print(div(5,0))
except:
    print("not divisible")


def fibo (n):
    if n <= 0:
        raise ValueError("n must be greater than 0")
    J = []
    a,b = 0, 1
    while len(J)<n:
        a,b = b, a + b
        J.append(a)
    return J

print(fibo(0))


try:
    x = 1/0
except ZeroDivisionError as err:
    print("Error class is: ", type(err))
    print("Error message is:", err)
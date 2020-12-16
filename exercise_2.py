# numero = int(input("Input a number "))
# if numero % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# d = int(input("Give a number greater than 0; "))
# def fib (d):
#     L = []
#     a, b = 0, 1
#     while len(L) < d:
#         a, b = b, a+b
#         L.append (a)
#     return(L)
# print(fib(d))

# Alist = [1, 2, 2, 3, 5, 6, 6, 6, 7, 8]
# Blist = set(Alist)
# print(Blist)
# print(set(Alist))
# Clist = {2, 3, 5, 6}
# print(list(Clist))

# def setter(e):
    # F = []
    # for g in e:
    #     if g not in F:
    #         F.append(g)
    # return F

e = [1, 2, 2, 3, 4, 2, 3]
# print(setter(e))

def setters(e):
    return list(set(e))
print(setters(e))
from itertools import count

# L = (n ** 2 for n in range(12))
# print(list(L))

# M = (n ** 2 for n in range(12))
# for val in M:
#     print(val, end = ' ')

# factors = [2, 3, 5, 7]
# G = (i for i in count() if all(i % n > 0 for n in factors))
# for val in G:
#     print(val, end = ' ')
#     if val>40: break


# for i in count():
#     if i>=10: break
#     print(i)


# G= (n ** 2 for n in range(12))
# for n in G:
#     print(n, end = ' ')
#     if n > 30: 
#         # print(n, end=' ')
#         break 

# print("doing something in between")

# for n in G:
#     print(n, end = ' ')


K = (n ** 2 for n in range(12))

def gen():
    for n in range(12):
        yield n ** 2

K2 = gen()
print(*K)
print(*K2)
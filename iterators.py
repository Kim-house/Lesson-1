for i in range(10):
    print(i)

for value in [2,3,5,7,9]:
    print(value+1)

i = iter([2, 4, 6, 8])
print(next(i))

L = [2,4,6,8,10]
print(len(L))
print(range(len(L)))
for i in range(len(L)):
    print(i, L[i])
for i in L:
    print(i)

R = [3, 6, 9, 12, 15]
# for x, y in zip (L, R):
#     print(x, y)
z = zip(L, R)
# print(*z)

M, N = zip(*z)
print(M, N)


square = lambda x: x ** 2
for z in map(square, range(10)):
    print(z)

is_even = lambda x: x%2==0
for z in filter(is_even, range(10)):
    print(z)


from itertools import permutations
p = permutations(range(3))
print(*p)

from itertools import combinations
c = combinations(range(4), 2)
print(*c)

from itertools import product
e = product('ab', range(3))
print(*e)
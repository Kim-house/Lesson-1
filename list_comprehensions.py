# a = [n ** 2 for n in range (12)]
# print(a)

# b = [(i, j, k) for i in range(2) for j in range(3) for k in range(4)]
# print(b)

# for i in range(2):
#     print(i, end = ' ')

# for j in range(3):
#     print(j, end = ' ')

# l = [m for m in range(20) if m%3>0]
# print(l)

# p = -10
# if p >= 0:
#     print(p)
# else: 
#     print(-p)

# r = -12
# r if r >=0 else -r
# print(r)


# for val in range(20):
#     val if val % 2 else -val
#     print(val, end = ' ')

# for val in range(20):
#     if val % 3 > 0:
#         print(val, end = ' ')

t = [val if val % 2 else -val for val in range(20) if val %3]
print(t)


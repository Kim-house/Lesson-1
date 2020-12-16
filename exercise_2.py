# EXERCISE on odd and even numbers
# numero = int(input("Input a number "))
# if numero % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")


# EXERCISE on fibonacci sequence
# d = int(input("Give a number greater than 0; "))
# def fib (d):
#     L = []
#     a, b = 0, 1
#     while len(L) < d:
#         a, b = b, a+b
#         L.append (a)
#     return(L)
# print(fib(d))


# EXERCISE on sets, converting list to set, using function to skip repeated elements
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

# e = [1, 2, 2, 3, 4, 2, 3]
# print(setter(e))

# def setters(e):
#     return list(set(e))
# print(setters(e))


# USE of is
# x = 10
# y = x
# print(x is y)


# EXERCISE on rock-paper-scissors game
# play1 = input("Rock, paper or scissors? ")
# play2 = input("Rock, paper or scissors? ")

# def rps(play1, play2):
#     if play1 == play2:
#         return("it's a tie")
#     if play1 == 'rock':
#         if play2 == 'scissors':
#             return("play1 wins")
#         else:
#             return("play2 wins")

#     elif play1 == "scissors":
#         if play2 == "paper":
#             return("play1 wins")
#         else:
#             return("play2 wins")
    
#     elif play1 == "paper":
#         if play2 == "rock":
#             return("play1 wins")
#         else:
#             return("play2 wins")

# print(rps(play1, play2))

# p = 5
# while p<10:
#     print (p)
#     p += 1

# quit = input('Type "enter" to quit:' )
# while quit != "enter":
#     quit = input('Type "enter" to quit:' )
#     print(quit)

# q = 4
# while True:
#     r = q +1
#     if r<10:
#         break
# print(r)

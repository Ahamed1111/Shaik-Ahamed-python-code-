# N = 10000
# a = 0
# b = 1
# c = 0

# fib_series = [a, b]


# while True:
#     c = a + b 0+1 1 +1 3
#     a = b
#     b = c
#     print("The value of a", a)
#     print("The value of b", b)
#     print("The value of C", c)
#     if c > N:
#         break
#     fib_series.append(c)

# print(','.join(map(str, fib_series)))



n = 10  # number of terms to generate
a, b = 0, 1  # initialize the first two terms
fib_series = [a, b]  # create a list to store the sequence

for i in range(2, n):
    print(i)
    c = a + b  # calculate the next term
    fib_series.append(c)  # add the next term to the list
    a, b = b, c  # update a and b for the next iteration

print(fib_series)

# print numbers from 1 to 10 using while loop

def printFrom1ToN(n):
    i = 1
    while(i <= n):
        print(i)
        i += 1

def sumFrom1toN(n):
    i = 1
    total = 0
    while(i <= n):
        total += i 
        i += 1
    return total

def sumOfEvenNumbers1toN(n):
    i = 1
    total = 0

    while (i <= n):
        if i % 2 == 0:
            total += i
            i += 2
        else:
            i += 1
    return total







# print(sumOfEvenNumbers1toN(10)) # total even numbers from 1 to 10 -> 2, 4, 6, 8, 10

# print(sumFrom1toN(8))


# printFrom1ToN(10)


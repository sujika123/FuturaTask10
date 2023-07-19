# square pattern
print('square pattern')
for i in range(5):
    for j in range(5):
        print(j + 1, end=' ')
    print()  # new line


print()
# Left triangle pattern
print("Left triangle pattern")
n = 5
for i in range(n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

print()
# Inverted Left triangle pattern
print('Inverted Left triangle pattern')
n = 5
for i in range(n,0,-1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()


# Left triangle pattern
n = 5
for i in range(n+1):
    for j in range(1, i+1):
        print(i, end=' ')
    print()


print()
# Left triangle pattern
n = 5
for i in range(n,0,-1):
    for j in range(1, i+1):
        print(i, end=' ')
    print()

print()
# right triangle pattern
print('right triangle pattern')
size = 5
for i in range(size):
    for j in range(1, size - i):
        print(" ", end="")
    for k in range(1, i + 2):
        print(k, end='')
    print()





print()
# pyramid number pattern
print('pyramid number pattern')
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(k + 1, end='')
    print()


print()
# reverse pyramid pattern
print("reverse pyramid pattern")
n = 5

for i in range(n):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(n-i)-1):
        print(j+1, end='')
    print()



print()
# right pascal
print('right pascal')
n = 5

# upper triangle
for i in range(n):
    for j in range(i + 1):
        print(j+1, end="")
    print()
# lower triangle
for i in range(n):
    for j in range(n - i - 1):
        print(j+1, end="")
    print()



print()

# diamond number pattern
print('diamond number pattern')
n = 5

# upward pyramid
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print(j+1, end='')
    print()

# downward pyramid
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        print(j+1, end='')
    print()



print()
#Multiplication table pattern
print('Multiplication table pattern')
rows = 10
# rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()


print()
#Reverse Pyramid of Numbers
print('Reverse Pyramid of Numbers')
rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")


print()
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()


print()
#Number triangle pattern
print('Number triangle pattern')
rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")


print()
#Unique pyramid pattern of digits
print('Unique pyramid pattern of digits')
rows = 6
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()



print()
#Number reduction pattern
print('Number reduction pattern')
rows = 5
for i in range(0, rows + 1, 1):
    for j in range(i + 1, rows + 1, 1):
        print(j, end=' ')
    print()
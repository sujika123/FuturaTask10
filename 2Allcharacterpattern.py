#square alphabet pattern
print('square alphabet pattern')
size = 5
count = 0

for i in range(size):
    for j in range(size):
        print(chr(65 + count), end=" ")
        # changing charater
        count += 1
    print()



print()
# square alphabet pattern

size = 5

for i in range(size):
    for j in range(size):
        print(chr(65 + i), end=" ")
    print()



print()
# square alphabet pattern

size = 5

for i in range(size):
    for j in range(65, 65+size):
        print(chr(j), end=' ')
    print()


print()
# Left triangle pattern
print('Left triangle pattern')
n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(j + 65), end=" ")
    print()


print()
# right triangle pattern
print('right triangle pattern')
size = 5
for i in range(size):
    for j in range(1, size - i):
        print(" ", end="")
    for k in range(i + 1):
        print(chr(65 + k), end="")
    print()


print()
#repeated alphabet patterns
print('repeated alphabet patterns')
# outer loop for ith rows
for i in range (65,70):
    # inner loop for jth columns
    for j in range(65,i+1):
        print(chr(i),end="")
    print()


print()
print('alphabet pattern')
asciichr = 65
# outer loop for ith rows
for i in range(0,6):
    # inner loop for jth columns
    for j in range(0,i+1):
        char = chr(asciichr)
        print(char,end="")
        asciichr += 1
    print()

print()
# pyramid alphabet pattern
print('pyramid alphabet pattern')
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(chr(65 + k), end='')
    print()


print()
# reverse pyramid pattern
print('reverse pyramid pattern')
n = 5

for i in range(n):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
    print()


print()
# diamond alphabet pattern
print('diamond alphabet pattern')
n = 5

# upward pyramid
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print(chr(65 + j), end='')
    print()

# downward pyramid
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        print(chr(65 + j), end='')
    print()



print()
# right pascal triangle
print('right pascal triangle')
n = 5

# upper triangle
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end="")
    print()
# lower triangle
for i in range(n):
    for j in range(n - i - 1):
        print(chr(65 + j), end="")
    print()



print()
#Pattern to display letter of the word
print('Pattern to display letter of the word')
word = "Python"
x = ""
for i in word:
    x += i
    print(x)
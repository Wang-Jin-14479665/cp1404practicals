for i in range(1, 21, 2):
    print(i, end=' ')
print()

# A
for i in range(10, 101, 10):
    print(i, end=' ')
print()

# B
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C
num_of_str = int(input("What is the number of star:"))

for i in range(num_of_str):
    print("*", end=' ')
print()

# D
num_of_line = int(input("How many lines:"))

for i in range(1, num_of_line + 1):
    print("*" * i)
print()
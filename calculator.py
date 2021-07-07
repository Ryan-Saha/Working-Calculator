first = input("1: ")
asmd = input("asmd: ")
second = input("2: ")
a = '+'
s = '-'
m = '*'
# addition

if asmd == a:
    print(float(first) + float(second))

# subtraction

elif asmd == s:
    print(float(first) - float(second))

# multiplication

elif asmd == m:
    print(float(first) * float(second))

# division

else:
    print(float(first) / float(second))

def rev(n):
    if (len(n) <= 0):
        return n
    else:
        return rev(n[1:]) + n[0]


name = "abcde"
val = rev(name)
print(val)

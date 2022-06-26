# Time - O(n)
# Space - O(N)  -> array
def addBinary(a, b):
    result = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:  # means that we have a bit
            total = total + int(a[i])
            i = i - 1
        if j >= 0:  # means that we have a bit
            total = total + int(b[j])
            j = j - 1
        result.append(str(total % 2))
        carry = total // 2
    return ''.join((reversed(result)))


value = addBinary("11","1")

print(value)
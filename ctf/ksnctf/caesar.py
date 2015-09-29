import string
sample = "fvzcyr"

result = []

for y in range(1,27):
    for x in range(len(sample)):
        check = ord(sample[x]) + y
        if check > 122:
            check = check - 26
        result.append(chr(check))
    print "".join(result)
    result = []

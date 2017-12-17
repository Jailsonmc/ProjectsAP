

print(str(chr(97)))

print(ord("a"))

for i in range(97, 123):
    if i == 122:
        print(str(chr(i)),end="")
    else:
        print(str(chr(i)+"-"),end="")
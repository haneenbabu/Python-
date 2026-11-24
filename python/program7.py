s = input("Enter a string: ")
fchar = s[0]
s = fchar + s[1:].replace(fchar, '$')
print(s)
columnNumber =2147483647
output = ""
while columnNumber > 0:
    output = chr(ord('A') + (columnNumber - 1) % 26) + output
    columnNumber = (columnNumber - 1) // 26
print(output)
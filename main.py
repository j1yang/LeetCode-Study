res = str("A man, a plan, a canal: Panama").lower()
stack = []

for i in res:
    if i.isalnum():
        stack.append(i)
print(stack)

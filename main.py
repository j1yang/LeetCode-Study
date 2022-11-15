n = 19
x = n

if n <= 9 and n >1:
            print("false")
else:
  while True:
    s = list(str(x))
    sum = 0
    print(s)
    for i in s:
      sum += int(i)**2

    if sum <= 9 and sum >1:
      print('false')
      break
    elif sum == 1:
      print("true")
      break
    else:
      x = str(sum)

# if n <= 9 and n >1:
#             print("false")
# else:
#     s = list(str(n))
#     sum = 0
#     print(s)
#     for i in s:
#       print(int(i)**2)
#       sum += int(i)**2

#     print("sum: "+ str(sum))
#     if sum <= 9 and sum >1:
#       print('false')
#     elif sum == 1:
#       print("true")
#     else:
      
#       s = list(str(sum))
#       print(s)
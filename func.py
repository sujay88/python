list = [3,4,88,5,1,66,7]

g = 0
s = 0

for i in list:
    if i > g:
      #  s = g
        g = i
    if i < g and i > s:
        s = i
print(s+g)

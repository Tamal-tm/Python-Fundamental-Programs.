# Using Enumerate Method

l=[34,65,12,4,90,78,43]
for index, value in enumerate(l, start=1):
    print(index, "-", value)

# Not Using Enumerate Method

l=[34,65,12,4,90,78,43]

for i in range(len(l)):
    v=l[i]
    print(i, v)
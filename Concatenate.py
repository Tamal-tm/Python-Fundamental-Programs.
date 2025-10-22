# Using + Operator
'''
l1=[4,6,25,"9-Porsche"]
l2=["Portugal",45,90]

l3=l1+l2
print(l3)
'''
# Using Unique Values

l1=[4,6,25,"9-Porsche","Portugal",89]
l2=["Portugal",45,90,4,6,25]

l3=set(l1+l2)
print(l3) # In set. 

l3=list(set(l1+l2))
print(l3) # In list.

# Using Extend function

l1.extend(l2)

print(l1)


# Collection: Single variable to store multiple values. 

# List  = [] Ordered and changeable. Duplicates OK.
# Set   = {} Ordered and immutable, but add/remove OK. No Duplicatess.
# Tuple = () Ordered and unchangeable. Duplocates OK. Faster.


# List
fruits=["apple","banana","orange","grape"]
print(fruits[::2])

for fruit in fruits:
    print(fruit)

# print(dir(fruits))
# (help(fruits)) To get information on all the functions you can perform on list. 
print("orange" in fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print("/////////////////////")

# Set --> Works well with constants. 
fruits={"apple","banana","orange","grape"}
print(fruits)

# print(dir(fruits)) # All methods. 

fruits.add("pineapple")
fruits.remove("apple")
for fruit in fruits:
    print(fruit)
print("////////////////////")

# Tuple
fruits=("apple","banana","orange","grape")
# print(help(fruits))
print(fruits.index("apple"))
print(fruits.count("grape"))
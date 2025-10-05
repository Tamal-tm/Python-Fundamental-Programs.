import random, itertools # Modules for shuffle. 
                         # To obtan each cars, we will use itertools.

deck=list(itertools.product(range(1,14),["Spade","Club",'Hearts',"Diamond"]))
print(deck) # Will print a list of deck tuples. Ordered.

random.shuffle(deck)

print(deck)

for i in range(5):
    print(deck[i][0], "of", deck[i][1])
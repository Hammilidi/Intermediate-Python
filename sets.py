myset = {1, 2, 3}
print(myset)

myset.add(4)
myset.add(5)
myset.add(6)

myset.discard(3)  # remove the element if not found, nothing will happen
last = myset.pop()  # remove and return the last element


odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = evens.intersection(primes)
print(i)


setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

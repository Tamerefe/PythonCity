#kume = set([1,2,3,4,5])

#kume.discard(6)
#kume.remove(5)

#kume.add(6)
#kume.add("Tamer")

#print(kume)

a = set([1,2,3,4,5])

b = set([5,6,7,8,9])

print(a)
print(b)

print(a.difference(b))
print(a.intersection(b))
print(a.isdisjoint(b))
print(a.symmetric_difference(b))
print(a.difference_update(b))

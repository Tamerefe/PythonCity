def giveSquare(x):
    return x**2

print(giveSquare(5))

nums = [*range(1,6)]

for index in range(len(nums)):
    nums[index] = giveSquare(nums[index])
print(nums)

nums2 = [*range(1, 6)]

print([*map(giveSquare, nums2)])

def doublenumsfilter(x):
    if x % 2 == 0:
        return x
    

print(doublenumsfilter(3))
print(doublenumsfilter(4))


def doublenumsfilter2(x):
    return x if x % 2 == 0 else None

nums3 = [*range(1, 6)]

print([*filter(doublenumsfilter2,nums3)])

print(list(map(lambda num: num**2, nums3)))

print([*filter(lambda x: x if x % 2 == 0 else None,nums3)])
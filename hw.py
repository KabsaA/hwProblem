
# Practice Problem #1

''' Given a list of n numbers , determine
if it contains any duplicate numbers.'''


lst = []

def duplicates(nums):
    for i in nums:
        for j in i:
            if j == i:
                j.append(i)
    return lst

print(duplicates([1,2,2,3,4,5]))

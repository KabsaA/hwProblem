
# Practice Problem #1

''' Given a list of n numbers , determine
if it contains any duplicate numbers.'''



def duplicates(nums,x):
    count = 0
    for i in nums:
        if (i == x):
            count = count + 1
    return str(x) + " occurs " + str(count) + " times."


print(duplicates([1,2,2,3,4,5],2)) # 2
print(duplicates([1,2,2,3,4,5,5,5],5)) # 3
print(duplicates([1,2,2,3,4,5,5,5],0)) # 0
#first commit didn't solve problem
#there was a type error couldn't iterate over int

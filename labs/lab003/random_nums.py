import random

def genRanNums(amount):
    ran_nums = []
    for x in range(0,amount):
        random.seed()
        ran_nums.append(random.randint(0,100))
    return ran_nums


def maxInArray(arr):
    curr_max = -1
    for x in range(0, len(arr)):
        if curr_max < arr[x]:
            curr_max = arr[x]
    return curr_max

user_in = int(input('How many random numbers do you wish to generate? '))
random_nums = genRanNums(user_in)
print('Generated the numbers ' + ', '.join(str(e) for e in random_nums))

print('Got the max number ' + str(maxInArray(random_nums)))

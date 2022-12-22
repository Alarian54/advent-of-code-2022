# Setup
file = open('../data/data20.txt', 'r')
nums = list(map(int, file.read().split("\n")))
file.close()

leng = len(nums)
indices = list(range(leng))

def mix(nums, indices, leng):
    for i in list(range(leng)):
        index = indices.index(i)
        num = nums[index]
        if num == 0: continue
        newIndex = ((index + num - 1) % (leng-1)) + 1
        if index == newIndex:
            pass
        elif index < newIndex:
            nums = nums[:index] + nums[index+1:newIndex+1] + [num] + nums[newIndex+1:]
            indices = indices[:index] + indices[index+1:newIndex+1] + [i] + indices[newIndex+1:]
        else:
            nums = nums[:newIndex] + [num] + nums[newIndex:index] + nums[index+1:]
            indices = indices[:newIndex] + [i] + indices[newIndex:index] + indices[index+1:]
    return nums, indices

# Part 1
nums1, indices1 = mix(nums, indices, leng)
zeroIndex = nums1.index(0)
total = 0
for i in range(1, 4):
    ans = nums1[(zeroIndex + (1000*i)) % leng]
    total += ans
print(total)

# Part 2
for i in range(leng):
    nums[i] *= 811589153

for i in range(10):
    nums, indices = mix(nums, indices, leng)

zeroIndex = nums.index(0)
total = 0
for i in range(1, 4):
    ans = nums[(zeroIndex + (1000*i)) % leng]
    total += ans
print(total)
def findLargestNum(nums):
    max = nums[0]
    for item in nums:
        if item > max :
            max = item
    return max

if __name__ == '__main__':
    print(findLargestNum([45,2,5,77,89,123,3,57]))
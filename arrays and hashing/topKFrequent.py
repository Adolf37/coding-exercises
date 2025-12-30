# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]

def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for num, cnt in count.items():
            freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res
        
        

nums = [1,2,2,3,3,3,1, 1, 4]
k = 2   
print(topKFrequent(nums, k))
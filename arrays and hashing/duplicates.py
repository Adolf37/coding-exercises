#Return true if the list has any duplicates

import time

nums=[21,22,23,24,25,26,27,28,29,30,11,31,32,33,34,35,36,37,38,39,11,40]
nums2 = [i for i in range(1_000_000)]

def optimalHasDuplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

def duplicateShort(nums):
    return len(set(nums)) < len(nums)

start_time = time.perf_counter()
duplicateShort(nums2)
end_time = time.perf_counter()

print(f"Runtime {end_time - start_time:.7f} second")
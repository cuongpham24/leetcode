"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Find unique element
        unique = {}
        for num in nums:
            unique[num] = unique.get(num, 0) + 1
        max_count = 0
        major_element = 0
        for num in unique:
            if unique[num] > max_count:
                max_count = unique[num]
                major_element = num
        return major_element
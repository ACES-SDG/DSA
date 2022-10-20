from typing import List


class Solution:
    def twoSum(self,nums :List[int],target:int) -> List[int]:
        
        hashmap = {}
        for index , number in enumerate(nums):
            num = target - number
            if num in hashmap:
                return [hashmap[num],index]
            hashmap[number]=index

class_obj = Solution()
answer = class_obj.twoSum([3,3],6)





print(answer)
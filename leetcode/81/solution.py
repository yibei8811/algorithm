from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        start = 0
        end = n - 1
        while start <= end:
            mid = (end + start)//2
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid] == nums[end]:
                start += 1
                end -= 1
            # 此处判断的 唯一 bug 是因为[3,1,3,3,3,3] 会将前半部分 判断为有序
            # 而满足bug的条件，必然 是 mid后的所有数据等于mid
            # 所以 需要上面一个初始判断
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False


print(Solution().search([1,0,1,1,1],0))

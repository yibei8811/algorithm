class Solution:
    @staticmethod
    def solve(lst, k):
        return Solution.find(lst, 0, len(lst), k)

    @staticmethod
    def find(lst, start, end, k):
        mid = start + (end-start)//2
        if lst[mid] < k:
            return Solution.find(lst,mid+1, end, k)
        elif lst[mid] > k:
            return Solution.find(lst, start, mid-1, k)
        else:
            start = mid
            end = mid
            while start - 1 >= 0 and lst[start-1] == k:
                start -= 1
            while end + 1 < len(lst) and lst[end+1] == k:
                end += 1
        return end - start + 1


lst = [1,2,2,3,3,3,3,4,4,4,5,5,5,5,5,5,5]
print(Solution.solve(lst, 1))
print(Solution.solve(lst, 2))
print(Solution.solve(lst, 3))
print(Solution.solve(lst, 4))
print(Solution.solve(lst, 5))


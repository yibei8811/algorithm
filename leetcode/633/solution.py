class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(c+1):
            a = i * i
            if a <= c:
                expect = c - a
                start = 0
                end = c
                while start <= end:
                    mid = (start + end) // 2
                    val = mid * mid
                    if val == expect:
                        return True
                    if val < expect:
                        start = mid + 1
                    elif val > expect:
                        end = mid - 1
            else:
                break
        return False


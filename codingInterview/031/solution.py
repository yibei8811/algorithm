class Solution:
    @staticmethod
    def solve(lst1, lst2):
        # start end step
        # but when step = -1
        # eg: [len(lst1)-1,0,-1]
        # index 0 is not output
        # maybe only use [len(lst1)-1,,-1]
        stack = lst1[len(lst1)-1::-1]
        lst1.clear()
        while len(lst2) > 0:
            result = False
            data2 = lst2.pop(0)
            if len(lst1) > 0:
                if lst1[-1] == data2:
                    lst1.pop(-1)
                    continue
            while len(stack) > 0:
                data1 = stack.pop(-1)
                if data1 == data2:
                    result = True
                    break
                else:
                    lst1.append(data1)
            if result is False:
                return False
        return True


lst1 = [1,2,3,4,5,6]
# lst2 = [4,6,5,3,2,1]
# lst2 = [4,5,6,3,2,1]
lst2 = [4,2,6,3,5,1]
print(Solution.solve(lst1, lst2))

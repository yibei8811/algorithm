class Solution:
    @staticmethod
    def solve(var_str):
        count = 0
        tail = len(var_str)
        for i in range(tail):
            if var_str[i] == ' ':
                count += 1
        if count != 0:
            # 【var_str[i + 1 + 2 * count:tail + 2 * count]】 python自动扩充长度
            # for i in range(count):
            #     var_str.extend(['x','x'])
            for i in range(0, len(var_str))[::-1]:
                if var_str[i] == ' ':
                    # 因为原来有一个空格，所以每替换一个空格，增加2个length，所以是2*count
                    var_str[i + 1 + 2 * count:tail + 2 * count] = var_str[i + 1:tail]
                    var_str[i - 2 + 2 * count:i + 1 + 2 * count] = ['%','2','0']
                    tail = i
                    count -= 1
        return var_str


var_list = ['w','e',' ','a','r','e',' ','t','h','e',' ','p','e','o','p','l','e']
print(Solution.solve(['w','e',' ','a','r','e',' ','t','h','e',' ','p','e','o','p','l','e']))

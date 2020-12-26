# https://www.nowcoder.com/questionTerminal/178b912722ac42a2865057a66d4e7de2
# 给你六种面额 1、5、10、20、50、100 元的纸币，
# 假设每种币值的数量都足够多，
# 编写程序求组成N元（N为0~10000的非负整数）
# 的不同组合的个数。
# 分析很好
# https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-iihe-pa-lou-ti-wen-ti-dao-di-yo/
# 不允许在后面的硬币层次使用之前的硬币。 这就像排列中2,2,1; 2,1,2是两种情况，
# 但是组合问题规定好了一种书写顺序，比如大的写在前面那就只有2,2,1这一种情况了。
# https://leetcode-cn.com/problems/coin-change-2/solution/bei-bao-si-xiang-jie-jue-ling-qian-dui-huan-wen-ti/
# https://leetcode-cn.com/problems/coin-change-2/solution/dong-tai-gui-hua-wan-quan-bei-bao-wen-ti-by-liweiw/


def solution(n):
    money = [1, 5, 10, 20, 50, 100]
    dp = [0] * (n + 1)
    dp[0] = 1
    for j in range(1, n+1):
        for i in money:
            if j >= i:
                dp[j] += dp[j-i]
    return dp[n]


print(solution(eval(input())))


# dp[6]= dp[5]+dp[1]
# dp[5] 有2种方式 1个5 和 5个1 。
# dp[5] 中的 1个5  + 1coin
# dp[1] 中的 1个1  + 5coin
# 以上会有重复问题


# 仅仅把循环掉一下位置，就去重了
# 这种题目值得研究和分享
# 第一轮循环i，money in [1]，dp[面额]都只有一种方式
# 第二轮循环i，money in [1,5], dp[面额] = dp[面额] + dp[面额-5]，且可以保证不重复，
# 因为只存在1和5，不存在5和1
# ......
# DP[j]表示的是对于第i个硬币能凑的组合数
# 不允许在后面的硬币层次使用之前的硬币。 这就像排列中2,2,1; 2,1,2是两种情况，
# 但是组合问题规定好了一种书写顺序，比如大的写在前面那就只有2,2,1这一种情况了。
def solution(n):
    money = [1, 5, 10, 20, 50, 100]
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in money:
        for j in range(1, n+1):
            if j >= i:
                dp[j] += dp[j-i]
    return dp[n]


print(solution(eval(input())))


def solution(n):
    money = [1, 5, 10, 20, 50, 100]
    m = len(money)
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp[0][0] = 1
    for i in range(m+1):  # 可以不需要
        dp[i][0] = 1      # 可以不需要
    try:
        for i in range(1,m+1):
            for j in range(0, n+1):
                if j >= money[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-money[i-1]]
                    #         不用这个金币 组合这个金额的组合数
                    #       + 用这个金币   组合（金额-面值）的组合数
                else:
                    dp[i][j] = dp[i-1][j]  # 不用这个金币 组合这个金额的组合数
    finally:
        # print('finally')
        # print(i)
        # print(j)
        pass
    return dp[m][n]


print(solution(eval(input())))

# 完全 or 不完全背包，是组合面值
# 可以小于面值 就是不完全

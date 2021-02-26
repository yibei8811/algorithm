from typing import List


class Solution:
    def findNumOfValidWords2(self, words: List[str], puzzles: List[str]) -> List[int]:
        words.sort()
        ans = [0] * (len(puzzles))
        for (i, puzzle) in enumerate(puzzles):
            count = 0
            for word in words:
                if puzzle[0] not in word:
                    continue
                success = 1
                for w in word:
                    if w not in puzzle:
                        success = 0
                        continue
                if success == 1:
                    count += 1
            ans[i] = count
        return ans

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # 压缩 word 并计数
        w_b_count = {}
        for word in words:
            w_b = 0
            for w in word:
                w_b |= (1 << (ord(w) - ord('a')))
            if w_b not in w_b_count:
                w_b_count[w_b] = 1
            else:
                w_b_count[w_b] += 1

        ans = [0] * (len(puzzles))
        for (i, puzzle) in enumerate(puzzles):
            count = 0
            # 从第二位 开始压缩 puzzle
            w_b = 0
            for w in puzzle[1:]:
                w_b |= (1 << (ord(w) - ord('a')))
            # 求 word中 每个字母 在puzzle中
            # 即是求 word 压缩后的 2进制 和 puzzle 任意一个子集有相同的2进制
            sub = w_b
            while sub:
                s = sub | (1 << (ord(puzzle[0]) - ord("a")))
                if s in w_b_count:
                    count += w_b_count[s]
                sub = (sub - 1) & w_b
            if 1 << (ord(puzzle[0]) - ord("a")) in w_b_count:
                count += w_b_count[1 << (ord(puzzle[0]) - ord("a"))]
            ans[i] = count
        return ans


print(Solution().findNumOfValidWords(["aaaa","asas","able","ability","actt","actor","access"],["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))
print(Solution().findNumOfValidWords2(["aaaa","asas","able","ability","actt","actor","access"],["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))

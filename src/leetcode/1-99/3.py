'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        left和right索引（左闭右闭）
        哈希表存遍历过的right索引处所指向的字符的信息
        时间复杂度：O(n)
        '''
        left = 0
        right = 0
        record = {}
        max_len = 0

        while right < len(s):
            if s[right] in record:
                # 不取max的badcase: 'abba'，此时遇到最后一个a的时候left会往左跑！
                left = max(record[s[right]] + 1, left)

            max_len = max(max_len, right - left + 1)
            record[s[right]] = right
            right += 1

        return max_len


if __name__ == '__main__':
    test = Solution()
    test_case = 'abba'
    print(test.lengthOfLongestSubstring(test_case))

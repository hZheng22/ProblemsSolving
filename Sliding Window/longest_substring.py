"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

'''
Brute Force
time complexity O(n^3)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def allUnique(s):
            count = {}
            for i in s:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
            for i in count:
                if count[i] > 1:
                    return False
            return True

        ans = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                print(s[i:j + 1])
                if (allUnique(s[i:j + 1])):
                    ans = max(ans, (j - i + 1))
        return ans

'''
sliding window

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mdict = {}
        ans = 0
        i = 0
        for j in range(len(s)):
            if s[j] in mdict:
                i = max(mdict[s[j]], i)

            ans = max(ans, j - i + 1)
            mdict[s[j]] = j + 1

        return ans

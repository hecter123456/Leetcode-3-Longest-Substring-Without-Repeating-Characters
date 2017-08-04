import unittest

class unitest(unittest.TestCase):
    def testEmptyStr(self):
        inputStr = ""
        ans = 0
        self.assertEqual(Solution().lengthOfLongestSubstring(inputStr),ans);
    def testFirst(self):
        inputStr = "abcabcbb"
        ans = 3
        self.assertEqual(Solution().lengthOfLongestSubstring(inputStr),ans);
    def testRepeatEnd(self):
        inputStr = "cdd"
        ans = 2
        self.assertEqual(Solution().lengthOfLongestSubstring(inputStr),ans);

class Solution():
    def lengthOfLongestSubstring(self, s):
        ans = start = 0
        dic = {}
        for index,item in enumerate(s):
            if item in dic and start <= dic[item]:
                start = dic[item] + 1
            else:
                ans = max(ans,index - start + 1)
            dic[item] = index
        return ans

if __name__ == '__main__':
    unittest.main()

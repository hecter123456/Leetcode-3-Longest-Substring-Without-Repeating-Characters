import unittest

class unitest(unittest.TestCase):
    def testEmptyStr(self):
        inputStr = ""
        ans = 0
        self.assertEqual(Solution().lengthOfLongestSubstring(inputStr),ans);

class Solution():
    def lengthOfLongestSubstring(self, s):
        if(s == ""):
            return 0

if __name__ == '__main__':
    unittest.main()

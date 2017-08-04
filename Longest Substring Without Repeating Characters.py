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
        if(s == ""):
            return 0
        ans = 0
        val = 0
        dic = {}
        index = 0
        for item in s:
            if item in dic:
                ans = max(val,ans)
                for dicitem in dict(dic):
                    if dic[dicitem] < dic[item]:
                        val -= 1
                        del dic[dicitem]
            else:
                val += 1
            dic[item] = index
            index +=1
        return max(val,ans)

if __name__ == '__main__':
    unittest.main()

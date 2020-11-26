class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i],s[len(s)-1-i] = s[len(s)-1-i], s[i]

def main():
    rev1 = ["h","e","l","l","o"]
    rev2 = ["H","a","n","n","a","h"]
    Solution().reverseString(rev1)
    print(rev1)
    Solution().reverseString(rev2)
    print(rev2)

if __name__ == "__main__":
    main()
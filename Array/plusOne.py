class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) < 2 and digits[0] == 9:
            return [1,0]
        elif digits[-1] <9:
            digits[-1]+=1
            return digits
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
            return digits

def main():
    digits = [1,2,3]
    print(Solution().plusOne(digits))
    digits = [0,0]
    print(Solution().plusOne(digits))
    digits = [9,9,9]
    print(Solution().plusOne(digits))
    digits = [9]
    print(Solution().plusOne(digits))
    digits = [0,9]
    print(Solution().plusOne(digits))

if __name__ == "__main__":
    main()
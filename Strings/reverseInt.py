class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = str(x)
        nums = num.strip().split()

        print(nums)

        return 0


def main():
    x = 123
    y = -123
    print(Solution().reverse(x))
    print(Solution().reverse(y))

if __name__ == "__main__":
    main()
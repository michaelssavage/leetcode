class Solution(object):
    def containDuplicate(self, nums):
        seen = []
        for i in nums:
            if i in seen:
                return True
            else:
                seen.append(i)
        return False


def main():
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(Solution().containDuplicate(nums))

if __name__ == "__main__":
    main()
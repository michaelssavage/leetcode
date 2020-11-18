from collections import defaultdict

class Solution(object):
    
    # using a list has o(n^2) time complexity
    def singleNumber(self, nums):
        seen = []
        for i in nums:
            seen.append(i) if i not in seen else seen.remove(i)

        return seen[0]

    # Using a hashing table has o(n)
    def singleNumber2(self, nums):
        seenHash = defaultdict(int)
        for i in nums:
            seenHash[i] += 1

        for i in seenHash:
            if seenHash[i]==1:
                return i

def main():
    nums = [4,1,2,1,2]
    print(Solution().singleNumber(nums))

    nums2 = [1]
    print(Solution().singleNumber2(nums2))

if __name__ == "__main__":
    main()
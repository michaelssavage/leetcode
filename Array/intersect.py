from collections import defaultdict

class Solution(object):
    def intersect(self, nums1,nums2):
        seen = dict()
        for i in nums1:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        intersect = []
        for i in nums2:
            if i in seen and seen[i] >0:
                intersect.append(i)
                seen[i]-=1
        return intersect

    def intersect2(self, nums1, nums2):
        result, amount = [], defaultdict(int)

        # each number added.
        for n in nums1:
            amount[n] += 1

        # each number, append to result.
        for n in nums2:
            if amount[n] > 0: 
                result.append(n)
                amount[n] -= 1
        return result

def main():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(Solution().intersect2(nums1,nums2))

if __name__ == "__main__":
    main()
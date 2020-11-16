class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        return nums[(len(nums)-k):] + nums[:(len(nums)-k)]

    def rotate2(self, nums, k):
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
            
        nums[:] = a

def main():
    # length = 7
    nums = [1,2,3,4,5,6,7]
    k = 3
    # my solution
    print(f"Using list manipulation, {nums} with {k} rotations = {Solution().rotate(nums,k)}")

    # o(n) solution
    print(f"Using modulation, {nums} with {k} rotations = ",end="")
    Solution().rotate2(nums,k)
    print(nums)

    #length = 4
    nums2 = [-1,-100,3,99]
    j = 2
    print(f"\n\nUsing list manipulation, {nums2} with {j} rotations = {Solution().rotate(nums2,j)}")
    print(f"Using modulation, {nums2} with {j} rotations = ",end="")
    Solution().rotate2(nums2,j)
    print(nums2)


if __name__ == "__main__":
    main()
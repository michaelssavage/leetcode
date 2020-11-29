class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        i = 1
        while i < len(nums):
            if nums[j] == 0:
                if nums[i] != 0:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    j+=1
                    i+=1
                else:
                    i+=1
            else:
                j+=1
                i+=1
        return nums


    # really simple, if 0 seen then pop it out and append to the end.
    def moveZeroes2(self, nums):
        for i in range(len(nums))[::-1]:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
        return nums

def main():
    nums = [0,1,0,3,12]
    # print(f"Solution = {Solution().moveZeroes(nums)}")

    nums3 = [1,0,0,3,3]
    # print(Solution().moveZeroes(nums2))

    nums2 = [1,0,0,3,0,7,6,3]
    print(Solution().moveZeroes2(nums2))

    nums2 = [0,3]
    print(Solution().moveZeroes2(nums2))

if __name__ == "__main__":
    main()
def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    listlen = removeDuplicates(nums)
    i = 0
    while i < listlen:
        print(nums[i])
        i+=1


def removeDuplicates(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i += 1
    return len(nums)


if __name__ == "__main__":
    main()

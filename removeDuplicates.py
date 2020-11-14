def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    listlen = removeDuplicates(nums)
    i = 0
    new=[]
    while i <= listlen:
        new.append(nums[i])
        i+=1
    print(new)


def removeDuplicates(nums):
    length = len(nums)
    if length == 0:
        return 0
    i = 1
    j = i
    new = nums[0]
    while i < length:
        #if next number is not the same
        if(nums[i] != new):
            new = nums[i]
            nums[j] = nums[i]
            j+=1
        i+=1
    return new


if __name__ == "__main__":
    main()

def main():
    nums = [5,4,7,2]
    target = 7
    print(twoSum(nums,target))

def twoSum(nums, target):

    # add values to dictionary with index
    # if input = [2,7,11,15]
    #then dictionary = {2,0;7,1;11,2;15,3}
    num_dict = dict()
    for i,key in enumerate(nums):
        num_dict[key] = i

    result = []
    for i in range(len(nums)):

        #num_dict keys
        x = nums[i]

        #x + y = target so
        y = target - x
        y_value = num_dict.get(y,None)

        if y_value is not None and y_value !=i:
            result = [i, y_value]

    return result

if __name__ == "__main__":
    main()

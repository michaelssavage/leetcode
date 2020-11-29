def main():
    a = [1,2,3]
    b = [1,2,3]
    k = 31
    print(countTinyPairs(a,b,k))

    c = [16, 1, 4, 2, 14]
    d = [7, 11, 2, 0, 15]
    l = 743
    print(countTinyPairs(c,d,l))

def countTinyPairs(a,b,k):
    i = 0
    count = 0
    while i < len(a):
        if int(str(a[i]) + str(b[len(a)-i-1])) < k:
            count +=1
        i+=1
    return count


if __name__ == "__main__":
    main()
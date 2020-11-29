def main():
    a = [10,2]
    print(concatenationsSum(a))

def concateSums(a):
    count = 0
    for i in a:
        print([sum(a)*[(len(str(i))-1)].count(j)*10**(j+1) for j in range(7)])
    
        

def concatenationsSum(a):
    sums=sum(a)
    mult=sums*len(a)
    powers=sum([sums*[len(str(x))-1 for x in a].count(j)*10**(j+1) for j in range(7)])
    return mult+powers
    
        
if __name__ == "__main__":
    main()
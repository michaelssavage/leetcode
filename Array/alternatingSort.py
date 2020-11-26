def main():
    a = [1, 3, 2, 4, 2]
    print(alternatingSort(a))

def alternatingSort(a):
    b = []
    i=0
    while len(a) >1:   
        b.append(a[0])
        b.append(a[-1])
        a = a[1:-1]
        if len(a) ==1:
            b.append(a[0])
    return b == sorted(b)

        
if __name__ == "__main__":
    main()
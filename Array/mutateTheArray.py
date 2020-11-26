def main():
    n = 5
    a = [4,0,1,-2,3]
    print(mutateTheArray(n,a))

def mutateTheArray(n,a):
    b = [0] * n
    for i in range(n):
        num1 = a[i-1] if i-1 >=0 else 0
        num2 = a[i] if i >=0 else 0
        num3 = a[i+1] if i+1 < len(a) else 0

        b[i] = num1 + num2 + num3
    return b


if __name__ == "__main__":
    main()
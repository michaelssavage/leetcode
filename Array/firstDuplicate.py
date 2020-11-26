def main():
    a = [2]
    print(firstDuplicate(a))

def firstDuplicate(a):
    seen = set()
    for i in a:
        if i in seen:
            return i
        else:
            seen.add(i)
    return -1

if __name__ == "__main__":
    main()
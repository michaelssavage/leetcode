def firstNotRepeatingCharacter(s):
    seen = dict()
    for i in s:
        if i not in seen:
            seen[i] =1
        else:
            seen[i]+=1

    for k,v in seen.items():
        if v == 1:
            return k
    return '_'


def main():
    s = "aab"
    print(firstNotRepeatingCharacter(s))

if __name__ == "__main__":
    main()
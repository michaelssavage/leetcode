def main():
    a = [[3, 3, 4, 2],
        [4, 4],
        [4, 0, 3, 3],
        [2, 3],
        [3, 3, 3]]
    print(meanGroups(a))

def meanGroups(a):
    groups, means = [], []
    for i,j in enumerate(a):
        mean = sum(j) / len(j)
        if mean not in means:
            means+= [mean]
            groups += [[i]]
        else:
            groups[means.index(mean)] += [i]
    return groups
        


if __name__ == "__main__":
    main()
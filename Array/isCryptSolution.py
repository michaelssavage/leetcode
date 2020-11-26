def isCryptSolution(crypt, solution):
    dic = dict()
    for i in solution:
        key,value = i[0], i[1]
        dic[key] = value

    score = [''] * len(crypt)
    i=0
    for i in range(len(crypt)):
        for c in crypt[i]:
            score[i] += dic[c]
        if score[i][0] == '0' and len(score[i]) != 1:
            return False
    return int(score[0]) + int(score[1]) == int(score[2])

def isCryptSolution2(crypt, solution):
    dic = {ord(c): d for c, d in solution}
    *v, = map(lambda x: x.translate(dic), crypt)
    return not any(x != "0" and x.startswith("0") for x in v) and \
        int(v[0]) + int(v[1]) == int(v[2])

def isCryptSolution3(crypt, solution):
    crypt_s = crypt
    for i in range(0, 3):
        for s in solution:
            crypt_s[i] = crypt_s[i].replace(s[0], s[1])
        
        if crypt_s[i] != '0' and crypt_s[i][0] == '0':
            return False
        
    return int(crypt_s[0]) + int(crypt_s[1]) == int(crypt_s[2])



def main():
    crypt = ["TEN", "TWO", "ONE"]
    solution =  [["O","1"], 
                ["T","0"], 
                ["W","9"], 
                ["E","5"], 
                ["N","4"]]

    print(isCryptSolution(crypt, solution))

    crypt2 = ["A", "A", "A"]
    solution2 = [["A","0"]]
    print(isCryptSolution2(crypt2, solution2))

    crypt3 =["SEND", 
        "MORE", 
        "MONEY"]
    solution3 =[["O","0"], 
        ["M","1"], 
        ["Y","2"], 
        ["E","5"], 
        ["N","6"], 
        ["D","7"], 
        ["R","8"], 
        ["S","9"]]
    print(isCryptSolution3(crypt3, solution3))

if __name__ == "__main__":
    main()
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        x=0
        while x < length:
            y=0
            while y < length:
                if x < y:
                    matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
                y+=1
            x+=1
        for l in matrix:
            l.reverse()
        return matrix

    def rotate2(self, a):
        a.reverse()
        for i in range(len(a)):
            for j in range(i):
                a[i][j], a[j][i] = a[j][i], a[i][j]
        return a

    def rotate3(self,a):
        return list(zip(*reversed(a)))

def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print("matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
    print("answer = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]\n")
    print(f"         {Solution().rotate(matrix)}")

if __name__ == "__main__":
    main()
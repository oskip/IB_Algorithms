class MatRot:
    def rotate(self, A):
        n = len(A)
        for l in range(n/2):
            for i in range(n-1-l*2):
                e1 = A[l][i+l]
                e2 = A[i+l][n-1-l]
                e3 = A[n-1-l][n-1-i-l]
                e4 = A[n-1-i-l][l]
                A[l][i+l] = e4
                A[i+l][n-1-l] = e1
                A[n-1-l][n-1-i-l] = e2
                A[n-1-i-l][l] = e3
        return A

A = []
for i in range(6):
    A.append([i*6+j+1 for j in range(6)])
print A
MatRot().rotate(A)
print A

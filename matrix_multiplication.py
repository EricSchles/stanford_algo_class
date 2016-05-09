class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
            
    def get_size(self):
        return len(self.matrix),len(self.matrix[0])

    def pprint(self):
        for row in self.matrix:
            print(row)
                
        
    def to_array(self):
        return self.matrix
        
    def get_elem(self,row,col):
        return self.matrix[row][col]    
        
    def __add__(self,other):
        row_size,col_size = self.get_size()
        new_matrix = []
        for row in range(row_size):
            new_matrix.append([elem+other.matrix[row][ind] for ind,elem in enumerate(self.matrix[row])])
        return Matrix(new_matrix)
    
    def __sub__(self,other):
        row_size,col_size = self.get_size()
        new_matrix = []
        for row in range(row_size):
            new_matrix.append([elem-other.matrix[row][ind] for ind,elem in enumerate(self.matrix[row])])
        return Matrix(new_matrix)

    def simple_multiplication(self,A,B):
        row_size,col_size = self.get_size()
        new_matrix = [[0 for i in range(row_size)] for j in range(row_size)]
        for i in range(row_size):
            for k in range(row_size):
                for j in range(row_size):
                    new_matrix[i][j] += A[i][k] * B[k][j]
        return Matrix(new_matrix)
    
    def __mul__(self,other):
        row_size,col_size = self.get_size()
        if row_size <= 2:
            return self.simple_multiplication(self.matrix,other.matrix)
        else:
            new_size = row_size//2
            A = [[0 for j in range(new_size)] for i in range(new_size)]
            B = [[0 for j in range(new_size)] for i in range(new_size)]
            C = [[0 for j in range(new_size)] for i in range(new_size)]
            D = [[0 for j in range(new_size)] for i in range(new_size)]

            E = [[0 for j in range(new_size)] for i in range(new_size)]
            F = [[0 for j in range(new_size)] for i in range(new_size)]
            G = [[0 for j in range(new_size)] for i in range(new_size)]
            H = [[0 for j in range(new_size)] for i in range(new_size)]

            for i in range(new_size):
                for j in range(new_size):
                    A[i][j] = self.matrix[i][j]
                    B[i][j] = self.matrix[i][j+new_size]
                    C[i][j] = self.matrix[i + new_size][j]
                    D[i][j] = self.matrix[i + new_size][j + new_size]

                    E[i][j] = other.matrix[i][j]
                    F[i][j] = other.matrix[i][j+new_size]
                    G[i][j] = other.matrix[i + new_size][j]
                    H[i][j] = other.matrix[i + new_size][j + new_size]

            A = Matrix(A)
            B = Matrix(B)
            C = Matrix(C)
            D = Matrix(D)
            E = Matrix(E)
            F = Matrix(F)
            G = Matrix(G)
            H = Matrix(H)
            
            p1 = A*(F-H)
            p2 = (A+B)*H
            p3 = (C+D)*E
            p4 = D*(G-E)
            p5 = (A+D)*(E+H)
            p6 = (B-D)*(G+H)
            p7 = (A -C)*(E+F)

            c11 = p5 + p4 - p2 + p6
            c12 = p1 + p2
            c21 = p3 + p4
            c22 = p1+ p5 - p3 - p7

            final = [[0 for j in range(row_size)] for i in range(row_size)]
            for i in range(new_size):
                for j in range(new_size):
                    final[i][j] = c11.matrix[i][j]
                    final[i][j+new_size] = c12.matrix[i][j]
                    final[i + new_size][j] = c21.matrix[i][j]
                    final[i + new_size][j + new_size] = c22.matrix[i][j]
            return Matrix(final)
            
A = Matrix([])
B = Matrix([])
(A*B).pprint()

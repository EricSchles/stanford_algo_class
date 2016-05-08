from collections import namedtuple
Point = namedtuple('Point','x,y,value')
class Matrix:
    def __init__(self,matrix):
        self.matrix = []
        for ind_row,row in enumerate(matrix):
            for ind_col,elem in enumerate(row):
                self.matrix.append(Point(ind_row,ind_col,elem))
        
    def from_matrix_to_array(self,elems):
        start_row = min([elem.x for elem in elems])
        end_row = max([elem.x for elem in elems])
        start_col = min([elem.y for elem in elems])
        end_col = max([elem.y for elem in elems])
        arr = []
        for row in range(start_row,end_row+1):
            tmp_row = []
            for col in range(start_col,end_col+1):
                for elem in elems:
                    if elem.x == row and elem.y == col:
                        tmp_row.append(elem.value)
            arr.append(tmp_row)
        return arr

    def get_size(self):
        elems = self.matrix
        start_row = min([elem.x for elem in elems])
        end_row = max([elem.x for elem in elems])+1
        start_col = min([elem.y for elem in elems])
        end_col = max([elem.y for elem in elems])+1
        return abs(start_row - end_row),abs(start_col - end_col)

    def get_iterators(self):
        elems = self.matrix
        start_row = min([elem.x for elem in elems])
        end_row = max([elem.x for elem in elems])
        start_col = min([elem.y for elem in elems])
        end_col = max([elem.y for elem in elems])
        return abs(start_row - end_row),abs(start_col - end_col)
    
    def pprint(self):
        elems = self.matrix
        start_row = min([elem.x for elem in elems])
        end_row = max([elem.x for elem in elems])
        start_col = min([elem.y for elem in elems])
        end_col = max([elem.y for elem in elems])
        arr = []
        for row in range(start_row,end_row+1):
            tmp_row = []
            for col in range(start_col,end_col+1):
                for elem in elems:
                    if elem.x == row and elem.y == col:
                        tmp_row.append(elem.value)
            print(tmp_row)
        
    def to_array(self):
        elems = self.matrix
        start_row = min([elem.x for elem in elems])
        end_row = max([elem.x for elem in elems])
        start_col = min([elem.y for elem in elems])
        end_col = max([elem.y for elem in elems])
        arr = []
        for row in range(start_row,end_row+1):
            tmp_row = []
            for col in range(start_col,end_col+1):
                for elem in elems:
                    if elem.x == row and elem.y == col:
                        tmp_row.append(elem.value)
            arr.append(tmp_row)
        return arr

    def get_elem(self,row,col):
        return [elem.value for elem in self.matrix if elem.x == row and elem.y == col][0]
    
    def get_sub_matrix(self,start_row,end_row,start_col,end_col):
        sub_matrix = [elem for elem in self.matrix if elem.x >= start_row  and elem.x <= end_row and elem.y >= start_col and elem.y <= end_col]
        return Matrix(self.from_matrix_to_array(sub_matrix))

    def __add__(self,other):
        other_elems = other.matrix
        elems = self.matrix
        start_row = min([elem.x for elem in elems])
        end_row = max([elem.x for elem in elems])
        start_col = min([elem.y for elem in elems])
        end_col = max([elem.y for elem in elems])
        arr = []
        for row in range(start_row,end_row+1):
            tmp_row = []
            for col in range(start_col,end_col+1):
                first_val = [elem.value for elem in elems if elem.x == row and elem.y == col][0]
                second_val = [elem.value for elem in other_elems if elem.x == row and elem.y == col][0]
                tmp_row.append(first_val+second_val)
            arr.append(tmp_row)
        return Matrix(arr)
    
    def __sub__(self,other):
        other_elems = other.matrix
        elems = self.matrix
        start_row = min([elem.x for elem in elems])
        end_row = max([elem.x for elem in elems])
        start_col = min([elem.y for elem in elems])
        end_col = max([elem.y for elem in elems])
        arr = []
        for row in range(start_row,end_row+1):
            tmp_row = []
            for col in range(start_col,end_col+1):
                first_val = [elem.value for elem in elems if elem.x == row and elem.y == col][0]
                second_val = [elem.value for elem in other_elems if elem.x == row and elem.y == col][0]
                tmp_row.append(first_val-second_val)
            arr.append(tmp_row)
        return Matrix(arr)

def join_quadrants(A,B):
    new_arr = []
    for ind,val in enumerate(A):
        new_arr.append(val+B[ind])
    return new_arr
    
def multiply(X,Y):
    if X.get_size() == (1,1) and Y.get_size() == (1,1):
        return X.matrix[0].value * Y.matrix[0].value
    if X.get_size() == (2,2) and Y.get_size() == (2,2):
        return Matrix([
            [X.get_elem(0,0)*Y.get_elem(0,0)+X.get_elem(0,1)*Y.get_elem(1,0), X.get_elem(0,0)*Y.get_elem(0,1)+X.get_elem(0,1)*Y.get_elem(1,1)],
            [X.get_elem(1,0)*Y.get_elem(0,0)+X.get_elem(1,1)*Y.get_elem(1,0), X.get_elem(1,0)*Y.get_elem(0,1)+X.get_elem(1,1)*Y.get_elem(1,1)]
        ])
    else:
        x_row_size,x_col_size = X.get_iterators()
        x_row_mid,x_col_mid = x_row_size//2,x_col_size//2
        y_row_size,y_col_size = Y.get_iterators()
        y_row_mid,y_col_mid = y_row_size//2,y_col_size//2
        #get_sub_matrix(start_row,end_row,start_col,end_col)
        A = X.get_sub_matrix(0,x_row_mid,0,x_col_mid)
        B = X.get_sub_matrix(0,x_row_mid,x_col_mid,x_col_size)
        C = X.get_sub_matrix(x_row_mid,x_row_size,0,x_col_mid)
        D = X.get_sub_matrix(x_row_mid,x_row_size,x_col_mid,x_col_size)
        E = Y.get_sub_matrix(0,y_row_mid,0,y_col_mid)
        F = Y.get_sub_matrix(0,y_row_mid,y_col_mid,y_col_size)
        G = Y.get_sub_matrix(y_row_mid,y_row_size,0,y_col_mid)
        H = Y.get_sub_matrix(y_row_mid,y_row_size,y_col_mid,y_col_size)
        P_1 = multiply(A,F-H)
        P_2 = multiply(A+B,H)
        P_3 = multiply(C+D,E)
        P_4 = multiply(D,G-E)
        P_5 = multiply(A+D,E+H)
        P_6 = multiply(B-D,G+H)
        P_7 = multiply(A-C,E+F)
        quad_1 = P_5 + P_4 - P_2 + P_6
        quad_2 = P_1 + P_2
        quad_3 = P_3 + P_4
        quad_4 = P_1 + P_5 - P_3 - P_7
        new_matrix = []
        top = join_quadrants(quad_1.to_array(),quad_2.to_array())
        bottom = join_quadrants(quad_3.to_array(),quad_4.to_array())
        return Matrix(top+bottom)
        

A = Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
B = Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
#print(A.get_size())
#print(B.get_size())
multiply(A,B)

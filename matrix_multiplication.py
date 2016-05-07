from collections import namedtuple
Point = namedtuple('Point','x,y,value')
class Matrix:
    def __init__(self,matrix=None):
        if matrix:
            self.matrix = []
            for ind_row,row in enumerate(matrix):
                for ind_col,elem in enumerate(row):
                    self.matrix.append(Point(ind_row,ind_col,elem))
        else: self.matrix = matrix
        
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

    def get_sub_matrix(self,start_row,end_row,start_col,end_col):
        sub_matrix = [elem for elem in self.matrix if elem.x >= start_row  and elem.x <= end_row and elem.y >= start_col and elem.y <= end_col]
        return Matrix(matrix=self.from_matrix_to_array(sub_matrix))
    
        

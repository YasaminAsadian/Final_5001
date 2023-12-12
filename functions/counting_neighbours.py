

def counting_neighbour_values_of_each_cell(matrix, i, j, boundary_type):
    """
    This function calculates the number of live cells surrounding each cell in a matrix, 
    considering either periodic or non-periodic boundary conditions.

    Arguments:
        matrix: A matrix with the shape (mat_i, mat_j).
        i: The row index in the matrix.
        j: The column index in the matrix.
        boundary_type: A string that determines whether the boundary condition is 'periodic' or 'non-periodic'.

    Returns: 
        An integer representing the number of live cells around the cell at matrix[i, j].
    """
    mat_i, mat_j = matrix.shape
    count = 0

    if boundary_type == "non_periodic":
        #In the non-periodic scenario, this function accounts for the edge cells by only considering 
        #the neighboring cells that are within the boundaries of the matrix. 
        #Essentially, it's akin to applying zero padding around the matrix. This means that the edge cells will 
        #treat any position outside the matrix as having a value of zero when calculating neighboring cells.
        
        if (0 <= i-1) and (0 <= j - 1):
            count += matrix[i - 1, j - 1]

        if (0 <= i-1):
            count += matrix[i - 1, j]

        if (0 <= i-1) and (j + 1 < mat_j):
            count += matrix[i - 1, j + 1] 
        
        if (0 <= j-1):
            count += matrix[i , j - 1] 

        if (j + 1 < mat_j):
            count += matrix[i , j + 1]

        if (i + 1 < mat_i) and (0 <= j - 1):
            count += matrix[i + 1, j - 1]

        if (i + 1 < mat_i):
            count += matrix[i+1, j]
        
        if (i + 1 < mat_i) and (j + 1 < mat_j):
            count += matrix[i + 1, j + 1]

    if boundary_type == "periodic":
        #In the periodic boundary condition scenario, the function employs a 
        #torus topology. This means that the matrix wraps around both horizontally and vertically, allowing the 
        #edges to connect seamlessly which means the cell values do not change under the following transformations:

        #i -> i + mat_i
        #j -> j + mat_j
        
        a1 = i - 1
        a3 = i + 1
        b1 = j - 1
        b3 = j + 1

        if i == 0:
            a1 = mat_i - 1
        if i == mat_i - 1:
            a3 = 0
        if j == 0:
            b1 = mat_j - 1
        if j == mat_j - 1:
            b3 = 0 
            
        count  = (matrix[a1, b1] + matrix[a1, j] + matrix[a1, b3] 
                + matrix[i , b1] +                matrix[i , b3]
                + matrix[a3, b1] + matrix[a3, j] + matrix[a3, b3])
        
    if count > 8 or count < 0:
        print("Total value of the neighbours cannot be greater than 8 or smaller than zero.")

    return count

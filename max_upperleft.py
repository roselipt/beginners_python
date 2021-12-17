#  This is a problem from a hackerrank mock test.
#  Given a square matrix, and one rule for transformation,
#  that rows or columns may be flipped, find the max possible sum
#  of the upper left quadrant.

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def showMatrix(m):
    for row in m:
        for column in row:
            column = format(column, '>4')
            print(column, end =' ')
        print()

def upperLeft(m):
    totes = 0
    half = len(m)//2    
    for row in range(half):
        for col in range(half):
            totes += m[row][col]
    return totes

def maxRows(m):
    """Maximizes each row. Meaning flips or leaves alone, ensuring that left half is greater."""
    for row in m:
        halfway = len(row) // 2     #  Integer division is important here! (Python division defaults to float)
        left = sum(row[:halfway])
        right = sum(row[halfway:])
        if right > left:
            for i in range(halfway):
                row[i], row[len(row)-i - 1] = row[len(row)-i-1], row[i]

def maxColumns(m):
    half = len(m)//2
    for col in range(half):
        top = 0
        for i in range(half):
            top += m[i][col]
        bottom = 0
        for i in range(half,len(m)):
            bottom +=m[i][col]
        print('From maxColumns, column', col, 'top is', top, 'and bottom is', bottom)
        if bottom > top:
            for i in range(half):
                last = len(m) - 1
                m[i][col], m[last - i][col] = m[last - i][col], m[i][col]
                #m[col][i], m[col][len(m) - i -1] = m[col][len(m) - i -1], m[col][i]

showMatrix(matrix)
print('Upper left total is', upperLeft(matrix))
maxRows(matrix)
print('After maxRows, matrix is')
showMatrix(matrix)
maxColumns(matrix)
print('After maxColumns, matrix is')
showMatrix(matrix)
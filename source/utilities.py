def nodalMatrix(node_number):
    matrix=[]
    for i in range(node_number):
        matrix.append([])
    return matrix[:]

mapper={"R":"resistor","I":"Current indipendent source"}
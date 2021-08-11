def sub (vector1, vector2):
    newVector = []
    if len(vector1) != len(vector2):
        return ArithmeticError("Las matrices no son del mismo tamaño")
    else:
        for x in range(len(vector1)):
            newVector.append(vector1[x]-vector2[x])
        return newVector


def punto (vector1, vector2):
    if len(vector1) != len(vector2):
        return ArithmeticError("Las matrices no son del mismo tamaño")
    else: 
        total = 0 
        for x in range(len(vector1)):
            total += vector1[x] * vector2[x]
        return total
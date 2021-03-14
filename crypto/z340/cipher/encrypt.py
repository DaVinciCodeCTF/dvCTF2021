from data import *
import numpy as np
import secrets
import html

def transpose(pt):
    matrix = np.zeros((9, 17))

    for i in range(len(pt)):
        matrix[i%9][(2*i)%17] = ord(pt[i])

    return matrix

def matrix_to_str(matrix):
    result = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result += chr(int(matrix[i][j]))
    return result

def substitute(result_trsp):
    result = ''
    for i in result_trsp:
        result += secrets.choice(key[i])
    return result

matrix = transpose(pt)
ct = substitute(matrix_to_str(matrix))
for i in range(9):
    print(f"{html.escape(ct[i*17:(i*17)+17])}<br>")

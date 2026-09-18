import copy

import numpy as np

n, m = map(int, input().split())
if n < m - 1:
    print("The system is unsolvable.")
elif n > m - 1:
    print("There are endless solutions.")
else:
    matrix = np.full((n, m), 0, dtype="float32")
    for i in range(n):
        matrix[i] = list(map(float, input().split()))

    matrix_0 = matrix[:, 0 : m-1]
    determ_0 = np.linalg.det(matrix_0)
    determs = []
    for i in range(m - 1):
        matrix_flex = copy.deepcopy(matrix[:, 0 : m-1])
        matrix_flex[:, i] = matrix[:, m-1]
        determ = np.linalg.det(matrix_flex)
        determs.append(determ)

    answer = [round(numb / determ_0, 3) for numb in determs]
    print(*answer)

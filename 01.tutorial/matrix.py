import numpy as np


def rotation_matrix(n):
    vector = np.random.rand(n)
    matrix = np.zeros((n, n))

    for i in range(0, n):
        matrix[i, i] = 1.0

    vector_dot = 0.0
    for i in range(0, n):
        vector_dot = vector_dot + vector[i] * vector[i]

    if 0.0 < vector_dot:
        for i in range(0, n):
            for j in range(0, n):
                matrix[i, j] = matrix[i, j] - 2.0 * vector[i] * vector[j] / vector_dot

    return matrix


def generate_low_rank_matrix(size, rank):
    matrix = np.zeros((size, size))

    for i in range(rank):
        vector_a = np.random.rand(size, 1)
        vector_b = np.random.rand(1, size)
        matrix += vector_a.dot(vector_b)

    return matrix

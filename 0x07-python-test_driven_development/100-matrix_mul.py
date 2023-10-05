#!/usr/bin/python3

"""
    Multiplication of two matrice
"""


def matrix_mul(m_a, m_b):
    """check if m_a or m_b is a list"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    """ check if m_a or m_b is empty"""
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    a_row_sizes = []

    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        if len(m_a[0]) == 0:
            raise ValueError("m_a can't be empty")
        a_row_sizes.append(len(i))
        if not all(val == a_row_sizes[0] for val in a_row_sizes):
            raise TypeError("each row of m_a must be of the same size")
        for _ in i:
            if type(_) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    b_row_sizes = []

    for j in m_b:
        if not isinstance(j, list):
            raise TypeError("m_b must be a list of lists")
        if len(m_b[0]) == 0:
            raise ValueError("m_b can't be empty")
        b_row_sizes.append(len(j))
        if not all(val == b_row_sizes[0] for val in b_row_sizes):
            raise TypeError("each row of m_b must be of the same size")
        for _ in j:
            if type(_) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    m_c = []
    for i in m_a:
        for j in range(len(i)):
            temp = []
            sumtotal = 0
            for k in m_b:
                try:
                    sumtotal = i[j] * k[j][0]
                except ValueError:
                    raise ValueError("m_a and m_b can't be multiplied")
            temp.append(sumtotal)
        m_c.append(temp)
    return m_c

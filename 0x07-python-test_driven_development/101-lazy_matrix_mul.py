import numpy as np
""" lazy matrix with NumPy"""


def lazy_matrix_mul(m_a, m_b):
    """ lazy matrix multiplication"""
    """
    try:
        result = np.dot(m_a, m_b)
        return result
    except ValueError:
        raise
        ValueError("shapes {} and {} not aligned: {} (dim 0) != {} (dim 1)"
                   .format(m_a.shape, m_b.shape, m_a.shape[1],
                           m_b.shape[0]))
    """
    return (np.matmul(m_a, m_b))

import numpy as np
from linear_algebra.basis_and_rank import determine_basis


def calculate_projection_from_basis(x,B):
    p=np.dot(np.dot(np.dot(B,np.linalg.inv(np.dot(np.transpose(B),B))),np.transpose(B)),x)
    return p

def calculate_projection_from_generating_set(x,generating_set):
    B=determine_basis(generating_set)
    p=calculate_projection_from_basis(x,B)
    return p





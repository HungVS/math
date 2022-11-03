import numpy as np
from analytic_geometry.orthogonal_projections import calculate_projection_from_generating_set

def calculate_distance_of_2_vectors(a,b):
    d=np.linalg.norm(a-b)
    return d

def calculate_distance_of_vector_and_space(x,generating_set):
    p=calculate_projection_from_generating_set(x,generating_set)
    d=calculate_distance_of_2_vectors(x,p)
    return d
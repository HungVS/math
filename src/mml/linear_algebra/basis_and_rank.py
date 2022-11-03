import sympy 
import numpy as np

# ref: https://stackoverflow.com/questions/28816627/how-to-find-linearly-independent-rows-from-a-matrix
def determine_basis(generating_set):
    generating_set=generating_set.T
    _, inds = sympy.Matrix(generating_set).T.rref()   # to check the rows you need to transpose!
    B=np.transpose(generating_set[inds,:])
    return B

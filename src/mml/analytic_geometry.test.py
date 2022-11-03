import unittest
from analytic_geometry.orthogonal_projections import *

class Test(unittest.TestCase):

    def test_calculate_projection_from_basis(self):
        B=np.transpose(
            [[1,1,1],
            [0,1,2]]
        )
        x=np.transpose([6,0,0])
        p=np.array([5,2,-1])
        res=calculate_projection_from_basis(x,B).round(6)
        self.assertEqual((res==p).all(), True)
    
    def test_calculate_projection_from_generating_set(self):
        generating_set=np.transpose(
            [[0,-1,2,0,2],
            [1,-3,1,-1,2],
            [-3,4,1,2,1],
            [-1,-3,5,0,7]]
        )
        x=np.transpose([-1,-9,-1,4,1])
        res=calculate_projection_from_generating_set(x,generating_set).round(6)
        p=np.array([1,-5,-1,-2,3])
        self.assertEqual((res==p).all(), True)


if __name__ == '__main__':
    unittest.main()
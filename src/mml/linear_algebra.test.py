import unittest
from linear_algebra.basis_and_rank import *

class Test(unittest.TestCase):

    def test_determine_basis(self):
        generating_set=np.transpose(
            [[0,-1,2,0,2],
            [1,-3,1,-1,2],
            [-3,4,1,2,1],
            [-1,-3,5,0,7]]
        )
        res=determine_basis(generating_set)
        B=generating_set[:,[0,1,2]]
        self.assertEqual((res==B).all(), True)


if __name__ == '__main__':
    unittest.main()
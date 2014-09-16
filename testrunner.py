import os
import sys
from tests import unittests
import unittest

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(unittests.TestWordCountValidator)
    unittest.TextTestRunner(verbosity=2).run(suite)

import os
import sys
from tests import unittests
from tests import integration
import unittest

if __name__ == "__main__":
    unit_suite = unittest.TestLoader().loadTestsFromTestCase(unittests.TestWordCountUtils)
    unittest.TextTestRunner(verbosity=2).run(unit_suite)

    integration_suite = unittest.TestLoader().loadTestsFromTestCase(integration.TestWordCountApp)
    unittest.TextTestRunner(verbosity=2).run(integration_suite)

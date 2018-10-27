import os
import unittest

loader = unittest.TestLoader()
suite = loader.discover('./tests', pattern="Test*.py")

runner = unittest.TextTestRunner()
runner.run(suite)
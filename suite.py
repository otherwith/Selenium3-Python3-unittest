import unittest
import time
from Common.funcation import project_path

if __name__ == '__main__':
    test_dir = project_path() + "TestCases"
    tests = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',top_level_dir= None)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests)
import unittest
from calculator import *

from functions import get_files_info


class GetFilesInfoTests(unittest.TestCase):
    def test_current_dir(self):
            get_files_info("calculator", ".")
            pass
    def test(self):
        get_files_info("calculator", "pkg")
        pass

    def test2(self):
        get_files_info("calculator", "/bin")
        pass

    def test3(self):
        get_files_info("calculator", "../")
        pass
import unittest
import calculator

from functions import get_files_info


class SimpleTests(unittest.TestCase):
    def get_files_info("calculator", "."):
        pass

    def get_files_info("calculator", "pkg"):
        pass

    def get_files_info("calculator", "/bin"):
        pass

    def get_files_info("calculator", "../"):
        pass
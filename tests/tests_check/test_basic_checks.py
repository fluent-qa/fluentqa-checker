import unittest

from qpychecker.check import Check
from qpychecker.checkers import CheckError


class TestBasicChecks(unittest.TestCase):

    def test_is_none(self):
        res = Check(None).is_none()
        self.assertIsInstance(res, Check)
        try:
            Check(123).is_none()
        except CheckError:
            pass

    def test_is_not_none(self):
        res = Check(123).is_not_none()
        self.assertIsInstance(res, Check)
        try:
            Check(None).is_not_none()
        except CheckError:
            pass

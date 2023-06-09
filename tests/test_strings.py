import unittest

from qpychecker.check import soft_checker
from qpychecker.checkers import StringChecker as Check, StringChecker
from qpychecker.checkers.exceptions import CheckError


class TestStringsAssertions(unittest.TestCase):

    def test_is_string(self):
        res = Check("Hello").is_string()
        self.assertIsInstance(res, Check)
        try:
            Check(123).is_string()
           
        except CheckError:
            pass

    def test_is_not_string(self):
        res = Check(123).is_not_string()
        self.assertIsInstance(res, Check)
        try:
            Check("Hello").is_not_string()
           
        except CheckError:
            pass

    def test_contains_numbers(self):
        res = Check("Hello123").contains_numbers()
        self.assertIsInstance(res, Check)
        try:
            Check("Hello").contains_numbers()
           
        except CheckError:
            pass

    def test_not_contains_numbers(self):
        res = Check("Hello").not_contains_numbers()
        self.assertIsInstance(res, Check)
        try:
            Check("Hello123").not_contains_numbers()
           
        except CheckError:
            pass

    def test_contains_numbers_only(self):
        res = Check("123").contains_numbers_only()
        self.assertIsInstance(res, Check)
        try:
            Check("Hello123").contains_numbers_only()
           
        except CheckError:
            pass

    def test_contains_chars(self):
        res = StringChecker("12a3").contains_chars()
        res.report_result()

    def test_not_contains_chars(self):
        res = StringChecker("123").not_contains_chars()
        self.assertIsInstance(res, Check)
        try:
            Check("012t3").not_contains_chars()
           
        except CheckError:
            pass

    def test_contains_chars_only(self):
        res = Check("abc").contains_chars_only()
        self.assertIsInstance(res, Check)
        try:
            Check("123").contains_chars_only()
           
        except CheckError:
            pass

    def test_contains_spaces(self):
        res = Check("hello world").contains_spaces()
        self.assertIsInstance(res, Check)
        try:
            Check("goodbye").contains_spaces()
           
        except CheckError:
            pass

    def test_contains_char(self):
        res = Check("hello world").contains_char('w')
        self.assertIsInstance(res, Check)
        try:
            Check("goodbye").contains_char('z')
           
        except CheckError:
            pass

    def test_not_contains_char(self):
        res = Check("hello world").not_contains_char('z')
        self.assertIsInstance(res, Check)
        try:
            Check("goodbye").not_contains_char('g')
           
        except CheckError:
            pass

    def test_is_shorter_than(self):
        res = Check("hi").is_shorter_than(5)
        self.assertIsInstance(res, Check)
        try:
            Check("goodbye").is_shorter_than(4)
           
        except CheckError:
            pass

    def test_is_longer_than(self):
        res = Check("hello").is_longer_than(2)
        self.assertIsInstance(res, Check)
        try:
            Check("good").is_longer_than(10)
           
        except CheckError:
            pass

    def test_has_length(self):
        res = Check("hello").has_length(5)
        self.assertIsInstance(res, Check)
        try:
            Check("good").has_length(10)
           
        except CheckError:
            pass

    def test_has_not_length(self):
        with soft_checker("hello") as checker:
            checker.set_check_target("t456").has_not_length(2)
            checker.has_not_length(4)
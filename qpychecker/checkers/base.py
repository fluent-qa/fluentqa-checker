from contextlib import contextmanager
from typing import List

from qpychecker.checkers import CheckResult, check_result


class CheckMixin:

    def __init__(self, value, soft_assertion=True):
        self._val = value
        self.SOFT_ASSERTION = soft_assertion
        self.check_results: List[CheckResult] = []

    @property
    def value(self):
        return self._val

    # Basic checks
    @contextmanager
    def check_context(self, msg):
        try:
            yield
            self.check_results.append(check_result('{} for {}'.format(msg, self._val),
                                                   status=True))

            return self
        except AssertionError as e:
            self.check_results.append(check_result('{} for {}'.format(msg, self._val), error=e,
                                                   capture=self.SOFT_ASSERTION))
            return self

    def report_result(self):
        for result in self.check_results:
            print(result.__repr__())

        assert 0 == len([item for item in self.check_results if item.status is False])


def checker_wrapper(target):
    def wrapper(*args, **kwargs):
        cls_obj = args[0]
        try:
            msg = args[1]
        except Exception as e:
            msg = None

        with cls_obj.check_context(msg):
            return target(*args, **kwargs)

    return wrapper

import importlib
import inspect
import pkgutil

from .checkers import *


class Check(BooleanChecker, CollectionChecker, UUIDChecker,
            TypeChecker, StringChecker, NumberChecker, DictChecker, SequenceChecker):

    def load_assertions(self, package_path):
        ass = importlib.import_module(package_path)
        assertion_modules = []
        for _1, module_name, _2 in pkgutil.iter_modules(ass.__path__):
            assertion_modules.append(importlib.import_module(ass.__name__ + '.' + module_name))
        for module in assertion_modules:
            for item in inspect.getmembers(module, inspect.isfunction):
                func_name = item[0]
                func = item[1]
                bound_method = func.__get__(self, self.__class__)
                setattr(self, func_name, bound_method)
        return self

    def set_check_target(self, val):
        self._val = val
        return self

    def is_none(self, msg=None):
        with self.check_context(msg):
            assert self._val is None
            return self

    def is_not_none(self, msg=None):
        with self.check_context(msg):
            assert self._val is not None
            return self


@contextmanager
def soft_checker(name):
    checker = Check(name)
    try:
        yield checker
    except Exception as e:
        checker.check_results.append(check_result("unexpected error", e))
    finally:
        checker.report_result()

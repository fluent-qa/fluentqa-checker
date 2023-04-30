import types as t

from qpychecker.checkers import CheckMixin


class TypeChecker(CheckMixin):

    def is_subtype_of(self, _type, msg=None):
        with self.check_context(msg):
            assert issubclass(self._val.__class__, _type)

    def is_not_subtype_of(self, _type, msg=None):
        with self.check_context(msg):
            assert not issubclass(self._val.__class__, _type)

    def is_of_type(self, _type, msg=None):
        with self.check_context(msg):
            assert isinstance(self._val, _type)

    def is_not_of_type(self, _type, msg=None):
        with self.check_context(msg):
            assert not isinstance(self._val, _type)

    def is_module(self, msg=None):
        with self.check_context(msg):
            assert isinstance(self._val, t.ModuleType)

    def is_runnable(self, msg=None):
        with self.check_context(msg):
            assert isinstance(self._val, t.FunctionType)

    def is_not_runnable(self, msg=None):
        with self.check_context(msg):
            assert not isinstance(self._val, t.FunctionType)

from . import CheckMixin


class BooleanChecker(CheckMixin):

    def is_boolean(self, msg=None):
        with self.check_context(msg):
            assert isinstance(self._val, bool)
            return self

    def is_not_boolean(self, msg=None):
        with self.check_context(msg):
            assert not isinstance(self._val, bool)
            return self

    def is_truthy(self, msg=None):
        with self.check_context(msg):
            assert self._val
            return self

    def is_true(self, msg=None):
        return self.is_truthy(msg)

    def is_not_false(self, msg=None):
        return self.is_true(msg)

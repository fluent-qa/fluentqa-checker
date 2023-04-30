from qpychecker.checkers import CheckMixin


class DictChecker(CheckMixin):

    def is_dict(self, msg=None):
        with self.check_context(msg):
            assert isinstance(self._val, dict)

    def is_not_dict(self, msg=None):
        with self.check_context(msg):
            assert not isinstance(self._val, dict)

    def has_keys(self, msg=None, *args):
        with self.check_context(msg):
            self.is_dict()
            for key in args:
                assert key in self._val

    def has_not_keys(self, msg=None, *args):
        with self.check_context(msg):
            self.is_dict()
            for key in args:
                assert key not in self._val

    def has_pairs(self, expected_pairs, msg=None):
        with self.check_context(msg):
            self.is_dict()
            for cur_key, cur_value in expected_pairs.items():
                assert self.value[cur_key] == cur_value

    def has_not_pairs(self, expected_pairs, msg=None):
        with self.check_context(msg):
            self.is_dict()
            for cur_key, cur_value in expected_pairs.items():
                does_not_have_key = cur_key not in self.value.keys()
                assert does_not_have_key or self.value[cur_key] != cur_value
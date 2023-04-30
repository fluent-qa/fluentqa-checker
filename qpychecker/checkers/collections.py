from . import CheckMixin


class CollectionChecker(CheckMixin):

    def is_set(self, msg=None):
        with self.check_context(msg):
            assert isinstance(self._val, set)

    def is_not_set(self, msg=None):
        with self.check_context(msg):
            assert not isinstance(self._val, set)

    def is_subset_of(self, _set, msg=None):
        with self.check_context(msg):
            self.is_set()
            assert self._val.issubset(_set)

    def is_not_subset_of(self, _set, msg=None):
        with self.check_context(msg):
            self.is_set()
            assert not self._val.issubset(_set)

    def is_superset_of(self, _set, msg=None):
        with self.check_context(msg):
            self.is_set()
            assert self._val.issuperset(_set)

    def is_not_superset_of(self, _set, msg=None):
        with self.check_context(msg):
            self.is_set()
            assert not self._val.issuperset(_set)

    def intersects(self, _set, msg=None):
        with self.check_context(msg):
            self.is_set()
            assert len(self._val.intersection(_set)) != 0

    def not_intersects(self, _set, msg=None):
        with self.check_context(msg):
            self.is_set()
            assert len(self._val.intersection(_set)) == 0

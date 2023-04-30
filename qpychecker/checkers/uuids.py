from uuid import UUID

from qpychecker.checkers import CheckMixin


class UUIDChecker(CheckMixin):

    def is_uuid1(self, msg=None):
        with self.check_context(msg):
            assert (UUID(self.value).version == 1)

    def is_not_uuid1(self, msg=None):
        with self.check_context(msg):
            assert (UUID(self.value).version != 1)

    def is_uuid4(self, msg=None):
        with self.check_context(msg):
            assert (UUID(self.value).version == 4)

    def is_not_uuid4(self, msg=None):
        with self.check_context(msg):
            assert (UUID(self.value).version != 4)

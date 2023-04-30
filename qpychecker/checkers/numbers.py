from qpychecker.checkers import CheckMixin, checker_wrapper
from qpychecker.checkers.exceptions import CheckError


class NumberChecker(CheckMixin):
    @checker_wrapper
    def is_number(self):
        try:
            assert isinstance(self._val, self.NUMERIC_TYPES)
            return self
        except AssertionError as e:
            raise CheckError('{} is not a number'.format(self._val)) from e

    @checker_wrapper
    def is_not_number(self):
        try:
            assert not isinstance(self._val, self.NUMERIC_TYPES)
            return self
        except AssertionError as e:
            raise CheckError('{} is a number'.format(self._val)) from e

    @checker_wrapper
    def is_integer(self):
        try:
            assert isinstance(self._val, int)
            return self
        except AssertionError as e:
            raise CheckError('{} is not integer'.format(self._val)) from e

    @checker_wrapper
    def is_not_integer(self):
        try:
            assert not isinstance(self._val, int)
            return self
        except AssertionError as e:
            raise CheckError('{} is integer'.format(self._val)) from e

    @checker_wrapper
    def is_float(self):
        try:
            assert isinstance(self._val, float)
            return self
        except AssertionError as e:
            raise CheckError('{} is not float'.format(self._val)) from e

    @checker_wrapper
    def is_not_float(self):
        try:
            assert not isinstance(self._val, float)
            return self
        except AssertionError as e:
            raise CheckError('{} is float'.format(self._val)) from e

    @checker_wrapper
    def is_real(self):
        self.is_number()
        try:
            assert not isinstance(self._val, complex)
            return self
        except AssertionError as e:
            raise CheckError('{} is not real'.format(self._val)) from e

    @checker_wrapper
    def is_not_real(self):
        self.is_number()
        try:
            assert isinstance(self._val, complex)
            return self
        except AssertionError as e:
            raise CheckError('{} is real'.format(self._val)) from e

    @checker_wrapper
    def is_complex(self):
        try:
            assert isinstance(self._val, complex)
            return self
        except AssertionError as e:
            raise CheckError('{} is not complex'.format(self._val)) from e

    @checker_wrapper
    def is_not_complex(self):
        try:
            assert not isinstance(self._val, complex)
            return self
        except AssertionError as e:
            raise CheckError('{} is complex'.format(self._val)) from e

    @checker_wrapper
    def is_positive(self):
        self.is_real()
        try:
            assert float(self._val) > 0.
            return self
        except AssertionError as e:
            raise CheckError('{} is zero or negative'.format(self._val)) from e

    @checker_wrapper
    def is_not_positive(self):
        self.is_real()
        try:
            assert float(self._val) <= 0
            return self
        except AssertionError as e:
            raise CheckError('{} is positive'.format(self._val)) from e

    @checker_wrapper
    def is_negative(self):
        self.is_real()
        try:
            assert float(self._val) < 0.
            return self
        except AssertionError as e:
            raise CheckError('{} is zero or positive'.format(self._val)) from e

    @checker_wrapper
    def is_not_negative(self):
        self.is_real()
        try:
            assert float(self._val) >= 0
            return self
        except AssertionError as e:
            raise CheckError('{} is negative'.format(self._val)) from e

    @checker_wrapper
    def is_zero(self):
        self.is_real()
        try:
            assert float(self._val) == 0.
            return self
        except AssertionError as e:
            raise CheckError('{} is non-zero'.format(self._val)) from e

    @checker_wrapper
    def is_not_zero(self):
        self.is_real()
        try:
            assert float(self._val) != 0.
            return self
        except AssertionError as e:
            raise CheckError('{} is non-zero'.format(self._val)) from e

    @checker_wrapper
    def is_at_least(self, lower):
        self.is_real()
        NumberChecker(lower).is_real()
        try:
            assert float(self._val) >= float(lower)
            return self
        except AssertionError as e:
            raise CheckError('{} is smaller than {}'.format(self._val, lower)) from e

    @checker_wrapper
    def is_at_most(self, upper):
        self.is_real()
        try:
            assert float(self._val) <= float(upper)
            return self
        except AssertionError as e:
            raise CheckError('{} is bigger than {}'.format(self._val, upper)) from e

    @checker_wrapper
    def is_between(self, lower, upper):
        self.is_real()
        NumberChecker(lower).is_real()
        NumberChecker(upper).is_real()
        self.is_at_least(lower).is_at_most(upper)
        return self

    @checker_wrapper
    def is_not_between(self, lower, upper):
        self.is_real()
        NumberChecker(lower).is_real()
        NumberChecker(upper).is_real()
        try:
            assert float(self._val) <= lower or float(self._val) >= upper
            return self
        except AssertionError as e:
            raise CheckError('{} is between {} and {}'.format(self._val, lower, upper)) from e

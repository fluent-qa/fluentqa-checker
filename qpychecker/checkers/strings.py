import json
import re
from xml.etree import ElementTree

import yaml

from qpychecker.checkers import CheckMixin, checker_wrapper
from qpychecker.checkers.exceptions import CheckError


class StringChecker(CheckMixin):
    @checker_wrapper
    def is_string(self, msg=None):
        assert isinstance(self._val, str)
        return self

    @checker_wrapper
    def is_not_string(self, msg=None):
        assert not isinstance(self._val, str)
        return self

    @checker_wrapper
    def contains_numbers(self, msg=None):
        self.is_string()
        assert any(char.isdigit() for char in self._val)
        return self

    @checker_wrapper
    def not_contains_numbers(self, msg=None):
        self.is_string()
        assert not any(char.isdigit() for char in self._val)
        return self

    @checker_wrapper
    def contains_numbers_only(self, msg=None):
        self.is_string()
        assert self._val.isdigit()
        return self

    @checker_wrapper
    def contains_chars(self, msg=None):
        try:
            self.is_string()
            assert bool(re.search('[a-zA-Z]', self._val))
            return self
        except AssertionError as e:
            raise CheckError('{} does not contain chars'.format(self._val)) from e

    def not_contains_chars(self, msg=None):
        self.is_string()
        try:
            assert not bool(re.search('[a-zA-Z]', self._val))
            return self
        except AssertionError as e:
            raise CheckError('{} contains chars'.format(self._val)) from e

    @checker_wrapper
    def contains_chars_only(self, msg=None):
        self.is_string()
        try:
            assert self._val.isalpha()
            return self
        except AssertionError as e:
            raise CheckError('{} also contains alphanumeric chars'.format(self._val)) from e

    @checker_wrapper
    def contains_spaces(self, msg=None):
        self.is_string()
        try:
            assert ' ' in self._val
            return self
        except AssertionError as e:
            raise CheckError('{} does not contain whitespaces'.format(self._val)) from e

    @checker_wrapper
    def not_contains_spaces(self, msg=None):
        self.is_string()
        try:
            assert not ' ' in self._val
            return self
        except AssertionError as e:
            raise CheckError('{} contains whitespaces'.format(self._val)) from e

    @checker_wrapper
    def contains_char(self, _char):
        self.is_string()
        try:
            assert _char in self._val
            return self
        except AssertionError as e:
            raise CheckError('{} does not contain char: {}'.format(self._val,
                                                                   _char)) from e

    @checker_wrapper
    def not_contains_char(self, _char):
        self.is_string()
        try:
            assert not _char in self._val
            return self
        except AssertionError as e:
            raise CheckError('{} contains char: {}'.format(self._val, _char)) from e

    @checker_wrapper
    def is_shorter_than(self, n_chars):
        self.is_string()
        try:
            assert len(self._val) < n_chars
            return self
        except AssertionError as e:
            raise CheckError('{} is longer than {}'.format(self._val, n_chars)) from e

    @checker_wrapper
    def is_longer_than(self, n_chars):
        self.is_string()
        try:
            assert len(self._val) > n_chars
            return self
        except AssertionError as e:
            raise CheckError('{} is shorter than {}'.format(self._val, n_chars)) from e

    @checker_wrapper
    def has_length(self, n_items):
        self.is_string()
        try:
            assert len(self._val) == n_items
            return self
        except AssertionError as e:
            raise CheckError('{} is not long {}'.format(self._val, n_items)) from e

    @checker_wrapper
    def has_not_length(self, n_items):
        self.is_string()
        try:
            assert len(self._val) != n_items
            return self
        except AssertionError as e:
            raise CheckError('{} is long {}'.format(self._val, n_items)) from e

    @checker_wrapper
    def is_lowercase(self, msg=None):
        self.is_string()

        try:
            assert all([c.islower() for c in self._val])
            return self
        except AssertionError as e:
            raise CheckError('{} is not lowercase'.format(self._val)) from e

    @checker_wrapper
    def is_not_lowercase(self, msg=None):
        self.is_string()

        try:
            assert any([not c.islower() for c in self._val])
            return self
        except AssertionError as e:
            raise CheckError('{} is lowercase'.format(self._val)) from e

    @checker_wrapper
    def is_uppercase(self, msg=None):
        self.is_string()
        try:
            assert all([c.isupper() for c in self._val])
            return self
        except AssertionError as e:
            raise CheckError('{} is not uppercase'.format(self._val)) from e

    @checker_wrapper
    def is_not_uppercase(self, msg=None):
        self.is_string()

        try:
            assert any([not c.isupper() for c in self._val])
            return self
        except AssertionError as e:
            raise CheckError('{} is uppercase'.format(self._val)) from e

    @checker_wrapper
    def is_snakecase(self, msg=None):
        self.is_string()
        try:
            tokens = self._val.split('_')
            assert len(tokens) > 1
            assert not any([' ' in t for t in tokens])
            return self
        except AssertionError as e:
            raise CheckError('{} is not snakecase'.format(self._val)) from e

    @checker_wrapper
    def is_not_snakecase(self, msg=None):
        self.is_string()
        try:
            self.is_snakecase()
            raise CheckError('{} is snakecase'.format(self._val))
        except AssertionError:
            return self

    @checker_wrapper
    def is_camelcase(self, msg=None):
        self.is_string()
        try:
            assert (self._val != self._val.lower() and self._val != self._val.upper())
            return self
        except AssertionError as e:
            raise CheckError('{} is not camelcase'.format(self._val)) from e

    @checker_wrapper
    def is_not_camelcase(self, msg=None):
        self.is_string()
        try:
            assert not (self._val != self._val.lower() and self._val != self._val.upper())
            return self
        except AssertionError as e:
            raise CheckError('{} is camelcase'.format(self._val)) from e

    @checker_wrapper
    def is_json(self, msg=None):
        self.is_string()
        try:
            json.loads(self._val)
            return self
        except ValueError:
            raise CheckError('{} is not valid JSON'.format(self._val))

    @checker_wrapper
    def is_not_json(self, msg=None):
        self.is_string()
        try:
            json.loads(self._val)
            raise CheckError('{} is valid JSON'.format(self._val))
        except ValueError:
            return self

    @checker_wrapper
    def is_yaml(self, msg=None):
        self.is_string()
        try:
            yaml.safe_load(self._val)
        except Exception as e:
            raise CheckError('{} is not valid YAML'.format(self._val)) from e
        else:
            return self

    @checker_wrapper
    def is_not_yaml(self, msg=None):
        self.is_string()
        try:
            yaml.safe_load(self._val)
        except Exception:
            return self
        else:
            raise CheckError('{} is valid YAML'.format(self._val))

    @checker_wrapper
    def is_xml(self, msg=None):
        self.is_string()
        try:
            ElementTree.fromstring(self._val)
        except Exception as e:
            raise CheckError('{} is not valid XML'.format(self._val)) from e
        else:
            return self

    @checker_wrapper
    def is_not_xml(self, msg=None):
        self.is_string()
        try:
            ElementTree.fromstring(self._val)
        except Exception:
            return self
        else:
            raise CheckError('{} is valid XML'.format(self._val))

    @checker_wrapper
    def matches(self, regex):
        self.is_string()
        try:
            pattern = re.compile(regex)
            assert pattern.match(self._val) is not None
            return self
        except AssertionError as e:
            raise CheckError('{} does not match pattern: {}'.format(self._val, regex)) from e

    @checker_wrapper
    def not_matches(self, regex):
        self.is_string()
        try:
            pattern = re.compile(regex)
            assert not pattern.match(self._val) is not None
            return self
        except AssertionError as e:
            raise CheckError('{} matches pattern: {}'.format(self._val, regex)) from e

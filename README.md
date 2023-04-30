# FluentQA Checker

## Soft Assertions

> add assertions in tests, with soft_checker, it will run all the assertions, despite any error raised.
And all the error will be reported after test completed.

```python
    def test_has_not_length(self):
        with soft_checker("hello") as checker:
            checker.set_check_target("t456").has_not_length(2)
            checker.has_not_length(4)
```

## fluent-checker

most of the checking is from: https://github.com/fluent-check/fluent-check
Only change some codes to support soft-assertion and do some adujst to make easy to find methods.

## Support Check Method now

```shell
check_results
contains_char
contains_chars
contains_chars_only
contains_numbers
contains_numbers_only
contains_spaces
has_dimensionality
has_keys
has_length
has_not_keys
has_not_length
has_not_pairs
has_pairs
intersects
is_at_least
is_at_most
is_between
is_boolean
is_camelcase
is_complex
is_couple
is_dict
is_empty
is_float
is_integer
is_iterable
is_json
is_list
is_longer_than
is_lowercase
is_module
is_negative
is_none
is_not_between
is_not_boolean
is_not_camelcase
is_not_complex
is_not_dict
is_not_empty
is_not_false
is_not_float
is_not_integer
is_not_iterable
is_not_json
is_not_lowercase
is_not_negative
is_not_none
is_not_number
is_not_of_type
is_not_positive
is_not_real
is_not_runnable
is_not_set
is_not_snakecase
is_not_string
is_not_subset_of
is_not_subtype_of
is_not_superset_of
is_not_uppercase
is_not_uuid1
is_not_uuid4
is_not_xml
is_not_yaml
is_not_zero
is_number
is_nuple
is_of_type
is_positive
is_real
is_runnable
is_set
is_shorter_than
is_snakecase
is_string
is_subset_of
is_subtype_of
is_superset_of
is_triplet
is_true
is_truthy
is_tuple
is_uppercase
is_uuid1
is_uuid4
is_xml
is_yaml
is_zero
load_assertions
matches
not_contains_char
not_contains_chars
not_contains_numbers
not_contains_spaces
not_intersects
not_matches
report_result
set_check_target
```

## Add Extension

```python
checker.load_assertions(<package_path>)
```

It is easy to add more functions, but it is not easy to find the right method in IDE.


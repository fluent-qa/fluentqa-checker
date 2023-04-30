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




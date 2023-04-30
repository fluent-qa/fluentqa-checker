# FluentQA Checker

Add Soft Assertions:

```python
    def test_has_not_length(self):
        with soft_checker("hello") as checker:
            checker.set_check_target("t456").has_not_length(2)
            checker.has_not_length(4)
```

when you try to add assertions, with soft_checker,
it will run all the assertions, despite any error raised
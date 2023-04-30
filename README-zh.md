# Fluent Check

- Soft Assertions

## With Assertions

```python
with Checker(target) as c:
    c.is_not_none()
    c.is_xxx(x,msg)

c.with_result()
```
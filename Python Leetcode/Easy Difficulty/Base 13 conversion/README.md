## Convert Integer to Base 13

Given an integer `num`, return its string representation in **base 13**.

Base 13 uses:

* Digits `0–9` for values `0–9`
* `A` for `10`
* `B` for `11`
* `C` for `12`

### Examples

| Decimal | Base 13 |
| ------: | :------ |
|     `9` | `"9"`   |
|    `10` | `"A"`   |
|    `11` | `"B"`   |
|    `12` | `"C"`   |
|    `13` | `"10"`  |
|    `14` | `"11"`  |
|    `49` | `"3A"`  |
|    `69` | `"54"`  |

For example:

* `49 = 3 × 13 + 10`, so its base-13 representation is `"3A"`.
* `69 = 5 × 13 + 4`, so its base-13 representation is `"54"`.

Write a function:

```python
def convertToBase13(num):
```

that returns the base-13 representation of `num` as a string.

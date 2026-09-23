# Weakest Strong Link

You know that phrase, **“a chain is only as strong as its weakest link”**?

Imagine you had a chain-link fence represented as a matrix. For the chain-link at position `(i, j)`, the input matrix `strength[i][j]` indicates how strong the chain is at that position, where a higher number means a stronger link.

**The numbers in the matrix are unique.**

The **Weakest Strong Link** is defined as a chain-link that is:

* the **weakest link in its row**, and
* the **strongest link in its column**.

Given a matrix `strength`, return the Weakest Strong Link if it exists. Otherwise, return `-1`.

If a Weakest Strong Link exists, there will be exactly one.

## Example 1

**Input:**

```python
strength = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Output:**

```text
7
```

**Explanation:**

`7` is the weakest value in its row:

```text
[7, 8, 9]
```

and the strongest value in its column:

```text
[1, 4, 7]
```

Therefore, `7` is the Weakest Strong Link.

[Weakest Strong Link Example 1](https://api.datalemur.com/assets/d5cb27d8-0ed6-432c-bef5-50752bbb278a)

## Example 2

**Input:**

```python
strength = [
    [9, 8, 10],
    [6, 15, 4]
]
```

**Output:**

```text
-1
```

**Explanation:**

No chain-link is both:

* the weakest value in its row, and
* the strongest value in its column.

Therefore, the output is `-1`.

# Diagonal Stripes

You are given an **`m x n`** matrix.

Your task is to determine if the matrix has diagonal stripes where all elements in each diagonal from **top-left to bottom-right** are identical.

Return **`True`** if every diagonal stripe contains the same number throughout. Otherwise, return **`False`**.

## Example 1

**Input:**

```python
matrix = [
    [42, 7, 13, 99],
    [6, 42, 7, 13],
    [1, 6, 42, 7]
]
```

**Output:**

```python
True
```

**Explanation:**

The diagonals are:

```text
[1]
[6, 6]
[42, 42, 42]
[7, 7, 7]
[13, 13]
[99]
```

Every diagonal contains identical values, so the result is:

```python
True
```

## Example 2

**Input:**

```python
matrix = [
    [8, 23],
    [69, 1]
]
```

**Output:**

```python
False
```

**Explanation:**

The main diagonal is:

```text
[8, 1]
```

The values are different, so the matrix does not have valid diagonal stripes.

## Hint

Think about how you could group all cells that belong to the same diagonal.

A dictionary can be useful because each diagonal can be assigned its own key, and the values belonging to that diagonal can be grouped together.
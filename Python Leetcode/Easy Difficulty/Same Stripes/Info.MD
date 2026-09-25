# Diagonal Matrix Problems — Key Learnings

## Main Idea

When a matrix problem asks you to group cells by something like:

- row
- column
- diagonal

ask:

> **What property of `(i, j)` stays the same for every cell in that group?**

The goal is to find a value that can act as the **ID of the group**.

---

## Top-Left to Bottom-Right Diagonals

For a cell:

```text
(i, j)
```

moving one step down-right gives:

```text
(i + 1, j + 1)
```

Now look at:

```text
i - j
```

After moving:

```text
(i + 1) - (j + 1)
```

Simplify:

```text
i + 1 - j - 1
= i - j
```

So `i - j` never changes while moving along the same diagonal.

Therefore:

```text
\ diagonal → i - j
```

`i - j` can be thought of as the **diagonal ID**.

---

## Example

For a `3 x 3` matrix, the `(i - j)` values are:

```text
 0   -1   -2
 1    0   -1
 2    1    0
```

Notice that matching values form diagonals:

```text
0:
(0,0), (1,1), (2,2)

-1:
(0,1), (1,2)

1:
(1,0), (2,1)
```

---

## This Also Works for Rectangular Matrices

The matrix does **not** need to be square.

For example, in a `2 x 4` matrix:

```text
 0   -1   -2   -3
 1    0   -1   -2
```

Cells with the same `i - j` still belong to the same top-left to bottom-right diagonal.

So:

```text
\ diagonal → i - j
```

works for any `m x n` matrix.

---

## Why a Dictionary Makes Sense

Once you know that `i - j` identifies a diagonal, the problem becomes:

```text
diagonal ID → values belonging to that diagonal
```

That is exactly the kind of grouping a dictionary is useful for.

Example:

```python
diagonals = {}

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        diagonal_id = i - j
        diagonals.setdefault(diagonal_id, []).append(matrix[i][j])
```

You might end up with:

```python
{
    0: [42, 42, 42],
    -1: [7, 7, 7],
    -2: [13, 13],
    -3: [99],
    1: [6, 6],
    2: [1]
}
```

Then the remaining problem is simply:

> For every dictionary key, are all the values the same?

One way to check:

```python
for key in diagonals:
    if len(set(diagonals[key])) != 1:
        return False

return True
```

---

## Useful Matrix Pattern to Remember

```text
same row       → i

same column    → j

\ diagonal     → i - j

/ diagonal     → i + j
```

---

## How to Recognize This Pattern

If a problem says something like:

- "group elements along diagonals"
- "all values on each diagonal must match"
- "find values belonging to the same diagonal"
- "process each diagonal separately"

think:

> **Can I create a diagonal ID from `(i, j)`?**

For top-left → bottom-right diagonals:

```text
i - j
```

For top-right → bottom-left diagonals:

```text
i + j
```

The broader pattern is:

> **When matrix cells need to be grouped, look for an expression involving their row and column indices that stays constant within the group.**
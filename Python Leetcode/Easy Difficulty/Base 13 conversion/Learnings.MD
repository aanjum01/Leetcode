## Base Conversion: How to Think About It

### Core Pattern

To convert a decimal number to base `b`:

```python
remainder = num % b
num = num // b
```

* `% b` gives the **next digit**
* `// b` removes that digit
* Repeat until `num == 0`
* The digits are found **backwards**, so reverse them at the end

For base 13:

```python
remainder = num % 13
num = num // 13
```

### Important Pattern I Didn't Initially Notice

Instead of using:

```python
if remainder == 10:
    digit = "A"
elif remainder == 11:
    digit = "B"
elif remainder == 12:
    digit = "C"
```

create a lookup:

```python
digits = "0123456789ABC"
```

Then:

```python
digit = digits[remainder]
```

Because the remainder is always `0–12`, it naturally works as an index.

```text
0  → digits[0]  → "0"
9  → digits[9]  → "9"
10 → digits[10] → "A"
11 → digits[11] → "B"
12 → digits[12] → "C"
```

### General Problem-Solving Lesson

When you see a fixed mapping like:

```text
0 → something
1 → something
2 → something
...
```

ask:

> Can the number itself be used as an index into a string or list?

This can often replace many `if` / `elif` statements.

### Mental Checklist for Base Conversion

1. **Get the next digit:** `num % base`
2. **Remove that digit:** `num // base`
3. **Map the remainder to a character**
4. **Repeat until the number reaches 0**
5. **Reverse the result**
6. Handle edge cases like `0` and negative numbers

### Pattern to Remember

```text
Base 2  → % 2,  // 2
Base 8  → % 8,  // 8
Base 13 → % 13, // 13
Base 16 → % 16, // 16
```

The base changes, but the algorithm stays almost exactly the same.

## Page With No Likes

## Facebook SQL Interview Question

Assume you're given two tables containing data about Facebook Pages and their respective likes.

Write a query to return the IDs of Facebook pages that have **zero likes**.

The output should be sorted in **ascending order** based on `page_id`.

---

### `pages` Table

| Column Name | Type    |
| ----------- | ------- |
| `page_id`   | integer |
| `page_name` | varchar |

### `pages` Example Input

| `page_id` | `page_name`            |
| --------: | ---------------------- |
|     20001 | SQL Solutions          |
|     20045 | Brain Exercises        |
|     20701 | Tips for Data Analysts |

---

### `page_likes` Table

| Column Name  | Type     |
| ------------ | -------- |
| `user_id`    | integer  |
| `page_id`    | integer  |
| `liked_date` | datetime |

### `page_likes` Example Input

| `user_id` | `page_id` | `liked_date`        |
| --------: | --------: | ------------------- |
|       111 |     20001 | 04/08/2022 00:00:00 |
|       121 |     20045 | 03/12/2022 00:00:00 |
|       156 |     20001 | 07/25/2022 00:00:00 |

---

### Example Output

| `page_id` |
| --------: |
|     20701 |

Page `20701` exists in the `pages` table but has **no matching rows** in the `page_likes` table.

> The dataset you are querying against may have different input and output. **This is just an example.**

---

# Understanding SQL Joins

A `JOIN` combines rows from two tables based on a related column.

In this problem, both tables contain:

```text
page_id
```

So we can connect them with:

```sql
ON pages.page_id = page_likes.page_id
```

Think of the two tables as sets:

```text
pages                         page_likes

┌──────────────┐          ┌──────────────┐
│              │          │              │
│   Facebook   │          │    Pages     │
│    Pages     │          │   With Likes │
│              │          │              │
└──────────────┘          └──────────────┘
```

The type of `JOIN` determines **which rows survive** when there is no match between the two tables.

---

## `INNER JOIN`

An `INNER JOIN` returns only rows that have a match in **both tables**.

```text
LEFT TABLE        RIGHT TABLE

     ╭───────╮
   ╭─┤███████├─╮
   │ │███████│ │
   ╰─┤███████├─╯
     ╰───────╯

      BOTH
```

For this problem:

```sql
SELECT *
FROM pages pg
INNER JOIN page_likes pl
  ON pg.page_id = pl.page_id;
```

This would return pages that **have at least one like**.

For the example data:

```text
pages
─────
20001
20045
20701

page_likes
──────────
20001
20045
```

An `INNER JOIN` keeps:

```text
20001
20045
```

It removes `20701` because there is no matching row in `page_likes`.

Therefore, an `INNER JOIN` is **not useful for finding pages with zero likes**, because those unmatched pages disappear.

---

## `LEFT JOIN`

A `LEFT JOIN` keeps **every row from the left table**.

If a row from the left table has no match in the right table, SQL fills the right-side columns with `NULL`.

```text
LEFT TABLE        RIGHT TABLE

     ╭───────╮
   ╭─┤███████├─╮
   │█│███████│ │
   ╰─┤███████├─╯
     ╰───────╯

   EVERYTHING
   FROM LEFT
```

Example:

```sql
SELECT *
FROM pages pg
LEFT JOIN page_likes pl
  ON pg.page_id = pl.page_id;
```

Conceptually, the result would look like:

| `pg.page_id` | `page_name`            | `pl.user_id` | `pl.page_id` |
| -----------: | ---------------------- | -----------: | -----------: |
|        20001 | SQL Solutions          |          111 |        20001 |
|        20001 | SQL Solutions          |          156 |        20001 |
|        20045 | Brain Exercises        |          121 |        20045 |
|        20701 | Tips for Data Analysts |       `NULL` |       `NULL` |

Notice what happened to page `20701`.

It still appears because `pages` is the **left table**, but because no matching like exists, the columns from `page_likes` become:

```text
NULL
```

This is exactly what we need for this problem.

---

## `RIGHT JOIN`

A `RIGHT JOIN` is essentially the opposite of a `LEFT JOIN`.

It keeps **every row from the right table**.

```text
LEFT TABLE        RIGHT TABLE

     ╭───────╮
   ╭─┤███████├─╮
   │ │███████│█│
   ╰─┤███████├─╯
     ╰───────╯

                 EVERYTHING
                 FROM RIGHT
```

For example:

```sql
SELECT *
FROM page_likes pl
RIGHT JOIN pages pg
  ON pl.page_id = pg.page_id;
```

Because `pages` is now the **right table**, this accomplishes essentially the same thing as:

```sql
FROM pages pg
LEFT JOIN page_likes pl
```

A useful way to remember this is:

```text
LEFT JOIN  → Keep everything on the LEFT
RIGHT JOIN → Keep everything on the RIGHT
INNER JOIN → Keep only matches in BOTH
```

---

## Join Summary

| Join         | Keeps                                                        |
| ------------ | ------------------------------------------------------------ |
| `INNER JOIN` | Only rows that match in both tables                          |
| `LEFT JOIN`  | Every row from the left table + matching rows from the right |
| `RIGHT JOIN` | Every row from the right table + matching rows from the left |

For this problem, we want:

> **Every Facebook page, including pages that don't have a matching like.**

Therefore:

```sql
pages
LEFT JOIN
page_likes
```

is the natural choice.

---

## Hint #1

First, find the relationship between the two tables: `pages` and `page_likes`.

What column exists in both tables?

```text
page_id
```

So we can connect the tables with:

```sql
ON pg.page_id = pl.page_id
```

Now think about the goal:

> We need pages that exist in `pages`, even if they do **not** exist in `page_likes`.

Which `JOIN` preserves every row from `pages`?

A `LEFT JOIN`.

---

## Hint #2

Start with:

```sql
SELECT pg.page_id
FROM pages pg
LEFT JOIN page_likes pl
  ON pg.page_id = pl.page_id
<missing_clause>;
```

The order of the tables is important.

```text
LEFT TABLE             RIGHT TABLE

pages                  page_likes
─────                  ──────────
20001                  20001
20045                  20045
20701
```

Because `pages` is on the **left**, all pages survive the join.

After the `LEFT JOIN`:

```text
pages.page_id        page_likes.page_id
─────────────        ──────────────────
20001                20001
20045                20045
20701                NULL
```

Now we need a way to keep only the row containing:

```text
NULL
```

---

## Hint #3

When a `LEFT JOIN` cannot find a matching row in the right table, SQL returns `NULL` for that table's columns.

Therefore:

```sql
WHERE pl.page_id IS NULL
```

means:

> Give me pages where SQL could not find a matching `page_id` in `page_likes`.

Finally, sort the results in ascending order.

---

## Final Query

```sql
SELECT pg.page_id
FROM pages pg
LEFT JOIN page_likes pl
  ON pg.page_id = pl.page_id
WHERE pl.page_id IS NULL
ORDER BY pg.page_id;
```

### How to Read the Query

```sql
SELECT pg.page_id
```

Return the Facebook page ID.

```sql
FROM pages pg
```

Start with **all Facebook pages**.

```sql
LEFT JOIN page_likes pl
```

Try to find likes belonging to each page while keeping every page.

```sql
ON pg.page_id = pl.page_id
```

Match rows where the two tables have the same `page_id`.

```sql
WHERE pl.page_id IS NULL
```

Keep only pages where **no matching like was found**.

```sql
ORDER BY pg.page_id;
```

Sort the resulting page IDs from smallest to largest.

---

## Key Pattern to Remember

This problem demonstrates a very common SQL interview pattern:

> **Find rows in Table A that do not have a corresponding row in Table B.**

A standard approach is:

```sql
SELECT ...
FROM table_a a
LEFT JOIN table_b b
  ON a.id = b.id
WHERE b.id IS NULL;
```

In plain English:

```text
Keep everything from A
        ↓
Try to match B
        ↓
Find rows where B is NULL
        ↓
Those are the rows in A with no match in B
```

### Solution

To calculate viewership across different device categories—**laptops** versus **mobile devices**—we can use the aggregate function [`COUNT()`](https://datalemur.com/sql-tutorial/sql-aggregate-functions) together with the `FILTER` clause.

The general pattern is:

```sql
SELECT
  COUNT(*) FILTER (WHERE conditional_expression)
FROM table_name;
```

In this problem:

* `laptop` is treated as its own device category.
* `tablet` and `phone` are grouped together as **mobile devices**.

The following query returns the desired result:

```sql
SELECT 
  COUNT(*) FILTER (WHERE device_type = 'laptop') AS laptop_views,
  COUNT(*) FILTER (WHERE device_type IN ('tablet', 'phone')) AS mobile_views 
FROM viewership;
```

### How It Works

For `laptop_views`:

```sql
COUNT(*) FILTER (WHERE device_type = 'laptop')
```

This counts only rows where:

```text
device_type = 'laptop'
```

For `mobile_views`:

```sql
COUNT(*) FILTER (WHERE device_type IN ('tablet', 'phone'))
```

This counts rows where `device_type` is either:

```text
tablet
phone
```

The result contains two columns:

| `laptop_views` | `mobile_views` |
| -------------: | -------------: |
|              2 |              3 |

---

## Solution #2: Using `SUM()` and `CASE`

Another way to solve the problem is with the [`SUM()`](https://datalemur.com/sql-tutorial/sql-aggregate-functions) aggregate function and a [`CASE`](https://datalemur.com/sql-tutorial/sql-case-statement) statement.

```sql
SELECT 
  SUM(
    CASE 
      WHEN device_type = 'laptop' THEN 1 
      ELSE 0 
    END
  ) AS laptop_views,

  SUM(
    CASE 
      WHEN device_type IN ('tablet', 'phone') THEN 1 
      ELSE 0 
    END
  ) AS mobile_views 
FROM viewership;
```

### How `SUM()` + `CASE` Works

The first `CASE` statement:

```sql
CASE 
  WHEN device_type = 'laptop' THEN 1 
  ELSE 0 
END
```

assigns:

```text
laptop → 1
anything else → 0
```

Then `SUM()` adds those values together.

For example:

| `device_type` | `CASE` Result |
| ------------- | ------------: |
| tablet        |             0 |
| laptop        |             1 |
| laptop        |             1 |
| phone         |             0 |
| tablet        |             0 |

So:

```text
0 + 1 + 1 + 0 + 0 = 2 laptop views
```

The same idea is used for mobile devices:

```sql
CASE 
  WHEN device_type IN ('tablet', 'phone') THEN 1 
  ELSE 0 
END
```

which produces:

| `device_type` | `CASE` Result |
| ------------- | ------------: |
| tablet        |             1 |
| laptop        |             0 |
| laptop        |             0 |
| phone         |             1 |
| tablet        |             1 |

So:

```text
1 + 0 + 0 + 1 + 1 = 3 mobile views
```

---

## Key Idea

Both approaches perform **conditional aggregation**.

```text
COUNT() + FILTER
```

and

```text
SUM() + CASE
```

are two ways to count only rows that satisfy a condition.

For this problem:

```text
Laptop Views = count rows where device_type = 'laptop'

Mobile Views = count rows where device_type = 'tablet' OR 'phone'
```

`FILTER` is more concise, while `SUM()` with `CASE` is a very common pattern that works across many SQL databases.

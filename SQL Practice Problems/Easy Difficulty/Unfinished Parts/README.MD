## Unfinished Parts

## Tesla SQL Interview Question

Tesla is investigating production bottlenecks and needs your help extracting the relevant data.

Write a query to determine which parts have **begun the assembly process but are not yet finished**.

### Assumptions

* The `parts_assembly` table contains all parts currently in production, each at varying stages of the assembly process.
* An unfinished part is one that does **not** have a `finish_date`.

This question is straightforward, so the solution should stay simple.

> Effective April 11, 2023, the problem statement and assumptions were updated for clarity.

---

### `parts_assembly` Table

| Column Name     | Type     |
| --------------- | -------- |
| `part`          | string   |
| `finish_date`   | datetime |
| `assembly_step` | integer  |

### `parts_assembly` Example Input

| `part`  | `finish_date`       | `assembly_step` |
| ------- | ------------------- | --------------: |
| battery | 01/22/2022 00:00:00 |               1 |
| battery | 02/22/2022 00:00:00 |               2 |
| battery | 03/22/2022 00:00:00 |               3 |
| bumper  | 01/22/2022 00:00:00 |               1 |
| bumper  | 02/22/2022 00:00:00 |               2 |
| bumper  | `NULL`              |               3 |
| bumper  | `NULL`              |               4 |

---

### Example Output

| `part` | `assembly_step` |
| ------ | --------------: |
| bumper |               3 |
| bumper |               4 |

### Explanation

The bumper rows for assembly steps `3` and `4` are unfinished because they do not have a recorded `finish_date`.

In SQL, a missing value is represented by:

```text
NULL
```

So the key idea is to find rows where:

```sql
finish_date IS NULL
```

> The dataset you are querying against may have different input and output. **This is just an example.**

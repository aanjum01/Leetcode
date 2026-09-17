This is the same question as problem #3 in the SQL Chapter of [Ace the Data Science Interview](https://amzn.to/3kF79Fx)!

Assume you're given a table containing user viewership categorized by device type. The three device types are:

* `laptop`
* `tablet`
* `phone`

Write a query that calculates:

* Total viewership for **laptops**
* Total viewership for **mobile devices**, where mobile is defined as the sum of `tablet` and `phone` viewership

Output the total laptop viewership as `laptop_views` and the total mobile viewership as `mobile_views`.

> Effective April 15, 2023, the solution was updated with a more concise and easy-to-understand approach.

---

### `viewership` Table

| Column Name   | Type                                 |
| ------------- | ------------------------------------ |
| `user_id`     | integer                              |
| `device_type` | string (`laptop`, `tablet`, `phone`) |
| `view_time`   | timestamp                            |

### `viewership` Example Input

| `user_id` | `device_type` | `view_time`         |
| --------: | ------------- | ------------------- |
|       123 | tablet        | 01/02/2022 00:00:00 |
|       125 | laptop        | 01/07/2022 00:00:00 |
|       128 | laptop        | 02/09/2022 00:00:00 |
|       129 | phone         | 02/09/2022 00:00:00 |
|       145 | tablet        | 02/24/2022 00:00:00 |

---

### Example Output

| `laptop_views` | `mobile_views` |
| -------------: | -------------: |
|              2 |              3 |

### Explanation

Based on the example input:

* There are **2 laptop views**
* There are **3 mobile views**

Mobile viewership is calculated as:

```text
tablet views + phone views
```

So in this example:

```text
2 tablet views + 1 phone view = 3 mobile views
```

> The dataset you are querying against may have different input and output. **This is just an example.**

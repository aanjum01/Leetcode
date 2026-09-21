## Teams Power Users

## Microsoft SQL Interview Question

Write a query to identify the **top 2 Power Users** who sent the highest number of messages on Microsoft Teams in **August 2022**.

Display:

* The IDs of these 2 users
* The total number of messages each user sent

Output the results in **descending order** based on the number of messages sent.

### Assumption

* No two users sent the same number of messages in August 2022.

---

### `messages` Table

| Column Name   | Type     |
| ------------- | -------- |
| `message_id`  | integer  |
| `sender_id`   | integer  |
| `receiver_id` | integer  |
| `content`     | varchar  |
| `sent_date`   | datetime |

### `messages` Example Input

| `message_id` | `sender_id` | `receiver_id` | `content`               | `sent_date`         |
| -----------: | ----------: | ------------: | ----------------------- | ------------------- |
|          901 |        3601 |          4500 | You up?                 | 08/03/2022 00:00:00 |
|          902 |        4500 |          3601 | Only if you're buying   | 08/03/2022 00:00:00 |
|          743 |        3601 |          8752 | Let's take this offline | 06/14/2022 00:00:00 |
|          922 |        3601 |          4500 | Get on the call         | 08/10/2022 00:00:00 |

---

### Example Output

| `sender_id` | `message_count` |
| ----------: | --------------: |
|        3601 |               2 |
|        4500 |               1 |

### Explanation

In August 2022:

* User `3601` sent **2 messages**
* User `4500` sent **1 message**

The June message sent by user `3601` is not included because the query only considers messages sent during August 2022.

> The dataset you are querying against may have different input and output. **This is just an example.**

---

## Hint #1

Take the problem one step at a time.

First, make sure we only include messages sent in **August 2022**.

We can extract the month and year from `sent_date` using the [`EXTRACT`](https://www.postgresqltutorial.com/postgresql-date-functions/postgresql-extract/) function.

```sql
SELECT 
  sender_id, 
  message_id
FROM messages
WHERE EXTRACT(MONTH FROM sent_date) = 8
  AND EXTRACT(YEAR FROM sent_date) = 2022;
```

This filters the table so that only messages sent in August 2022 remain.

Now ask:

> How can we determine how many messages each user sent?

Use:

```text
COUNT()
+
GROUP BY
```

---

## Hint #2

Your query should now look similar to:

```sql
SELECT 
  sender_id,
  COUNT(message_id) AS message_count
FROM messages
WHERE EXTRACT(MONTH FROM sent_date) = 8
  AND EXTRACT(YEAR FROM sent_date) = 2022
GROUP BY sender_id;
```

### What Does `GROUP BY` Do Here?

```sql
GROUP BY sender_id
```

puts all messages sent by the same user into one group.

For example:

```text
sender_id    message_id
---------    ----------
3601         901
4500         902
3601         922
```

After:

```sql
GROUP BY sender_id
```

conceptually, SQL creates:

```text
3601 → [901, 922]
4500 → [902]
```

Then:

```sql
COUNT(message_id)
```

counts the messages in each group:

```text
3601 → 2
4500 → 1
```

---

Now we need to find the **2 users with the highest message counts**.

Start with:

```sql
SELECT 
  sender_id,
  COUNT(message_id) AS message_count
FROM messages
WHERE EXTRACT(MONTH FROM sent_date) = 8
  AND EXTRACT(YEAR FROM sent_date) = 2022
GROUP BY sender_id
ORDER BY _____ DESC
LIMIT _____;
```

Think about:

```text
What column should we sort by?
```

and:

```text
How many rows should we keep?
```

---

## Final Query

```sql
SELECT 
  sender_id,
  COUNT(message_id) AS message_count
FROM messages
WHERE EXTRACT(MONTH FROM sent_date) = 8
  AND EXTRACT(YEAR FROM sent_date) = 2022
GROUP BY sender_id
ORDER BY message_count DESC
LIMIT 2;
```

---

## How to Read the Query

```sql
FROM messages
```

Start with the `messages` table.

```sql
WHERE EXTRACT(MONTH FROM sent_date) = 8
  AND EXTRACT(YEAR FROM sent_date) = 2022
```

Keep only messages sent during **August 2022**.

```sql
GROUP BY sender_id
```

Put all messages sent by the same user into one group.

```sql
COUNT(message_id) AS message_count
```

Count how many messages each user sent.

```sql
ORDER BY message_count DESC
```

Sort users from the **highest number of messages to the lowest**.

```sql
LIMIT 2
```

Keep only the first **2 users**.

---

## Key Pattern to Remember

This problem follows a very common SQL pattern:

```text
Filter
   ↓
Group
   ↓
Aggregate
   ↓
Sort
   ↓
Limit
```

In SQL:

```sql
SELECT group_column, COUNT(*)
FROM table
WHERE condition
GROUP BY group_column
ORDER BY COUNT(*) DESC
LIMIT n;
```

This pattern is useful whenever a question asks for something like:

> Find the **top N** users, products, customers, employees, or categories based on some count.

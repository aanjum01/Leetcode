## Histogram of Tweets

## Twitter SQL Interview Question

This is the same question as problem #6 in the SQL Chapter of [Ace the Data Science Interview](https://amzn.to/3kF79Fx)!

Assume you're given a table containing Twitter tweet data. Write a query to obtain a histogram of tweets posted per user in 2022.

Output:

* The **tweet count per user** as the bucket.
* The **number of Twitter users** who fall into that bucket.

In other words, group users by the number of tweets they posted in 2022, then count the number of users in each group.

### `tweets` Table

| Column Name  | Type      |
| ------------ | --------- |
| `tweet_id`   | integer   |
| `user_id`    | integer   |
| `msg`        | string    |
| `tweet_date` | timestamp |

### `tweets` Example Input

| `tweet_id` | `user_id` | `msg`                                                             | `tweet_date`        |
| ---------: | --------: | ----------------------------------------------------------------- | ------------------- |
|     214252 |       111 | Am considering taking Tesla private at $420. Funding secured.     | 12/30/2021 00:00:00 |
|     739252 |       111 | Despite the constant negative press covfefe                       | 01/01/2022 00:00:00 |
|     846402 |       111 | Following @NickSinghTech on Twitter changed my life!              | 02/14/2022 00:00:00 |
|     241425 |       254 | If the salary is so competitive why won’t you tell me what it is? | 03/01/2022 00:00:00 |
|     231574 |       148 | I no longer have a manager. I can't be managed                    | 03/23/2022 00:00:00 |

### Example Output

| `tweet_bucket` | `users_num` |
| -------------: | ----------: |
|              1 |           2 |
|              2 |           1 |

### Explanation

Based on the example output:

* Two users posted only **one tweet** in 2022.
* One user posted **two tweets** in 2022.

The query groups users by the number of tweets they posted and displays the number of users in each group.

> The dataset you are querying against may have different input and output. **This is just an example.**

---

## Hint #1

Eager beavers, let's forget about the Tweet activity histogram for a second and solve a simpler sub-problem:

**Can you figure out the total number of tweets made by each user in 2022?**

You'll want to use `COUNT` and `GROUP BY` for this:

```sql
SELECT ...
FROM tweets
GROUP BY ...;
```

---

## Hint #2

To find the total number of tweets made by each user in 2022, run:

```sql
SELECT 
  user_id, 
  COUNT(tweet_id) AS tweets_num 
FROM tweets 
WHERE tweet_date BETWEEN '2022-01-01' AND '2022-12-31' 
GROUP BY user_id;
```

Seriously, copy-paste the code into the editor and run it. I made DataLemur interactive for a damn reason!

Inspect the results.

`tweets_num` should look close-ish to the `tweet_bucket` column in the example output.

Can you use a **subquery** or **CTE** to take this intermediate result and shape it into the format the question is looking for?

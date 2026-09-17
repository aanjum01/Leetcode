with cte as(
SELECT 
  user_id,
  COUNT(tweet_id) as tweets_num
FROM tweets
WHERE tweet_date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY user_id
)

SELECT
  tweets_num as tweet_bucket,
  COUNT(user_id) as users_num
FROM cte
GROUP BY tweet_bucket
  
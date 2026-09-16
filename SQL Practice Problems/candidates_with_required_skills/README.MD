# Candidates With Required Skills

Given a table of candidates and their skills, you're tasked with finding the candidates best suited for an open Data Science job.

You want to find candidates who are proficient in:

- Python
- Tableau
- PostgreSQL

Write a query to list the candidates who possess **all** of the required skills for the job.

Sort the output by `candidate_id` in ascending order.

## Assumption

- There are no duplicates in the `candidates` table.

## `candidates` Table

| Column Name | Type |
|---|---|
| `candidate_id` | integer |
| `skill` | varchar |

## Example Input

| `candidate_id` | `skill` |
|---|---|
| 123 | Python |
| 123 | Tableau |
| 123 | PostgreSQL |
| 234 | R |
| 234 | PowerBI |
| 234 | SQL Server |
| 345 | Python |
| 345 | Tableau |

## Example Output

| `candidate_id` |
|---|
| 123 |

## Explanation

Candidate `123` is displayed because they have all three required skills:

- Python
- Tableau
- PostgreSQL

Candidate `345` is not included because they are missing one of the required skills: PostgreSQL.

> The dataset you are querying against may have different input and output. This is just an example.
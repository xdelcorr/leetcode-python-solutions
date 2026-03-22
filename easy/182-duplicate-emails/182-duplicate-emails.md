# Problem

Given a `Person` table, return all email addresses that appear more than once. Each duplicate email should be listed once in the result.

# Approach

The solution groups the rows by `email` and counts how many records belong to each email value. Once those counts are available, it filters the grouped result to keep only the emails whose count is greater than one.

After identifying the duplicated values, the result is renamed to match the required output format and reduced to the single output column.

# Key Idea

Count how many times each email appears, then keep only the emails with multiple occurrences.

# Step-by-Step Explanation

1. Group the `Person` DataFrame by the `email` column.
2. Count how many rows belong to each grouped email.
3. Convert the grouped result into a regular DataFrame with a `count` column.
4. Filter the rows to keep only records where `count > 1`.
5. Rename the `email` column to `Email` so the output matches the expected column name.
6. Select only the `Email` column for the final result.
7. Return the filtered DataFrame.

# Code

```python
import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = (
        person.groupby("email")["id"]
        .size()
        .reset_index(name = "count")
        .query('count > 1')
        .rename(columns={'email': 'Email'})
        [['Email']]
    )
    return df
```

# Notes

- The grouped count is based on the number of rows associated with each email.
- The output includes each duplicated email only once.

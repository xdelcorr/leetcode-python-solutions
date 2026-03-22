# Problem

Given a `Person` table and an `Address` table, return each person's first name, last name, city, and state. If a person does not have a matching address record, the city and state should appear as `null`.

# Approach

The solution uses a left merge between `Person` and `Address` on `personId`. This keeps every row from the `Person` table while attaching matching address details when they exist.

After combining the two tables, the result is narrowed to the four required output columns: `firstName`, `lastName`, `city`, and `state`.

# Key Idea

Use a left join so that all people remain in the result, even when there is no corresponding row in the `Address` table.

# Step-by-Step Explanation

1. Start with the `Person` DataFrame because every person must appear in the final result.
2. Merge `Person` with `Address` using `personId` as the shared key.
3. Apply `how="left"` so unmatched people are still included.
4. Select only the columns required by the problem statement.
5. Return the resulting DataFrame.

# Code

```python
import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df = person.merge(address, on="personId", how="left")[
        ["firstName", "lastName", "city", "state"]
    ]
    return df
```

# Notes

- Missing address records naturally produce `null` values in the `city` and `state` columns after the left merge.
- The output order is not restricted, so no additional sorting is required.

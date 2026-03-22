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
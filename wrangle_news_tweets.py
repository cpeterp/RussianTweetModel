import twint
import pandas as pd

accounts = pd.read_csv("datasets/news-tweets/new_outlets-accounts.csv")

def harvest_account(row):
    print(row)
    c = twint.Config()
    c.Since = "2012-01-01"
    c.Store_csv = True
    c.Custom["tweet"] = ["id", "user_id", "created_at", "tweet", "urls", "username"]
    handle = row['handle']
    name = row['Name']
    lean = row['Lean']
    c.Output = "News_Tweets/" + handle
    c.Username = handle
    twint.run.Profile(c)
    
accounts.apply(harvest_account, axis=1)
# ARE FOR TESTING CODE

import pandas as pd
from datetime import datetime


user_database = {"username": ["user1_username"],
                 "user_first_name": ["user1_first_name"],
                 "user_last_name": ["user1_last_name"],
                 "user_email": ["user1_email"],
                 "user_date_of_creation": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]}
user_database_df = pd.DataFrame(user_database, index=["user1"])

new_user = {"username": ["aa"],
            "user_first_name": ["aa"],
            "user_last_name": ["aa"],
            "user_email": ["aa"],
            "user_date_of_creation": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]}
new_user_df = pd.DataFrame(new_user, index=["aa"])
updated_df = pd.concat([user_database_df, new_user_df])

with open("testing.csv", 'w') as csv:
    updated_df.to_csv(csv)

print(updated_df)

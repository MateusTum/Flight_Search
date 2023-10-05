import pandas as pd
from datetime import datetime


class UserManager:
    # This class is responsible for managing the user database
    def __init__(self, users_database_csv_filepath):
        self.users_database_csv_filepath = users_database_csv_filepath
        self.load_users_dataframe()

    # ====== Functions related to dataframe/csv ======
    def load_users_dataframe(self):
        try:
            with open(self.users_database_csv_filepath, 'r') as data:
                user_database_df = pd.read_csv(data, index_col="user_id")
            print("Df loaded")
        except FileNotFoundError:
            print("Csv file is empty or doesn't exist")
            print("Creating a new csv file...")
            user_database = {"username": ["user1_username"],
                             "user_first_name": ["user1_first_name"],
                             "user_last_name": ["user1_last_name"],
                             "user_email": ["user1_email"],
                             "user_date_of_creation": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                             "user_last_update": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]}
            user_database_df = pd.DataFrame(user_database, index=["1"])
            print(user_database_df)
            self.save_df_to_csv(user_database_df)
            print("Csv file created")
        else:
            return user_database_df

    def save_df_to_csv(self, df):
        new_df = df.reset_index(drop=True)
        new_df.to_csv(self.users_database_csv_filepath, lineterminator='\n', index=True, index_label="user_id")

    def read_users_dataframe(self) -> pd.DataFrame:
        with open(self.users_database_csv_filepath, 'r') as read_users_data:
            user_database_df = pd.read_csv(read_users_data, index_col="user_id")
            return user_database_df

    def print_df(self):
        print(self.load_users_dataframe())

    # ====== Methods for user control/creation ======
    def add_user(self):
        new_user_username = input("Type an username: ")
        new_user_first_name = input("What is your first name? ")
        new_user_last_name = input("What is your last name? ")
        new_user_email = input("What is your email? ")
        check_email = False
        while not check_email:
            check_new_user_email = input("Type your email again:")
            if check_new_user_email == new_user_email:
                check_email = True
            else:
                print("You typed two different emails, try again")

        new_user = {"username": [new_user_username],
                    "user_first_name": [new_user_first_name],
                    "user_last_name": [new_user_last_name],
                    "user_email": [new_user_email],
                    "user_date_of_creation": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                    "user_last_update": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]}

        new_user_df = pd.DataFrame(new_user)
        updated_df = pd.concat([self.load_users_dataframe(), new_user_df])
        self.save_df_to_csv(updated_df)

    def update_user(self):
        user_id = int(input("Type the user_id to update its data: "))
        try:
            users_df_copy = self.read_users_dataframe().copy()
            user_to_update = users_df_copy.loc[user_id]
        except KeyError:
            print("User not found")
        else:
            keep_updating = True
            while keep_updating:
                print("User information:")
                print(user_to_update)
                update_choice = input("What do you want to update? (type 'exit' to exit this function)")
                if update_choice == "user_first_name":
                    users_df_copy.loc[user_id, 'user_first_name'] = input("What is the new user's first name? ")
                    users_df_copy.loc[user_id, 'user_last_update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"New first name was updated to: {users_df_copy.loc[user_id, 'user_first_name']}")
                elif update_choice == "user_last_name":
                    users_df_copy.loc[user_id, 'user_last_name'] = input("What is the new user's last name? ")
                    users_df_copy.loc[user_id, 'user_last_update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"New last name was updated to: {users_df_copy.loc[user_id, 'user_last_name']}")
                elif update_choice == "user_email":
                    users_df_copy.loc[user_id, 'user_email'] = input("What is the new user's email? ")
                    users_df_copy.loc[user_id, 'user_last_update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"New user's email was updated to: {users_df_copy.loc[user_id, 'user_email']}")
                else:
                    keep_updating = False
            self.save_df_to_csv(users_df_copy)

    def delete_user(self):
        user_to_delete = input("Type the username to delete all its data from the database: ")
        try:
            updated_df = self.load_users_dataframe().drop(user_to_delete, inplace=False)
        except KeyError:
            print("Username not found")
        else:
            self.save_df_to_csv(updated_df)

    # ====== Methods for user info collection ======
    def get_user_info(self):
        user_to_get_info = input("Type the username to get its data")
        try:
            user_info = self.read_users_dataframe().loc[user_to_get_info]
        except KeyError:
            print("Username not found")
        else:
            print(user_info)

    def get_all_users(self):
        total_users = len(self.read_users_dataframe())
        print(f"Total users: {total_users}\n")
        for index, row in self.read_users_dataframe().iterrows():
            print(f"User_id: {index}")
            print(f"{row}\n")


# running = True
# UserManager = UserManager(users_database_csv_filepath="../user_database.csv")
#
# while running:
#     run_what = input("Run a function: ")
#     if run_what == "add":
#         UserManager.add_user()
#     elif run_what == "get":
#         UserManager.get_all_users()
#     elif run_what == "print":
#         UserManager.print_df()
#     elif run_what == "update":
#         UserManager.update_user()
#     elif run_what == "delete":
#         UserManager.delete_user()
#     elif run_what == "exit":
#         running = False

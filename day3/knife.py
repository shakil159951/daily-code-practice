def greet_users(user_list):
    for name in user_list:
        if name.lower() == "admin":
            print(f"Hello {name}, would you like a status report?")
        else:
            print(f"Hello {name}, thanks for logging in again.")

users = ["Adam", "Bob", "Admin", "Charlie"]
greet_users(users)

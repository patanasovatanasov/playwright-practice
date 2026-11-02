users = [("admin", "1234"), ("guest", "guest"), ("petar", "pass")]

for user, pwd in users:
    if len(pwd) < 5:
        print(user, pwd)

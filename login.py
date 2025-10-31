# Dictionary of usernames and passwords
users = {
    "admin": "12345",
    "john": "pass123",
    "alice": "qwerty"
}

username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password:
    print(f"✅ Welcome, {username}!")
else:
    print("❌ Invalid login.")

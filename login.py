# Dictionary of usernames and passwords
users = {
    "admin": "12345",
    "john": "pass123",
    "alice": "qwerty"
}

username = input("Enter your Username: ")
password = input("Enter your Password: ")

if username in users and users[username] == password:
    print(f"✅ Welcome, {username}! You have successfully logged in.")
else:
    print("❌ Invalid login.")

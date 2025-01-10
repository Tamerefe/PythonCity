import getpass

users = {
    "user1": "password123",
    "user2": "mypassword",
    "admin": "adminpass"
}

def authenticate(username, password):
    if username in users and users[username] == password:
        return True
    return False

def main():
    print("Welcome to the Password Authentication System")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    if authenticate(username, password):
        print("Authentication successful!")
    else:
        print("Authentication failed. Invalid username or password.")

if __name__ == "__main__":
    main()
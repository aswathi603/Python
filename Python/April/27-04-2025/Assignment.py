'''
You need to create a signup and login page for social Media platform 
1.you have to ask the user whether they want to login pr signup 
2.if user says login then we have to ask for username and password and then we have to check it is valid user or not where we stored the user name and passwords 
    a) if it is the first time the user is using this and click the signup page then we have to redirected it into sign up page
3.if user says sign up you need to ask username and password and then store it 
4.Once the user looged in then you need to ask the user to Post something:-
    a.User can post on the platform 
    b.user can see alla the post done by user
'''

users = {}  # Stores username: password
posts = {}  # Stores username: list of posts

def signup():
    print("=== Signup ===")
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists. Please login.")
        return None
    password = input("Enter new password: ")
    users[username] = password
    posts[username] = []
    print("Signup successful! Please login.")
    return None

def login():
    print("=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials or user does not exist.")
        return None

def user_menu(username):
    while True:
        print("\n1. Post something")
        print("2. See all your posts")
        print("3. Logout")
        choice = input("Choose an option: ")
        if choice == "1":
            post = input("Write your post: ")
            posts[username].append(post)
            print("Post added!")
        elif choice == "2":
            print("Your posts:")
            for idx, post in enumerate(posts[username], 1):
                print(f"{idx}. {post}")
        elif choice == "3":
            print("Logged out.")
            break
        else:
            print("Invalid option.")

def main():
    while True:
        print("\nWelcome to Social Media Platform")
        action = input("Do you want to login or signup? (login/signup/exit): ").strip().lower()
        if action == "signup":
            signup()
        elif action == "login":
            user = login()
            if user:
                user_menu(user)
        elif action == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please type 'login', 'signup', or 'exit'.")

if __name__ == "__main__":
    main()


#  💻 Programming Task:
# Write a Python program that demonstrates the use of:

# Functions for modularity,

# File handling to log important events,

# Object-Oriented Programming (OOP) to model users and a database.

# 📝 Requirements:
# Error Logging:

# Whenever an error occurs, the program should automatically log the timestamp and a description of the error into a file.

# Database Modification Logging:

# When the database is modified, the program should:

# Record the timestamp of the modification,

# Log the user who performed the operation,

# Specify what change was made (e.g., key updated and old vs. new value).

# Structure:

# Use a class to represent the database.

# Use another class to represent a user who can perform operations on the database.

# Define separate functions for getting the current timestamp and logging events to a file.

# Output:

# All logs (errors and database edits) should be saved in a file (e.g., activity_log.txt) with appropriate labels and timestamps.

# Here's a Python program that demonstrates:

# Functions for modular code,

# File handling to log events (errors or database edits),

# OOP (Object-Oriented Programming) for managing users and a simulated database.

# ✅ Features:
# Logs errors with timestamps.

# Logs database edits with user info and timestamps.

# Simulates a user editing a basic in-memory "database".

# Python Code:
import datetime

# Function to get the current timestamp
def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to log activity to file
def log_event(event_type, message):
    with open("activity_log.txt", "a") as log_file:
        log_file.write(f"[{get_timestamp()}] {event_type}: {message}\n")

# Database class using OOP
class Database:
    def __init__(self):
        self.data = {}

    def update_entry(self, key, value, user):
        try:
            old_value = self.data.get(key, "None")
            self.data[key] = value
            log_event("DATABASE_EDIT", f"User '{user.username}' updated '{key}' from '{old_value}' to '{value}'")
        except Exception as e:
            log_event("ERROR", f"User '{user.username}' encountered an error: {str(e)}")

# User class
class User:
    def __init__(self, username):
        self.username = username

    def edit_database(self, db, key, value):
        db.update_entry(key, value, self)

# Simulate the program
def main():
    db = Database()
    user1 = User("Aswathi")
    user2 = User("Rahil")

    # Normal updates
    user1.edit_database(db, "age", 23)
    user2.edit_database(db, "location", "Delhi")

    # Simulate an error (e.g., updating with an invalid key type)
    try:
        user1.edit_database(db, ["invalid_key"], "value")
    except Exception as e:
        log_event("ERROR", f"Unhandled error: {str(e)}")

if __name__ == "__main__":
    main()


# 📁 Output (activity_log.txt will look like this):
# [2025-05-22 17:40:22] DATABASE_EDIT: User 'Aswathi' updated 'age' from 'None' to '23'
# [2025-05-22 17:40:22] DATABASE_EDIT: User 'Rahil' updated 'location' from 'None' to 'Delhi'
# [2025-05-22 17:40:22] ERROR: User 'Aswathi' encountered an error: unhashable type: 'list'
# 🧠 Key Concepts Used:
# OOP: User and Database classes.

# Functions: log_event(), get_timestamp().

# File Handling: Logging to activity_log.txt.

# Error Handling: try-except blocks log exceptions.
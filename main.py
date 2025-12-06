import sqlite3
import sys

def connect_db():
    """Connect to the SQLite database (conference.db)."""
    return sqlite3.connect("conference.db")

def main_menu():
    """Display the main menu options."""
    print("\n Conference Program Menu")
    print("1. Add Session")
    print("2. Add Speaker")
    print("3. Assign Speaker to Session")
    print("4. View Sessions")
    print("5. View Speakers")
    print("6. Exit")
    sys.stdout.flush()

def run():
    """Run the conference management system."""
    conn = connect_db()
    cursor = conn.cursor()

    while True:
        main_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Session title: ")
            location = input("Location: ")
            time = input("Time: ")
            cursor.execute(
                "INSERT INTO session (title, location, time) VALUES (?, ?, ?)",
                (title, location, time)
            )
            conn.commit()
            print(" Session added.")

        elif choice == "2":
            name = input("Speaker name: ")
            bio = input("Speaker bio: ")
            cursor.execute(
                "INSERT INTO speaker (name, bio) VALUES (?, ?)",
                (name, bio)
            )
            conn.commit()
            print(" Speaker added.")

        elif choice == "3":
            session_id = input("Session ID: ")
            speaker_id = input("Speaker ID: ")
            cursor.execute(
                "INSERT INTO session_speaker_xref (session_id, speaker_id) VALUES (?, ?)",
                (session_id, speaker_id)
            )
            conn.commit()
            print(" Speaker assigned to session.")

        elif choice == "4":
            cursor.execute("SELECT * FROM session")
            for row in cursor.fetchall():
                print(row)

        elif choice == "5":
            cursor.execute("SELECT * FROM speaker")
            for row in cursor.fetchall():
                print(row)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    conn.close()

def main():
    """Entry point for the program."""
    print("Welcome to the Conference Manager!")
    sys.stdout.flush()
    run()

if __name__ == "__main__":
    main()
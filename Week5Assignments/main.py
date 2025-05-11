from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, advanced_search, add_course, view_course, enrollcourse, searchcoursenuser

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Advance Search")
    print("6. Add Course")
    print("7. View all courses")
    print("8. enroll to a course")
    print("9. Search course for student ")
    print("10. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-10): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            user_id = input("Enter user ID to search: ")
            name = input("Enter name to search: ")
            users = advanced_search(user_id=user_id, name=name)
            for user in users:
                print(user)
        elif choice == '6':
            name = input("Enter course name: ")
            unit = input("Enter course unit: ")
            add_course(name, unit)
        elif choice == '7':
            course = view_course()
            for user in course:
                print(user)
        elif choice == '8':
            user_id = input("Enter user ID to enroll: ")
            course_id = input("Enter course ID to enroll in: ")
            enrollcourse(user_id, course_id)
        elif choice == '9':
            course_id = input("Enter course ID to search: ")
            user_name = input("Enter user name to search: ")
            results = searchcoursenuser(course_id=course_id, user_name=user_name)
            for row in results:
                print(f"{row[1]} is registered to {row[4]} and course ID is ({row[3]})")
        elif choice == '10':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

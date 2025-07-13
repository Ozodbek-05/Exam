from apps.auth.views import register, login, logout
from apps.slots.admin_views import *
from apps.slots.user_views import *
from apps.slots.views import show_all_timeslots


def auth_menu():
    print("""
    1. Register
    2. Login
    3. Exit
    """)
    choice = input("Choice: ")
    if choice == "1":
        if register():
            print("Successfully registered")
        else:
            print("Something went wrong")
    elif choice == "2":
        result = login()
        if result == "admin":
            print("Welcome my owner")
            return admin_menu()
        elif result == "user":
            return user_menu()
        else:
            return login()
    elif choice == "3":
        print("Good bye")
        return None
    else:
        print("Invalid choice")
    return auth_menu()


def admin_menu():
    print("""
    1. Add time slot
    2. Show all time slots
    3. Show all orders
    4. Show all users
    5. Logout
    """)
    choice = input("Choice: ")
    if choice == "1":
        add_timeslot()
    elif choice == "2":
        show_all_timeslots()
    elif choice == "3":
        show_all_orders()
    elif choice == "4":
        show_all_users()
    elif choice == "5":
        logout()
        return auth_menu()
    else:
        print("Invalid choice")
    return admin_menu()


def user_menu():
    print("""
    1. Show available time slots 
    2. Reserve a slot
    3. My reservations
    4. Logout
    """)
    choice = input("Choice: ")
    if choice == "1":
        show_all_timeslots()
        
    elif choice == "2":
        reserve_slot()
        
    elif choice == '3':
        my_reservations()
        
    elif choice == "4":
        logout()
        return auth_menu()
    
    else:
        print("Invalid choice")

    return user_menu()


if __name__ == '__main__':
    logout()
    auth_menu()

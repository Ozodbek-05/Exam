from core.file_manager import *
from core.utils import get_next_id


def add_timeslot():
    start_time = input("Start time: (ex, 11:00): ")
    end_time = input("End time: (ex, 12:00): ")
    limit = input("Max order quantity: ")

    next_id = get_next_id("slots")
    append(filename="slots", data=[next_id, start_time, end_time, limit])
    print("Time interval is added successfully!")


def show_all_orders():
    orders = read("orders")
    if orders:
        for order in orders:
            print(f"Name: {order[-1]}  Slot ID: {order[0]} | Start time: {order[1]} | End time: {order[2]} | Limit: {order[3]}")
    else:
        print("No orders found")


def show_all_users():
    users = read("users")
    if users:
        for user in users:
            print(f"User ID: {user[0]}  Name: {user[1]}  Email: {user[2]} Datetime: {user[-1]}")
    else:
        print("Users not found!!!")
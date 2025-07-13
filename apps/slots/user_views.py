from apps.slots.views import show_all_timeslots
from core.file_manager import *
from apps.auth.utils import get_user_active



def reserve_slot():
    user = get_user_active()
    show_all_timeslots()
    order_slot = input("Enter time interval id: ")
    slots = read("slots")
    if slots:
        for index, slot in enumerate(slots):
            if slot[0].strip() == order_slot.strip():
                append("orders", data=[slot[0], user[0], user[1], slot[1], slot[2]])
                if slot[0] == order_slot and int(slot[-1]) >= 1:
                    slots[index][-1] = int(slots[index][-1]) - 1
                    writerows(filename='slots', data=slots)
                    print("Time has been reserved")
                    return         
    else:
        print("Time slots not found!!")




def my_reservations():
    user = get_user_active()
    if not user:
        print("Active user not found!")
        return

    orders = read("orders")
    if not orders:
        print("No orders found.")
        return

    print("<<< My Reservations >>>")
    found = False
    for order in orders:
        if order[1].strip() == user[0].strip():  # order[1] — user_id
            print(f"Slot ID: {order[0]} | Start time: {order[3]} | End time: {order[4]}")
            found = True

    if not found:
        print("You don't have any reservations.")




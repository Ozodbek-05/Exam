from core.file_manager import read


def show_all_timeslots():
    timeslots = read(filename="slots")
    if not timeslots:
        print("No time interval found!")
        return

    print("\nAll time intervals:\n")
    for slot in timeslots:
        print(f"Slot ID: {slot[0]} | Start time: {slot[1]} | End time: {slot[2]} | Limit: {slot[3]}")

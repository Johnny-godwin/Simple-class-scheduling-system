class_schedules = []

def add_class():
    course = input("Enter course name: ")
    day = input("Enter day: ")
    time = input("Enter time: ")
    class_schedules.append({"course": course, "day": day, "time": time})
    print("Class scheduled successfully")

def view_classes():
    if not class_schedules:
        print("No class schedules available")
    else:
        for cls in class_schedules:
            print(cls["course"], "-", cls["day"], "-", cls["time"])

def main():
    while True:
        print("1. Add Class Schedule")
        print("2. View Class Schedules")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_class()
        elif choice == "2":
            view_classes()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()

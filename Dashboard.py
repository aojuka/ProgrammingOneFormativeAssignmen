import Student_Grade_Traker as st

def stater():

    while True:
        user_choice=input(
            "To proceed tracking your assignments, type Yes\n"
            "Let's first take some important information from you\n"
            "(use 'exit' to end the program\n): "
        ).strip().lower()

        if user_choice in ("yes","exit"):
            return user_choice
        else:
            print("Huh! Not the output I expected, but let's give it another try.\n")

def show_menu():
    menu = [
        "1) Add homework",
        "2) Add exam",
        "3) List assignments",
        "4) Filter (by subject / type / month)",
        "5) Show summary",
        "6) Change name",
        "0) Exit",
    ]
    for line in menu:
        print(line)

def filterer(tracker):

    print("Filter by: 1) Type  2) Subject  3) Month")
    sub_choice = input("Choose an option: ").strip()

    if sub_choice == "1":
        value = input("Enter type (homework/exam): ")
        tracker.filter_assignments("type", value)
    elif sub_choice == "2":
        value = input("Enter subject: ")
        tracker.filter_assignments("subject", value)
    elif sub_choice == "3":
        value = input("Enter month (YYYY-MM): ")
        tracker.filter_assignments("month", value)
    else:
        print("Invalid filter option.")

def run_my_program():

    print("~." * 40)
    print("Welcome to My Bevelovent Assignment Tracker")
    print("~." * 40 + "\n")

    user = st.Student_information()
    tracker = st.Gradetraker(user)

    while True:
        user.display_student()
        show_menu()
        option = input("Choose your Menu option: ").strip()

        if option == "1":
            tracker.add_assignments("homework")
        elif option == "2":
            tracker.add_assignments("exam")
        elif option == "3":
            tracker.list_assignment()
        elif option == "4":
            filterer(tracker)
        elif option == "5":
            tracker.show_summary()
        elif option == "6":
            new_name = input("Enter your new name: ")
            user.set_name(new_name)
        elif option == "0":
            print("Session ended. All the best, mon pote!")
            break
        else:
            print("Invalid menu option — please choose a number from the list.\n")

def main_file_runner():

    while True:
        start =stater()
        if start == "exit" :
            print("Sorry we were never meant to be, all the best mon pote")
            exit()
        else:
            run_my_program()

if __name__ == "__main__" :
    main_file_runner()
else:
    "You have to run this module directly"

 


    

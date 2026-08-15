import datetime as dt

class Homework:

    def __init__(self):

        self.type = "Homework"

        due_date_input = input("Enter Due Date -1856-07-10 :")
        due_date= dt.date.fromisoformat(due_date_input)

        self.due_date = due_date

user1 = Homework()




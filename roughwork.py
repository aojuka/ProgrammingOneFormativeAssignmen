import datetime as dt

#due_date_input = input("Enter Due Date -1856-07-10 :")

sample_due_dates = [
    "1856-07-10",
    "2026-08-15",
    "1856-07-10",
    "2026-12-31",
    "1900-01-01",
    "2030-05-20"
]
#due_date= dt.date.fromisoformat(due_date_input)
refined=[]
for i in sample_due_dates:
    due_date_list= dt.date.fromisoformat(i)
    refined.append(due_date_list)

print(refined)

sortedd=list(filter(lambda p: p.month >= 7,refined)).sort()

filtered_dates = list(filter(lambda p: p.month >= 7, refined))

# Sorts directly on the existing list
filtered_dates.sort() 

print(filtered_dates)
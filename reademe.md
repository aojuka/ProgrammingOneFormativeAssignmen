# Student Grade / Assignment Tracker

## Project Overview
This is my Programming 1 formative project. I created a command-line Student Grade Tracker using Python.

The program allows a student to add homework and exam results, see all the assignments they have entered, filter them, and view a summary of their grades. The data is only kept while the program is running.

## Features
1. Add homework and exam results
2. Store subject, title, score, maximum score, due date, and assignment type
3. Prevent duplicate assignments
4. List assignments in a readable table
5. Filter assignments by type or subject
6. Show overall grade average
7. Show per-subject averages
8. Show highest and lowest scoring assignments
9. Validate names, student IDs, scores, dates, and menu choices
10. Change the student's name during the session

## OOP Structure
The project uses:
- `Student_information` for student details
- `Assignment` as the parent class
- `HomeWork` and `Exam` as subclasses of `Assignment`
- `Gradetraker` to manage assignment operations

## How to Run
1. Make sure Python 3 is installed.
2. Keep `Dashboard.py` and `Student_Grade_Traker.py` in the same folder.
3. Open a terminal in the project folder.
4. Run:

```bash
python Dashboard.py
```

## Menu Structure
```text
1) Add homework
2) Add exam
3) List assignments
4) Filter (by subject / type / month)
5) Show summary
6) Change name
0) Exit
```

## Sample Interaction
```text
Enter your name:Mary
Nice mary, please now enter your student ID: 12345
Mary, please enter your current cohort: 2026

Choose your Menu option: 1
Math,Algebra HW1,75,80,2026-08-15
Math has successfully been added !!!!

Choose your Menu option: 3
Title           Subject      Score    Max    Due Date      Type       Remarks
ALGEBRA HW1     math         75.0     80.0   2026-08-15    homework   A PLAIN
```
### Adding homework

```text
Choose your Menu option: 1

Enter Module, Subject, Score, Max Score, duedate:
Math,Algebra HW1,75,80,2026-08-15

Math has successfully been added!
```

### Listing assignments

```text
Title           Subject      Score    Max    Due Date       Type
ALGEBRA HW1     math         75.0     80.0   2026-08-15     homework
```

### Filtering

```text
Filter by: 1) Type  2) Subject  3) Month
Choose an option: 2
Enter subject: math
```

### Grade summary

```text
GRADE SUMMARY

Overall Average      : 93.75%

Per-Subject Averages:
Math                 : 93.75%

Highest Scoring      : ALGEBRA HW1 (93.75%)
Lowest Scoring       : ALGEBRA HW1 (93.75%)
```

## Files

- `Dashboard.py` - runs the menu and controls the program
- `Student_Grade_Traker.py` - contains the classes and the main grade tracker functions
- `README.md` - information about the project


## Notes
All assignment data is stored only while the program is running. No files or databases are used to save the data.

print("welcome to My Bevelovent assignment tracker")
User_creation=input("To proceed tracking you assignment,Type Yes" \
"\n Let's First take some important information from you " \
" \n (use-Exit to end the program): ")
if User_creation.strip().lower() == "yes":
    from Student_Grade_Traker import view_student_n_dashboard
    user1=view_student_n_dashboard
else:
    print("Sorry we were never Ment to be, All the best mon pote")
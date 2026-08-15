import Student_Grade_Traker as st
while True:
    print("~." * 40)
    print("welcome to My Bevelovent assignment tracker")
    print("~." * 40 +"\n" * 2)


    User_creation=input("To proceed tracking you assignment,Type Yes" \
        "\n Let's First take some important information from you " \
        " \n (use-Exit to end the program): "
    )


    if User_creation.strip().lower() == "yes":
        #from Student_Grade_Traker import Student_information
        user1=st.Student_information()

    elif User_creation.strip().lower() == "exit":
        print("Sorry we were never Ment to be, All the best mon pote")
        break
    else:
        print("Huhh! Not the output I expect bet lets give it another try")
        continue
        
    
    
    Menu=[ ''
        "1) Add homework" ,
        "2) Add exam",
        "3) List assignments ",
        "4) Filter (by subject / type / month) ",
        "5) Show summary" ,
        "0) Exit ",
        "6)Change Name"         #set fuction
    ]

    user1.display_student()

    for i in Menu:
        
        print(i)

    Menu_option=input("Choose your Menu option: ")

    match Menu_option :
        case "1" :
            Add_assignment_obj= st.Assignment()
        case "2" :
            Add_assignment_obj= st.Assignment()
        case "3" :
            Add_assignment_obj.show_modules()
        case "4" :
            pass
        case "5" :
            pass
        case "6" :
            pass
        case "0":
            pass

    

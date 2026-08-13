# One small code for  All one giant leep for mankind
class Student_information:                               #parent class to bare the student information,id ,and cohorty name..be sure to create a display dashboard
    def __init__(self):                                  #My user have the sol chance to input there actial name as the class instancitilizes
        self.__name=input("Enter your name: ")             # Apply Encampsulation to prevent accidental modification of student name once set 
        if self.__name.isalpha():                          #Just as simple error handling to mosdifiy before assignment deadline
                print( f"Welcome {self.__name} This is  your student tracker") 
        elif self.__name.isnumeric(): 
            print("Invalid input please try again")
        self.id=int(input(f" Nice {self.__name}, Please now enter your student ID: "))
        self.cohort=input(f"{self.__name}, Now Please enter your current cohort ")
    # Keep Dreaming big  Allan  
    def gett_name(self):
         return self.__name

class Assignments():     #subjrct ,title ,score, max score,due date, assignment type
    def __init__(self):
         attemps= 0
         modules_dict={}
         while attemps <= 3: #Consider While true for flexibility
             Module_name=input("Enter Module Name and Maximum score:- Math,80 ")
             attemps +=1
             Module_name_list=Module_name.split(",")
             modules_dict[Module_name_list[0]]=int(Module_name_list[1]) #Adds the module name and maximum score in the dictionary
         self.modules_dict= modules_dict
         self.titles=input("Now enter title of the module:  ")
         self.assingment_type=input("Now enter assignment type:  ")
         self.due_date=input("Now enter Due Date of the assignment:  ")
    def show_modules(self):
        print("═════════════════════════════════════")
        print(f"                          ")
        print("══════════════════════════════════════")
        for module,max_score  in self.modules_dict.items():
            if max_score >= 70:
                remarks= "Exellent"
            elif max_score >= 50:
                remarks= "ABOVE AVERAGE"
            else:
                remarks= "POOR"
            print(f"  {module}   {max_score}%  {remarks}")

        print("══════════════════════════════════════") 



class List_Assignment(Assignments):
     pass
class view_student_n_dashboard(Assignments):
     def view_Menu(self):
        info_dictionary=dict(
             welcome    = "╔══════════════════════════════════════╗",
        dashboard1 = f"║     GRADE TRACKER — {self.name}║",
        dashboard10 = f"║     GRADE TRACKER — {self.id}║",
        dashboard2 = "╠══════════════════════════════════════╣",
        dashboard3 = "║   1.   Add Homework                 ║",
        dashboard4 = "║   2.   Add Exam                     ║",
        dashboard5 = "║   3.   List Assignments             ║",
        dashboard6 = "║   4.   Filter Assignments           ║",
        dashboard7 = "║   5.   Show Summary                 ║",
        dashboard8 = "║   0.   Exit                         ║",
        dashboard9 = "╚══════════════════════════════════════╝"
        )
        for i in info_dictionary.values():
            print(i)  
     def user_options(self):
          pass    
class Grade_tracker:
     pass

student1=view_student_n_dashboard()

student1.Module_colecttor()

   
        

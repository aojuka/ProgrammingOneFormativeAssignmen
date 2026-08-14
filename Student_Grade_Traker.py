# One small code for  All one giant leep for mankind
class Student_information:                                        #parent class to bare the student information,id ,and cohorty name..be sure to create a display dashboard
    
     def __init__(self):
          
          self.__name=input("Enter your name: ")            
                                                                           
          if self.__name.isalpha():                                       #Just as simple error handling to mosdifiy before assignment deadline--# Apply Encampsulation to prevent accidental modification of student name once set 
               print( f"Welcome {self.__name} This is  your student tracker") 
          elif self.__name.isnumeric(): 
               print("Invalid input please try again")

          self.id=int(input(f" Nice {self.__name}, Please now enter your student ID: "))          
          self.cohort=input(f"{self.__name}, Now Please enter your current cohort ")

     # Keep Dreaming big  Allan  

     def get_name(self):
          return self.__name
     
     def set_name(self,New_name):
         self.__name= New_name
         

class Assignment(Student_information):
    def __init__(self):
        super().__init__()
        modules_dict={}
        
        while True:
            
            module_input= input(
                f"{self.get_name()} please enter Module, Subject, Score, Max Score, Due Date, Type\n"
                "Example: Math,Mathematics,75,80,2026-08-20,Exam\n"
                "or type 'done' to finish: "
            )
        
            if module_input.lower() == "done":
                break

            module_List= module_input.split(",")
            try:
                module_name= module_List[0]
                Subject_title= module_List[1]
                score= int(module_List[2])
                max_score= int(module_List[3])
                due_date= module_List[4]
                assignment_type= module_List[5]
            except:
                print("Opps you did not follow my instructions\n" \
                "Please ensure data was separated by a ',' only "
                "Example: Math,Mathematics,75,80,2026-08-20,Exam\n")
                continue

            #Data cleaning and validation of User Input
            pass
            pass 
            pass
            pass

            modules_dict[module_name]=[
                Subject_title,
                score,
                max_score,
                due_date,
                assignment_type
            ]
        self.modules_dict= modules_dict

    def show_modules(self):

        print("=" * 80)
        print("Module     Subject        Score    Max    Due Date      Type   Remarks")
        print("=" * 80)

        for module, values in self.modules_dict.items() :

            subject= values[0]
            score= values[1]
            max_score= values[2]
            due_date= values[3]
            ass_type= values[4]

            percentage= (score / max_score )* 100

            if percentage >= 70 :
                remarks = "Excellent"
            elif percentage >= 50 :
                remarks = "Excellent"
            else:
                remarks = "POOR"
                pass
                #TO ADD NOTESSS
            print(
                f"{module.upper():<10} " # :> right aligns the results with the available space
                f"{subject.capitalize():<12} "
                f"{score:<8} "
                f"{max_score:<6} "
                f"{due_date:<13} "
                f"{ass_type:<8} "
                f"{remarks}"
            )
        print("=" * 80)
            




    def add_to_existing(self):
        pass



class List_Assignment(Assignment):
     pass
class view_student_n_dashboard(Assignment):
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

student1.show_modules()

   
        

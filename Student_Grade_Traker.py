# One small code for  All one giant leep for mankind
import datetime as dt
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

          if New_name.replace(" ", "").isalpha():
               self.__name = New_name
          else:
               print("Invalid name.")

     def display_student(self):

          print("~." * 40)
          print("." * 25 + " Student Details " + "." * 25)
          print("═" * 80)

          print(f"Student ID : {self.id}")
          print(f"Name       : {self.__name}")
          print(f"Cohort     : {self.cohort}")

          print("═" * 80)



         

class Assignment(Student_information):
    def __init__(self):
        #super().__init__()
        modules_dict={}
        
        while True:
            
            module_input= input(
               f"{user1.get_name()} please enter Module, Subject, Score, Max Score, duedate\n"
               "Example: Math,Mathematics,75,80,\n"
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
               due_date= dt.date.fromisoformat(module_List[4]) 
               assignment_type= None
            except:
               print("Opps you did not follow my instructions\n" \
               "Please ensure data was separated by a ',' only "
               "Example: Math,Mathematics,75,80\n")
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
               f"{remarks}"
               f"{due_date:<13} "
               f"{ass_type:<8} "
            )
        print("=" * 80)
            




    def add_to_existing(self):
        pass

##def __init__(self):
          #super().__init__()
          #self.type = "Homework"

          #due_date_input = input("Enter Due Date -1856-07-10 :")
          ##self.due_date = due_date

#user1 = Homework()


















































    #pass


class Exams(Assignment):
    pass

class GradeTracker:
    pass

   
        

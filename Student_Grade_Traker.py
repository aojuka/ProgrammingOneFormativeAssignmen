# One small code for  All one giant leep for mankind
import datetime as dt



class Student_information:                                        #parent class to bare the student information,id ,and cohorty name..be sure to create a display dashboard
    
     def __init__(self):
         
         while True:
            name = input("Enter your name: ").strip()
            if name.isalpha():
                self.__name = name
                print(f"Welcome {self.__name}, this is your student tracker")
                break
            print("Invalid input — name must contain letters only. Please try again.")

         while True:
            id_input = input(f"Nice {self.__name}, please now enter your student ID: ").strip()
            if id_input.isdigit():
                self.id = int(id_input)
                break
            print("Invalid ID — please enter numbers only.")

         self.cohort = input(f"{self.__name}, please enter your current cohort: ").strip()
          
          

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



         

class Assignment: # Base class for grade item that my user will put

    def __init__(self,subject,title,score,max_score,due_date,assignmet_type):

        self.subject= subject.lower().strip()     
        self.title= title.upper().strip()
        self.score = float(score)
        self.max_score= float(max_score)
        self.due_date= due_date
        self.type = assignmet_type 

    def percent(self):
        return (self.score / self.max_score) * 100

    def remarks(self):
        percentage=self.percent()
        if percentage > 80 :
            return " A PLAIN"
        elif percentage >= 75 :
            return " A- minus"
        elif percentage >= 70 :
            return " B+ plus"
        elif percentage >= 60 :
            return " B PLAIN"
        elif percentage >= 50 :
            return " B- minus"
        else:
            return " 🤦‍♂️☠️☠️☠️"

    def __str__(self):                     # Controls what is output when the fuction is called
        return (
            f"{self.title: <15} "
            f"{self.subject: <12} "
            f"{self.score: <8.1f} "
            f"{self.max_score: <6.1f} "
            f"{self.due_date: <15} "
            f"{self.type: <15} "
            f"{self.remarks()} "
        )





    
class HomeWork(Assignment):  # to be a sub class of assignment ,hence to inherit from assignment

        def __init__(self, subject, title, score, max_score, due_date, assignmet_type):
            super().__init__(subject, title, score, max_score, due_date, assignmet_type="homework") # To always default to homework

class Exam(Assignment):

        def __init__(self, subject, title, score, max_score, due_date, assignmet_type):
             super().__init__(subject, title, score, max_score, due_date, assignmet_type="Exam")


















































    #pass


class Exams(Assignment):
    pass

class GradeTracker:
    pass

   
        

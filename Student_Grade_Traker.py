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

    def __init__(self,subject,title,score,max_score,due_date,assignment_type):

        self.subject= subject.lower().strip()     
        self.title= title.upper().strip()
        self.score = float(score)
        self.max_score= float(max_score)
        self.due_date= due_date
        self.type = assignment_type 

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





        # Sub classes of Assignment classs
class HomeWork(Assignment):  # to be a sub class of assignment ,hence to inherit from assignment

        def __init__(self, subject, title, score, max_score, due_date):
            super().__init__(subject, title, score, max_score, due_date, assignment_type="homework") # To always default to homework

class Exam(Assignment):

        def __init__(self, subject, title, score, max_score, due_date):
             super().__init__(subject, title, score, max_score, due_date, assignment_type="Exam")
        


class Gradetraker:

     def __init__(self,student):
          self.student= student
          self.modules=[]  # dictonary to capture assingments ----modifided to list

     def add_assignments(self,assignment_type):

          modules_input= input(
               f"{self.student.get_name()} please enter Module, Subject, Score, Max Score, duedate\n"
               "Example: Math,Mathematics,75,80,2026-08-15\n"
               "or type 'done' to finish: "
               )
          if modules_input.lower() == "done":
               return False

          modules_list= modules_input.split(",")

          if len(modules_list) != 5 :
               print(
                    "PLEASE-GIVE EXACTLY 5 VALUES ,SEPARRATED BY A COMMA.\n" \
               "Example: Mathematics,Algebra HW1,75,80,2026-08-15\n"
               "or type 'done' to finish"
               )

          module_name, Subject_title, score_string, max_score_str,due_date_str = [p.strip() for p in modules_list]    # List comprehence applied to clean user input and remove white space

          try:
               score_=float(score_string)
               max_score_= float(max_score_str)
          except:
               print("Score and Max must be numbers")
               return False

          if max_score_ <= 0:
               print("Max must be greater than 0")
               return False
          if score_ <= 0 or score_ > max_score_:
               print("score must be greater than 0 and max score ")
               return False

          try:
              due_date_str= dt.date.fromisoformat(due_date_str)
          except :
               print("Due date Must be in YYYY-MM-DD format or yyy/mm/dd")
               return False

          if assignment_type == "homework" :
               new_module= HomeWork(module_name, Subject_title, score_string, max_score_str,due_date_str)
          else:
               new_module= Exam(module_name, Subject_title, score_string, max_score_str,due_date_str)

          self.modules.append(new_module)
          print(f"{module_name} has succefully been add !!!!")
          return True            #to succeffully output add assignment without the none- like so that the functun es not return none
     

     def list_assignment(self, assingmnents=None):

          if assingmnents is None:
               assingmnents = self.modules

          if not assingmnents:
               print("No assignment add - so I can not show anything")
               return

          print("=" * 90)
          print(f"{'Title':<15} {'Subject':<12} {'Score':<8} {'Max':<6} {'Due Date':<13} {'Type':<10} Remarks")
          print("=" * 90)

          for i in assingmnents:
               print(i)
          print("=" * 90)


     def filter_assignments(self,by ,value):
          result=[]

          if by == "type":               
               for a in self.modules:
                    if a.type.lower().strip() == value.lower().strip():
                        result.append(a)
          elif by== "subject" :
               for a in self.modules:
                    if a.subject == value.lower().strip():
                         result.append(a)
          else:
               print("Unknow filter type.\n")
               return []
          self.list_assignment(result)

          return result
     def show_summary(self):

          if not self.modules:
               print("No assignments recorded yet — nothing to summarize.\n")
               return

          # calculate total score and max score using loops
          total_score= 0.0          
          total_max= 0.0
          for j in self.modules:
               total_score += j.score
               total_max   += j.max_score

          if total_max > 0 :
               overall_average =(total_score/total_max)  * 100 
          else:
               overall_average = 0

          #per- subject average using  loops
          
          subjects = {}
          for a in self.modules:
               if a.subject not in subjects:
                    subjects[a.subject] = {"score": 0.0, "max": 0.0}

               subjects[a.subject]["score"] += a.score
               subjects[a.subject]["max"] += a.max_score

          # find the highest and lowest scoring assignment

          highest_assignment=self.modules[0]
          lowest_assigment = self.modules[0]

          for item in self.modules:
               if item.percent() > highest_assignment.percent():
                    highest_assignment = item
               if item.percent() < lowest_assigment.percent():
                    lowest_assigment = item


          print("=" * 60)
          print("GRADE SUMMARY")
          print("=" * 60)
          print(f"Overall Average      : {overall_average:.2f}%")
          print("-" * 60)
          print("Per-Subject Averages:")

          for subject_name, data in subjects.items():
            if data["max"] > 0:
                sub_avg = (data["score"] / data["max"]) * 100
            else:
                sub_avg = 0
            print(f"  {subject_name.capitalize():<15}: {sub_avg:.2f}%")

          print("-" * 60)
          print(f"Highest Scoring      : {highest_assignment.title} ({highest_assignment.percent():.2f}%)")
          print(f"Lowest Scoring       : {lowest_assigment.title} ({lowest_assigment.percent():.2f}%)")
 
          


          





          

                    


          







          
          

          
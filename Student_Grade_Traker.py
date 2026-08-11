class Student_information:
    def __init__(self):
        self.name=input("Enter your name: ") # 
        if self.name.isalpha():
                print( f"Welcome {self.name} This is  your student tracker") 
        elif self.name.isnumeric():
            print("Invalid input please try again")
        self.cohort=input(f"{self.name}, Now Please enter your current cohort ")
        
class Assignments(Student_information):     
    def Module_colecttor():         
         attemps= 0
         modules={}
         while attemps <= 3:
             Module_name=input("Enter Module name and Grades:- Math,80 ")
             attemps +=1
             Module_name_list=Module_name.split(",")
             modules[Module_name_list[0]]=int(Module_name_list[1])
             return modules
     


class List_Assignment(Student_information):
     pass



class view1(Student_information,Assignments):
     def view(self):
        info_dictionary=dict(
             welcome    = "╔══════════════════════════════════════╗",
        dashboard1 = f"║     GRADE TRACKER — {self.name}║",
        dashboard2 = "╠══════════════════════════════════════╣",
        dashboard3 = "║   1.   Add Homework                ║",
        dashboard4 = "║   2.   Add Exam                    ║",
        dashboard5 = "║   3.   List Assignments            ║",
        dashboard6 = "║   4.   Filter Assignments          ║",
        dashboard7 = "║   5.   Show Summary                ║",
        dashboard8 = "║   0.   Exit                        ║",
        dashboard9 = "╚══════════════════════════════════════╝"
        )
        for i in info_dictionary.values():
            print(i)  
     
     
class Filter:
     pass

student1=view1()
student1.view()
   
        

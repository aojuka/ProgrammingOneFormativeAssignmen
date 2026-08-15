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





                       

                



  

                
        pass

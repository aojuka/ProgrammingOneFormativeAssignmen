class Assignment:
    def __init__(self):

        modules_dict={}
        
        while True:
            
            module_input= input(
                f"{"Name"} please enter Module, Subject, Score, Max Score, Due Date, Type\n"
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
user1=Assignment()
user1.show_modules()







 
             


            
          
    

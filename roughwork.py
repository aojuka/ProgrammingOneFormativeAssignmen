class Assignments():     #subjrct ,title ,score, max score,due date, assignment type
    def __init__(self):
         attemps= 0
         modules_dict={}
         Module_name[""]
         while attemps <= 3: #Consider While true for flexibility
             Module_name=input("Enter Module NAME,TITLE,SCORE,Max score,due date,assignment type:- Math,80 ")
             attemps +=1
             Module_name_list=Module_name.split(",")
             modules_dict[Module_name_list[0]]=int(Module_name_list[1]) #Adds the module name and maximum score in the dictionary
         self.modules_dict= modules_dict
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

 
             


            
          
    

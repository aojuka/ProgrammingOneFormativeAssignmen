
def Module_colecttor():
    attemps= 0
    modules={}
    while attemps <= 3:
        Module_name=input("Enter Module name and Grades:- Math,80 ")
        attemps +=1
        Module_name_list=Module_name.split(",")
        modules[Module_name_list[0]]=int(Module_name_list[1])
    return modules
class Assignments():     
    def __init__(self):
         attempts= 0
         modules_dict={}
         modules_dict["Modules"]=["subject","title","score" ,"Max_score","remark","assignment type"]
         while attempts <= 3: #Consider While true for flexibility
             Module_name=input("Enter Module name and max_score:- Math,80 ")
             attempts +=1
             Module_name_list=Module_name.split(",")
             modules_dict[Module_name_list[0]]=int(Module_name_list[1]) #Adds the module name and maximum score in the dictionary
         self.modules_dict= modules_dict
    def show_modules(self):
        print("═════════════════════════════════════════════════════════════════════════════════════")
        print(f"            {self.modules_dict["Modules"]}              ")
        print("══════════════════════════════════════════════════════════════════════════════════════")
        for module,max_score  in self.modules_dict.items():
            if max_score >= 70:
                remarks= "Exellent"
            elif max_score >= 50:
                remarks= "ABOVE AVERAGE"
            else:
                remarks= "POOR"
            print(f"  {module}   {max_score}%  {remarks}")

        print("══════════════════════════════════════") 
             
us1=Assignments()
us1.show_modules()

            
          
    

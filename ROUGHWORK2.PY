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




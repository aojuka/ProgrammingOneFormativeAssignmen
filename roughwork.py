
def Module_colecttor():
    attemps= 0
    modules={}
    while attemps <= 3:
        Module_name=input("Enter Module name and Grades:- Math,80 ")
        attemps +=1
        Module_name_list=Module_name.split(",")
        modules[Module_name_list[0]]=int(Module_name_list[1])
    return modules
        
            
          
    

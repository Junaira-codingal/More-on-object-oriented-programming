#creat class
class IOString( ):
    
    #constructor to set default value
    def __init__(self):
        self.str1 = ""
        
    def get_String(self):
        self.str1 = input("Enter String: ")
    
    def print_String(self):
        print(f"Result is:{self.str1.upper()} ")
        
#Object creation
strObj = IOString()

#Call functions
strObj.get_String( )
strObj.print_String()
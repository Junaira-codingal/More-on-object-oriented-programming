#Create Class
class Employee:
    
    #Initializing CONSTRUCTOR
    def __init__(self):
        print("Employee created")
        
    #Calling destructor
    def __del__(self):
        print("Destructor called")

def Creat_obj():
    print('Making Object...')
    objFunc = Employee()
    print("Function end...")
    return objFunc

print("Calling Create_obj( ) function...")
obj = Creat_obj()
print("Program End...")
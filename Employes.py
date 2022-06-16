
class Employee:
    
    def __init__(self, fname, lname):
        self.__FirstName = fname
        self.__LastName  = lname

    def set_first_name(self, fname):
        self.__FirstName = fname  # setter method

    def set_last_name(self, lname):
        self.__LastName = lname # setter method

    def get_first_name(self):
        return self.__FirstName # getter method

    def get_last_name(self):
        return self.__LastName # getter method


    def print_employee(self):
        print("First Name: " + self.__FirstName)
        print("Last Name: " + self.__LastName)
        

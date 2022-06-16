from CommisionEmployes import CommissionEmployee

class BasePlusCommissionEmployee(CommissionEmployee):
    def __init__(self, fname, lname, gross_sales, commission_rate, base_salary):
        super().__init__(fname, lname, gross_sales, commission_rate)
        self.__BaseSalary = base_salary

    def setbase_salary(self, base_salary):
        self.__BaseSalary = base_salary
    
    def getbase_salary(self):
        return self.__BaseSalary

    def print_employee(self):
        super().print_employee()
        print("Base Salary: " + str(self.__BaseSalary))
        print("Earnings: " + str(self.earnings()))

    def earnings(self):
        return self.__BaseSalary + super().earnings()
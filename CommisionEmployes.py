from Employes import Employee

class CommissionEmployee(Employee):
    def __init__(self, fname, lname, gross_sales, commission_rate):
        super().__init__(fname, lname)
        self.__GrossSales = gross_sales
        self.__CommissionRate = commission_rate
    
    def setgross_sales(self, gross_sales):
        self.__GrossSales = gross_sales

    def setcommission_rate(self, commission_rate):
        self.__CommissionRate = commission_rate

    def getgross_sales(self):
        return self.__GrossSales

    def getcommission_rate(self):
        return self.__CommissionRate

    def earnings(self):
        return self.__GrossSales * self.__CommissionRate

    def print_employee(self):
        super().print_employee()
        print("Gross Sales: " + str(self.__GrossSales))
        print("Commission Rate: " + str(self.__CommissionRate))
        print("Earnings: " + str(self.earnings()))
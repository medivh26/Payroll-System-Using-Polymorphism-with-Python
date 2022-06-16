import Employes
import CommisionEmployes
import BasePlusCommisionEmployes

def main():

    my_employee = Employes.Employee("John", "Smith")
    my_employee.print_employee()

    my_comm_employee = CommisionEmployes.CommissionEmployee("Sue", "Jones", 10000, 0.6)
    my_comm_employee.print_employee()
    my_comm_employee.earnings()

    my_base_comm_employee = BasePlusCommisionEmployes.BasePlusCommissionEmployee("Bob", "Lewis", 5000, 0.4, 300)
    my_base_comm_employee.print_employee()
    my_base_comm_employee.earnings()

main()
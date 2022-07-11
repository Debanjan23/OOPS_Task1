import logging

logging.basicConfig(filename = "encapsulation.log" ,  filemode= "w", level= logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s" )
logging.info("We are now inside encapsulation program")

"""In this program we are trying to implement encapsulation methodology"""

try:
    class iNeuron_employee:

        def __init__(self, employee_name, employee_salary, employee_doj):

             self.employee_name = employee_name
             self.__employee_salary = employee_salary
             self.__employee_doj = employee_doj

        def employee_current_salary(self):

            print("This is employees current salary ", self.__employee_salary)

        def employee_salary_changed(self, new_changed_salary):

            self.__employee_salary = new_changed_salary
            return "Salary has been changed"

except Exception as e:
    logging.exception(e)

emp1 = iNeuron_employee("Debanjan", "12 lac" , "23/09/2021")
emp1.employee_current_salary()
print(emp1.employee_salary_change("20 lac"))
emp1.employee_current_salary()


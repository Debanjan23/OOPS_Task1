import logging

logging.basicConfig(filename="Multilevel_Inherit.log",level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
logging.info("Entering into Task1 Program")

"""In this program we are trying to implement multilevel inheritance"""

class iNeuron:

   employee_name = ""
   total_no_of_employees = "600"
   no_of_departments = "6"
   asset_value = ""

   def set_employee_name(self, name):
     try:

        employee_name=name
        print(employee_name)
     except Exception as e:
        logging.exception(e)


class ineuron_testing_team(iNeuron):

    try:
      def Testing_to_Developement_qr_weekly(self):
         print("This is the weekly testing report for current project")
    except Exception as e:
       logging.exception(e)


class iNeuron_develpement_team(ineuron_testing_team):
   pass



f1 = iNeuron_develpement_team()
f1.set_employee_name("Debanjan")
f1.Testing_to_Developement_qr_weekly()
print(f1.employee_name)

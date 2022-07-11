import logging
from One_Neuron.Tech_neuron import Tech_neuron
from One_Neuron.Kids_neuron import Kids_neuron

logging.basicConfig(filename = "Raise_your_demand.log" ,  filemode= "w", level= logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s" )
logging.info("We are now inside Raise_your_demand program")

"""In this program we are trying to understand how to import external modules, classes and usage of them in the current package"""

try:
    class Raise_your_demand(Tech_neuron,Kids_neuron):

        def interested_in(self,value, candidate_name, course_name):

            if value =="Tech_neuron":
                self.student_name_tech = candidate_name
                self.course_name_tech = course_name
                print(self.student_name_tech,"intereseted in ",self.course_name_tech )

            elif value == "Kids_neuron":
                self.student_name_kid = candidate_name
                self.course_name_kid = course_name
                print(self.student_name_tech, "intereseted in", self.course_name_tech)

            else:
                print("Invalid Input")

except Exception as e:
    logging.exception(e)

t2 = Raise_your_demand()
t2.interested_in("Tech_neuron","Debanjan","DA")
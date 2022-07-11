import logging

logging.basicConfig(filename = "Tech_neuron.log" ,  filemode= "w", level= logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s" )
logging.info("We are now inside Tech Neuron program")

"""In this program we are trying to implement package-module concept"""
"""So we have created two packages under One_Neuron module"""

try:
    class Tech_neuron:

        def course_access(self):
            print("This is all about 200+ access to all the course")
        def student_name(self, name):
            self.student_name_tech = name
        def student_intereseted_course(self, course_name):
            self.course_name_tech = course_name

except Exception as e:
    logging.exception(e)


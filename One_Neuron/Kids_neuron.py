import logging

logging.basicConfig(filename = "Kids_neuron.log" ,  filemode= "w", level= logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s" )
logging.info("We are now inside Tech Neuron program")

"""In this program we are trying to implement package-module concept"""

try:
    class Kids_neuron:

        def student_name(self, name):
            self.student_name_kid = name
        def student_age(self, age):
            self.student_age = age
        def student_intereseted_course(self, course_name):
            self.course_name_kid = course_name

except Exception as e:
    logging.exception(e)
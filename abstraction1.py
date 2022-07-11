import logging

logging.basicConfig(filename = "abstraction1.log" ,  filemode= "w", level= logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s" )
logging.info("We are now inside abstratcion program")

"""In this program we are trying to implement data abstraction methodology"""

try:
    class iNeuron_students:

        __student_name = "Kailash"
        __student_assigned_course="Full Stack Data Science"
        __student_experience = "Fresher"

        def student_name(self):
            print("Student name is",self.__student_name)
        def student_assigned_course(self):
            print( self.__student_name," has been assigned to", self.__student_assigned_course)
        def student_experience(self):
            print("Student experience is", self.__student_experience)

except Exception as e:
    logging.exception(e)

s1 = iNeuron_students()
s1.student_name()
s1.student_assigned_course()
s1.student_experience()
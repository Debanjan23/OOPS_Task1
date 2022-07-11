import logging

logging.basicConfig(filename = "Polymorpsim.log" ,  filemode= "w", level= logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s" )
logging.info("We are now inside encapsulation program")

"""In this program we are trying to implement polymorpsim concept"""

try:
    class FSDS_course:

        def course_name(self):
            print("Course name is Full Stack Data science")
        def course_duration(self):
            print("Course duration is for 12 months")
        def course_eligiblity(self):
            print("B Tech/ B. E Graduate in any stream")
        def system_requirement(self):
            print("Good internet connection, Laptop/Desktop & dedication is required")

    class Data_Analytics:

        def course_name(self):
            print("Course name is Data Analytics")
        def course_duration(self):
            print("Course duration is for 4 months")
        def course_eligiblity(self):
            print("Graduate in any stream")
        def system_requirement(self):
            print("This is system requirement for data_analytics course")

    f1 = FSDS_course()
    d1 = Data_Analytics()

    for course in (f1,d1):

        course.course_name()
        course.course_duration()
        course.course_eligiblity()
        course.system_requirement()

except Exception as e:
    logging.exception()

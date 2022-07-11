import logging

logging.basicConfig(filename="Multiple_inherit.log",filemode="w",format="%(asctime)s %(levelname)s %(message)s")
logging.info("We are entering to Multiple inheritance")

try:

  class Ineuron_courses:

      def __init__(self, course_name, course_type):
          self.course_name=course_name
          self.course_type=course_type

  class FSDS_course:

      def course_duration(self):
           print("This course duration is for 12 months")
      def internship_project(self):
          print("This is the course for internship project")

  class internship(Ineuron_courses,FSDS_course):

      def __init__(self,internship_name,internship_duration):
          self.internship_name=internship_name
          self.internship_duration=internship_duration

      def print_intern_name(self):

          print("Internship name is",self.internship_name)

      def print_intern_duration(self):
          print("Intern Duration is",self.internship_duration)

except Exception as e:
    logging.exception(e)

t1=internship("Face Detection","4 months")
t1.course_duration()
t1.internship_project()
t1.print_intern_duration()
t1.print_intern_name()
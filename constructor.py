import logging

logging.basicConfig(filename="main.log", filemode="w",level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
logging.info("Entering into Task1 Program")

class iNeuron_students:

    def __init__(self, studentname, coursename, doj):
        """This is a constructor method of the class"""
        try:
            self.studentname = studentname
            self. coursename = coursename
            self.doj = doj
        except Exception as e:
            logging.exception(e)



s1 = iNeuron_students("Debanjan", "FSDS","29th July")

print(s1.studentname)
print(s1.coursename)
print(s1.doj)
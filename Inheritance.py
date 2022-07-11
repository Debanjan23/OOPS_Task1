import logging

logging.basicConfig(filename="Task.log",level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
logging.info("Entering into Task1 Program")

class iNeuron_students:

    def __init__(self, studentname,doj):
        """This is a constructor method of the class"""
        try:
            self.studentname = studentname
            self.doj = doj

        except Exception as e:
            logging.exception(e)


class FSDS_students(iNeuron_students):
    """FSDS_Student class is a child class of iNeuron students"""
pass


f1 = FSDS_students("Debanjan","29th June")
print(f1.studentname)
print(f1.doj)


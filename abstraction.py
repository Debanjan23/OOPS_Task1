import logging

logging.basicConfig(filename = "abstraction.log" ,  filemode= "w", level= logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s" )
logging.info("We are now inside abstratcion program")

"""In this program we are trying to implement data abstraction methodology"""

try:
    class iNeuron_login :
        __admin_login_flag = 1
        __employee_login_flag = 2
        __student_login_flag = 3

        def login_type(self, flag_value):

                      if flag_value==iNeuron_login.__admin_login_flag:
                              print("This is admin login type")
                      if flag_value==iNeuron_login.__student_login_flag:
                              print("This is student login type")
                      elif flag_value==iNeuron_login.__employee_login_flag:
                              print("This is employee login type")
                      else:
                              print("Login type is invalid")


except Exception as e:
 logging.exception(e)

login1 = iNeuron_login()
login1.login_type(3)
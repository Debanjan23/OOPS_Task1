import logging

logging.basicConfig(filename = "mthod_overide.log" ,  filemode= "w", level= logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s" )
logging.info("We are now inside encapsulation program")

"""In this program we are trying to implement method_overide concept"""

try:
    class iNeuron_products:

       def product_type(self):
        print("We have two type of products, one is B2C and B2B")

       def product_cost(self):
            print("Need to mention the product cost")

    class Resume_Builder(iNeuron_products):

        def student_resume(self):

            print("We have current 300 sample resumes based on year of expeirence")
        def resume_templates(self):

            print("We have 1000 resume template format")
        def product_cost(self):

            print("This subscription will cost you 100 rs monthly")

except Exception as e:
    logging.exception(e)

iR=Resume_Builder()
iR.product_cost()


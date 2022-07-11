import logging

logging.basicConfig(filename="Private.log",filemode="w",format="%(asctime)s %(levelname)s %(message)s")
logging.info("We are entering to Private, Public, Private and Protected Task program")

class iNeuron_vlog:

  try:
      vlog_name = "Transition Story"
      _no_of_viewers = 680
      __reviews_internal = "Good Feedback overall"

      def _vlog_rating(self):
        print("This is all about vlog rating")

      def __vlog_quality(self):
          print("This is all about vlog quality")


  except Exception as e:
     logging.exception(e)


vblog1 = iNeuron_vlog()

print(vblog1._iNeuron_vlog__reviews_internal)
print(vblog1.vlog_name)
print(vblog1._no_of_viewers)
vblog1._vlog_rating()
vblog1._iNeuron_vlog__vlog_quality()



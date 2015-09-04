import unittest
from gcm import *

SERVER_GCM_KEY = "AIzaSyD5CwBRQLMS0fuXh99T-t846FDmJbnA_G8"
CLIENT_GCM = ["fAy3t5vTJzk:APA91bEExaEWS2XmdDXgr9w3yIXMo2Rz9spUV0lu4TWy8PPwVrSeYm7KB0FV7h9WcHuaG_skFvmvmx1omxvwJKiNdE5vLi_5nOO6U4FFhauBwz4GRLsrT4IdA7LudHQ-eFW9s4XI80R1"]

data = {"msgid":102,
			"ncode":1001,
			"sender":"Ydn",
			"send_date": "2014-08-15 13:26:13",
			"subject":"haee kak lupeks",
			"message":"halooo kak lupeks... kira2 ya gini sih hasilnyaaa.... :p ",
			"extras":{"idJob":1, "idTicket":10, "ticket_no":"BCA_IN_AAAB"}}


class TestNotifyCall(unittest.TestCase):

	def setUp(self):
		self.gcm_notify = GCM(SERVER_GCM_KEY)

	def test_call(self):
		self.assertEqual(self.gcm_notify.notify(CLIENT_GCM, data),200)

if __name__ == '__main__':
	unittest.main()

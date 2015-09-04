# GCM
Simple lib for Goole Cloud Messaging


#Basics

from gcm import GCM

SERVER_GCM_KEY = "app_id"
CLIENT_GCM = ["client_id"]

data = {"msgid":102,
			"sender":"Ydn",
			"send_date": "2014-08-15 13:26:13",
			"subject":"haee kak lupeks",
			"message":"halooo kak lupeks... kira2 ya gini sih hasilnyaaa.... :p ",
			"extras":{"idJob":1, "idTicket":10, "ticket_no":"BCA_IN_AAAB"}}

gcm_notify = GCM(SERVER_GCM_KEY)
print gcm_notify.notify(CLIENT_GCM, data)
from gcm import GCM

SERVER_GCM_KEY = "AIzaSyD5CwBRQLMS0fuXh99T-t846FDmJbnA_G8"
CLIENT_GCM = ["dCS3kAB1CB4:APA91bEkUfR0xn0FeCnmyZZvl7OM55r3xh3XpoiAzw_-5g58e-RIag5YcjYqyKgLX8LQQu1ofBXKx5FkqL2DG0d_ASgdTodLPH1gvugyLXiTj7B77QPgEdwPun6hT7IeocyA4TciLfut"]

data = {"msgid":102,
			"sender":"Ydn",
			"send_date": "2014-08-15 13:26:13",
			"subject":"haee kak lupeks",
			"message":"Hello world",
			"extras":{"idJob":1, "idTicket":10, "ticket_no":"BCA_IN_AAAB"}}

gcm_notify = GCM(SERVER_GCM_KEY)
print gcm_notify.notify(CLIENT_GCM, data)
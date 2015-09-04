import urllib
import urllib2
import json

class GCM(object):
	"""
		Simple GCM (Google Cloud Messaging API) client for python
		URL to GCM is gived by default, but can be changed if needeed

		Args:
			key : String a key of your project
			gcm_url : String to GCM service.

	"""
	def __init__(self, key, gcm_url="https://android.googleapis.com/gcm/send"):
		self.key = key
		self.gcm_url = gcm_url

	"""
		Form json output for given data

		Args:
			data : dict filed with data to be sent
			clients: list of keys (users) to send notification

		Return:
			return : JSON object
	"""
	def __form_json_data(self, data, clients):
		post_data = {}
		post_data['data'] = data
		post_data['registration_ids'] = clients

		return json.dumps(post_data)


	"""
		Form HTTP headers to send on GCM server

		Args:
			no arguments

		Return:
			return HTTP header for call
	"""
	def __form_headers(self):
		return {'Content-Type':'application/json', "authorization":"key=" + self.key}

	"""
		Form HTTP request based ond json data and headers

		Args:
			post_data_json : JSON object that represent the data
			headers : dict with header info

		Return:
			return : urllib2.Request object with JSON data and headers
	"""	
	def __form_request(self, post_data_json, headers):
		return urllib2.Request(self.gcm_url, post_data_json, headers)

	"""
		Send data notifications to given users

		Args:
			clients : list of registered IDs provided by Google
			data : dict filed with data

		Return:
			return : HTTP Response Code, if no exception occurred
	"""
	def notify(self, clients, data):
		headers = self.__form_headers()

		post_data_json = self.__form_json_data(data, clients)

		try:
			req = self.__form_request(post_data_json, headers)
			response = urllib2.urlopen(req)

			return response.code
		except urllib2.URLError, e:
			e.message

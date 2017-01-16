"""
	A simple python script to send a push notification
	to the configured device.
"""
import sys
import urllib
import urllib2

PUSHOVER_URL = 'https://api.pushover.net/1/messages.json'

PUSH_OVER_SETTINGS = {
	'application_token': 'application token',
	'user_token': 'user key',
	# specify the device if a particular device is to be targeted.
	# 'device': 'nexus6p',
}

class PushoverSettings(object):
	def __init__(self, application_token, user_token, device=None):
		self.application_token = application_token
		self.user_token = user_token
		self.device = device

class Notifier(object):
	def __init__(self, settings):
		self.settings = settings

	def get_encoded_data(self, message):
		data = {
			"message": message,
			"user": self.settings.user_token,
			"token": self.settings.application_token
		}
		if self.settings.device is not None:
			data["device"] = self.settings.device

		encoded_data = urllib.urlencode(data)
		return encoded_data

	def send(self, message):
		encoded_data = self.get_encoded_data(message)
		try:
			response = urllib2.urlopen(PUSHOVER_URL, encoded_data)
			status_msg = "Notification sent with message " + message
		except urllib2.URLError as e:
			status_msg = "There was an error sending the notification. "
			status_msg += e.reason
		return status_msg

def print_usage():
	print "Usage: ", sys.argv[0], " <push_message>"

def main():
	if len(sys.argv) != 2:
		print_usage()
		return

	message = sys.argv[1]

	settings = PushoverSettings(**PUSH_OVER_SETTINGS)

	print Notifier(settings).send(message)

if __name__ == "__main__":
	main()
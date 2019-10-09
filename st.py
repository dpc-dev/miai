# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse,urllib3,requests

class ZhenziSmsClient(object):
	def __init__(self, apiUrl, appId, appSecret):
		self.apiUrl = apiUrl
		self.appId = appId
		self.appSecret = appSecret

	def send(self, number, message, messageId=''):
		data = {
    	    'appId': self.appId,
		    'appSecret': self.appSecret,
		    'message': message,
		    'number': number,
		    'messageId': messageId
		}
        
		# data = urllib.parse.urlencode(data).encode('utf-8')
		req = requests.post(self.apiUrl+'/sms/send.do', data=data,verify=False)
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		return req.text


	def balance(self):
		data = {
		    'appId': self.appId,
		    'appSecret': self.appSecret
		}
		data = urllib.parse.urlencode(data).encode('utf-8');
		req = urllib.request.Request(self.apiUrl+'/account/balance.do', data=data);
		res_data = urllib.request.urlopen(req);
		res = res_data.read();
		return res;

	def findSmsByMessageId(self, messageId):
		data = {
		    'appId': self.appId,
		    'appSecret': self.appSecret,
		    'messageId': messageId
		}
		data = urllib.parse.urlencode(data).encode('utf-8');
		req = urllib.request.Request(self.apiUrl+'/smslog/findSmsByMessageId.do', data=data);
		res_data = urllib.request.urlopen(req);
		res = res_data.read();
		return res;
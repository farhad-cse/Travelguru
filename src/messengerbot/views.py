from django.shortcuts import render
from django.views import generic
from pprint import pprint
from django.utils.decorators import method_decorator
from django.view.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse

 #Create your views here.
 #for receive message 
class TravelBotView(generic.view):
	def get(self,request,*args,**kwargs):
		if self.request.GET['hub.verify_token']=='7657245521':
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Error,invalid token')

@method_decorator(csrf_exempt)
def dispatch(self,request,*args,**kwargs):
	return generic.view.dispatch(self,request,*args,**kwargs)

#post function to handle fb messege
def post(self,request,*args,**kwargs):
	incoming_message=json.loads(self.request.body)
	for entry in entry['messaging']:
		if message.has_key('message'):
			pprint(message)
			post_facebook_message(message['sender']['id'],message['message']['text'])
			return HttpResponse()





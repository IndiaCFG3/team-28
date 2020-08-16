

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from twilio.rest import Client


account_sid = 'AC2c49d79585a7af83ac6b40e578e92ffb'
auth_token = '3da1954c71039122aa4e1f0b45180c20'
client = Client(account_sid, auth_token)

@login_required(login_url="/login/")
def index(request):

	file1 = open('myfile.txt', 'r') 
	Lines = file1.readlines()
	print(Lines) 
	return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
	context = {}
	# All resource paths end in .html.
	# Pick out the html file name from the url. And load that template.
	try:
		'''
		logic req
		...
		'''
		load_template = request.path.split('/')[-1]
		html_template = loader.get_template( load_template )
		return HttpResponse(html_template.render(context, request))
		
	except template.TemplateDoesNotExist:

		html_template = loader.get_template( 'error-404.html' )
		return HttpResponse(html_template.render(context, request))

	except:
	
		html_template = loader.get_template( 'error-500.html' )
		return HttpResponse(html_template.render(context, request))
   
def WAForm(request):
	if request.method == "POST":
		subject = request.POST['WA_subject']
		class_id = request.POST['WA_Select']
		text = request.POST['WA_Text']
		#details=model_name.objects.create(subject=subject,class_id=class_id,text=text)
		#details.save();
		print(subject)

		message = client.messages.create(
							  body=text,
							  from_='whatsapp:+14155238886',
							  to='whatsapp:+918660902359'
						  )
		print(message.sid)
		return render(request, "index.html")
	else:
		return render(request, "ui-forms.html")
	

def SMSForm(request):
	if request.method == "POST":
		subject = request.POST['SMS_subject']
		class_id = request.POST['SMS_Select']
		text = request.POST['SMS_Text']
	#details=model_name.objects.create(subject=subject,class_id=class_id,text=text)
		#details.save();
		print(subject)
		return render(request, "index.html")
	else:
		return render(request, "ui-forms.html")

from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def contact(request):
    if request.method == 'POST':
        message_name = request.POST['Name']
        message_email = request.POST['Email']
        message_subject = request.POST['Subject']
        message_comment = request.POST['comment']

    #send an email

        send_mail(
            message_name,
            message_comment,
            message_subject,
            message_email,
            ['saadvavatofficial@gmail.com']
            )

        return render(request, 'contactusvone.html', {'message_name': message_name})
   
    else:
         return render(request, 'contactusvone.html')
    

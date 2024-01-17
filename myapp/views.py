from django.shortcuts import render
from django.template.loader import render_to_string,get_template
from django.core.mail import EmailMessage
from django.http import HttpResponse
def sendmail(request):
    ctx={
        'name':'akshaya',
        'message':'Hello,this is a test email',
    }
    message=get_template('index.html').render(ctx)
    try:
        msg = EmailMessage(
            'Subject',
            message,
            'aroma95chand@gmail.com',
            ['nsaaromachandrasekhar@gmail.com'],
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        print("Mail successfully sent")
        return HttpResponse("Mail sent successfully")
    except Exception as e:
        print("Error sending mail:", str(e))
        return HttpResponse("Error sending mail: " + str(e))
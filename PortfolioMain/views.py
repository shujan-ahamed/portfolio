import os
from django.shortcuts import redirect, render

from portfolio.models import Achivements, ContactMessages, Education, Experience, Features, Languages, Portfolio, Resume,  Skills, Web_cat
from django.contrib import messages

from .utils import send_contact_email
from django.contrib.sites.shortcuts import get_current_site


from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.contrib.auth.models import User


from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def home(request):
    portfolios = Portfolio.objects.all()[:5]
    resume = Resume.objects.filter().first()
    achievement = Achivements.objects.filter().first()

    languages = Languages.objects.all()
    web_cats = Web_cat.objects.all()
    features = Features.objects.all()

    context={
        'portfolios' : portfolios,
        'resume' : resume,
        'achievement' : achievement,
        'languages' : languages,
        'web_cats' : web_cats,
        'features' : features,
    }
    return render(request, 'home.html', context)




def contact(request):
    resume = Resume.objects.filter().first()
    current_site = get_current_site(request)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        print(email)
        

        #send info notification
        mail_subject = "You have recieved a contact mail."
        mail_template = 'mail/contact_mail.html'

        admin_info = User.objects.filter(is_superuser= True)
        print(admin_info)
        admin_email = []
        for i in admin_info:
            admin_email.append(i.email)
        print(admin_email)

        message = Mail(
        from_email= email,
        to_emails= 'work.shujan1@gmail.com',
        subject= subject,
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
        
        context= {
            'to_email' :email,
            'name' : name,
            'subject' : subject,
            'message' : message,
            'domain' : current_site,
        }
        try:
            sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
            sg = SendGridAPIClient(sendgrid_api_key)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            print('e')
        except Exception as e:
            print(e)

        # send_contact_email(mail_subject, mail_template, context)
        print('email, done')
        message = ContactMessages(
            name = name,
            email = email,
            subject = subject,
            message = message,
        )
        message.save()
        messages.success(request, 'submitted successfully')
        return redirect('contact')
    else:
        return render(request, 'contact.html', {'resume' : resume,
            'domain' : current_site,})


    
def resume(request):
    resume = Resume.objects.filter().first()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skills.objects.all()
    context = {
        'resume' : resume,
        'experiences'  : experiences,
        'educations' : educations,
        'skills' : skills,
    }
    return render(request, 'resume.html', context)



def services(request):
    languages = Languages.objects.all()
    web_cats = Web_cat.objects.all()
    features = Features.objects.all()

    context = {
        'languages' : languages,
        'web_cats' : web_cats,
        'features' : features,
    }
    return render(request, 'services.html',context)


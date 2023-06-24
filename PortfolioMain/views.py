from django.shortcuts import redirect, render

from portfolio.models import Achivements, ContactMessages, Education, Experience, Features, Languages, Portfolio, Resume,  Skills, Web_cat
from django.contrib import messages

from .utils import send_contact_email
from django.contrib.sites.shortcuts import get_current_site



def home(request):
    portfolios = Portfolio.objects.all()[:5]
    resume = Resume.objects.get()
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
    resume = Resume.objects.get().first()
    current_site = get_current_site(request)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        

        #send info notification
        mail_subject = "You have recieved a contact mail."
        mail_template = 'mail/contact_mail.html'
        
        context= {
            'to_email' :email,
            'name' : name,
            'subject' : subject,
            'message' : message,
            'domain' : current_site,
        }
        send_contact_email(mail_subject, mail_template, context)
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
    resume = Resume.objects.get()
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


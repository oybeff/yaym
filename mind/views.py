from .models import Work, Team, Article,  Newsletter, UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ContactForm
from django.core.mail import send_mail 
from django.template.loader import render_to_string
from django.conf import settings
import ssl
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ContactForm 
from django.contrib.auth import logout
from django.shortcuts import render # type: ignore
from datetime import datetime

ssl._create_default_https_context = ssl._create_unverified_context

def index(request):
    work_item = Work.objects.all()
    print(work_item)
    team = Team.objects.all()
    article = Article.objects.all()
    newsletter = Newsletter.objects.all()
    translated_works = []

    for work in work_item:
        translated_subtitle = _(work.subtitle)  # Mark for translation
        translated_works.append({'subtitle': translated_subtitle})

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            msg = form.cleaned_data['msg']

            email_subject = _('New Contact Form Submission from {name}').format(name=name)  # Mark for translation
            email_message = _('Name: {name}\nEmail: {email}\n\nMessage:\n{msg}').format(
                name=name, email=email, msg=msg)  # Mark for translation

            try:
                send_mail(email_subject, email_message, email, ['yourmindca@gmail.com'])
                return redirect('home')
            except Exception as e:
                return HttpResponse(_("An error occurred: {e}").format(e=e))  # Mark for translation

    else:
        form = ContactForm()

    context = {
        'work': translated_works,
        'team': team,
        'article': article,
        'newsletter': newsletter,
        'form': form
    }

    return render(request, 'mind/base.html', context)

def newsletter(request):
    return render(request, 'mind/index.html')

def articles(request):
    return render(request, 'mind/articles.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

# views.py
# views.py
from django.shortcuts import render, redirect
from .models import UserProfile
from datetime import datetime

def multi_step_form(request):
    if request.method == 'POST':
        step = int(request.POST.get('step', '1'))
        if step == 1:
            request.session['first_name'] = request.POST.get('first_name')
            request.session['last_name'] = request.POST.get('last_name')
            return render(request, 'mind/find_element.html', {'step': 2})
        elif step == 2:
            dob_day = int(request.POST.get('dob-day'))
            dob_month = int(request.POST.get('dob-month'))
            dob_year = int(request.POST.get('dob-year'))
            dob = datetime(dob_year, dob_month, dob_day).date()
            request.session['dob'] = dob.isoformat()  # Store only the date part
            return render(request, 'mind/find_element.html', {'step': 3})
        elif step == 3:
            request.session['region'] = request.POST.get('region')
            request.session['country'] = request.POST.get('country')
            return render(request, 'mind/find_element.html', {'step': 4})
        elif step == 4:
            email = request.POST.get('email')
            dob = datetime.fromisoformat(request.session['dob']).date()  # Convert back to date
            user_profile = UserProfile(
                first_name=request.session['first_name'],
                last_name=request.session['last_name'],
                dob=dob,
                region=request.session['region'],
                country=request.session['country'],
                email=email
            )
            user_profile.save()
            response = user_profile.get_element_response()
            return render(request, 'mind/result.html', {'response': response})

    return render(request, 'mind/find_element.html', {'step': 1})

def result(request):
    return render(request, "mind/result.html",)
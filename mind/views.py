from .models import Work, Team, Article,  Newsletter, UserProfile, Newsletterin, Articlein, Category, Teamin
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ContactForm
from django.core.mail import send_mail 
from django.template.loader import render_to_string
import ssl
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from datetime import datetime
from .forms import CustomUserCreationForm, ContactForm 
from django.contrib.auth import logout
from googletrans import Translator
from django.utils.translation import get_language
ssl._create_default_https_context = ssl._create_unverified_context



def index(request):
    # Fetch all newsletters
    newsletters = Newsletter.objects.all()

    # Initialize the translator
    translator = Translator()
    lang_code = get_language()  # Get the current language code

    # Translate newsletter titles and descriptions
    translated_newsletters = []
    for newsletter in newsletters:
        try:
            translated_title = translator.translate(newsletter.title, dest=lang_code).text if newsletter.title else None
            translated_description = translator.translate(newsletter.description, dest=lang_code).text if newsletter.description else None
        except Exception as e:
            # Use the original title and description if translation fails
            translated_title = newsletter.title
            translated_description = newsletter.description

        translated_newsletters.append({
            'title': translated_title,
            'img': newsletter.img.url if newsletter.img else None,
            'description': translated_description,
            'slug': newsletter.slug
        })

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
                error_message = _("An error occurred: {error}").format(error=str(e))
                return HttpResponse(error_message)

    else:
        form = ContactForm()

    context = {
        'newsletter1': translated_newsletters,
        'form': form
    }

    return render(request, 'mind/base.html', context)
   

def newsletterin(request, slug):
    newsletter = get_object_or_404(Newsletter, slug=slug)
    newsletter_detail = Newsletterin.objects.filter(related_newsletter=newsletter)
    
    

    context = {
        'newsletter_detail': newsletter_detail,
        'newsletter': newsletter,
    }
   

    return render(request, 'mind/index.html', context)


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

def privacy(request):
    return render(request, "privacy/privacy_policy.html",)

def disclaimer(request):
    return render(request, "privacy/disclaimer.html")

def statedc(request):
    return render(request, "privacy/statedc.html")

def linkpolicy(request):
    return render(request, "privacy/linkpolicy.html")

def yyrequired(request):
    return render(request, "privacy/yyrequired.html")

def yystore(request):
    return render(request, "privacy/yystore.html")


def howwework(request):
    work_items = Work.objects.all()
    translated_works = []

    translator = Translator()
    lang_code = get_language()  # Get the current language code

    for work in work_items:
        # Translate the subtitle dynamically
        translated_subtitle = translator.translate(work.subtitle, dest=lang_code).text
        translated_works.append({'subtitle': translated_subtitle})

    context = {
        'work': translated_works,
    }

    return render(request, "mind/howwework.html", context)

def articlepage(request, slug=None):
    # Initialize the translator
    translator = Translator()

    if slug:
        category = get_object_or_404(Category, slug=slug)
        article1 = Article.objects.filter(category=category).order_by('-published_date')[:2]
    else:
        article1 = Article.objects.order_by('-published_date')[:2]
        category = None

    # Get the current language code
    lang_code = get_language()

    # Translate article fields
    for article in article1:
        if article.title_article:
            article.title_article = translator.translate(article.title_article, dest=lang_code).text

        if article.subtitle:
            article.subtitle = translator.translate(article.subtitle, dest=lang_code).text

    context = {
        'article1': article1,
        'category': category,
    }
    return render(request, "mind/articlepage.html", context)
def articles_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category).order_by('-published_date')
    
    if not articles.exists():
        return render(request, 'mind/404.html', status=404)
    
    return render(request, 'mind/related_article.html', {'articles': articles, 'category': category})


def articles(request, slug):
    translator = Translator()
    article = get_object_or_404(Article, slug=slug)

    # Get the current language code
    lang_code = get_language()

    try:
        articlein = Articlein.objects.get(related_article=article)

        # Translate all relevant fields
        if articlein.title_article:
            articlein.title_article = translator.translate(articlein.title_article, dest=lang_code).text

        if articlein.subtitle:
            articlein.subtitle = translator.translate(articlein.subtitle, dest=lang_code).text

        if articlein.title_first_article:
            articlein.title_first_article = translator.translate(articlein.title_first_article, dest=lang_code).text

        if articlein.content1:
            articlein.content1 = translator.translate(articlein.content1, dest=lang_code).text

        if articlein.content2:
            articlein.content2 = translator.translate(articlein.content2, dest=lang_code).text

        if articlein.content3:
            articlein.content3 = translator.translate(articlein.content3, dest=lang_code).text

        if articlein.content4:
            articlein.content4 = translator.translate(articlein.content4, dest=lang_code).text

        if articlein.title_second_article:
            articlein.title_second_article = translator.translate(articlein.title_second_article, dest=lang_code).text

        if articlein.content5:
            articlein.content5 = translator.translate(articlein.content5, dest=lang_code).text

        if articlein.content6:
            articlein.content6 = translator.translate(articlein.content6, dest=lang_code).text

    except Articlein.DoesNotExist:
        return render(request, 'mind/404.html', {'error_message': 'Article details not found'}, status=404)

    context = {
        'article': article,
        'articlein': articlein,
    }
    return render(request, 'mind/articles.html', context)

def related_article(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category).order_by('-published_date')
    articles1 = Article.objects.all()

    context = {
        'articles': articles,
        'category': category,
        'articles1': articles1
    }
    return render(request, 'mind/related_article.html', context)

def shop(request):
    return render(request, 'mind/shop.html')

def teamin(request, slug):
    # Fetch the team member based on the slug
    team_member = get_object_or_404(Team, slug=slug)
    
    # Fetch the related image from the Teamin model
    teamin_img = Teamin.objects.filter(related_person=team_member).first()
    
    context = {
        'title': team_member.title,
        'description': team_member.description,
        'img': teamin_img.img if teamin_img else None,  # Use the image from Teamin or None if not available
    }
    return render(request, 'mind/teamin.html', context)

def team(request):
    # Fetch all team members
    team_members = Team.objects.all()
    translated_team_members = []

    # Initialize the translator
    translator = Translator()
    lang_code = get_language()  # Get the current language code

    for member in team_members:
        try:
            # Translate the fields dynamically
            translated_title = translator.translate(member.title, dest=lang_code).text if member.title else None
            translated_subtitle = translator.translate(member.subtitle, dest=lang_code).text if member.subtitle else None
            translated_description = translator.translate(member.description, dest=lang_code).text if member.description else None
        except Exception:
            # Use the original fields if translation fails
            translated_title = member.title
            translated_subtitle = member.subtitle
            translated_description = member.description

        translated_team_members.append({
            'title': translated_title,
            'img': member.img,
            'subtitle': translated_subtitle,
            'description': translated_description,
            'slug': member.slug,  # Include slug here
        })

    context = {
        'team': translated_team_members,
    }

    return render(request, "mind/team.html", context)

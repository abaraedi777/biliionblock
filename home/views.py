from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/job-2.html")
    
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        twitter_username = request.POST.get("twitter_username")
        followers_number = request.POST.get("followers_number")
        wallet_proof = request.POST.get("wallet_proof")
        experience_years = request.POST.get("experience_years")
        previous_project = request.POST.get("previous_project")
        why_join = request.POST.get("why_join")
        what_to_contribute = request.POST.get("what_to_contribute")

        checked_data = []
        for key in request.POST:
            if key.startswith('checkbox'):
                checked_data.append(request.POST[key])

        context = {
            "name": name,
            "email": email,
            "twitter_username": twitter_username,
            "followers_number": followers_number,
            "wallet_proof": wallet_proof,
            "experience_years": experience_years,
            "previous_project": previous_project,
            "skills": checked_data,
            "why_join": why_join,
            "what_to_contribute": what_to_contribute,
        }
        html_message = render_to_string("home/email-sending.html", context=context)
        plain_message = strip_tags(html_message)
        message = EmailMultiAlternatives(
            subject = 'Billion Block User Registration',
            body = plain_message,
            from_email = settings.EMAIL_HOST_USER,
            to = ["zkland001@gmail.com", ]
        )
        message.attach_alternative(html_message, "text/html")
        message.send()

        messages.success(request, f"{name} your application has been recieved!!!")

        return redirect("home:home_view")
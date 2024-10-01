from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from base import models
from base.models import Contact


def contact(request):
    if request.method == "POST":
        print("POST")
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')
        print(name, email, number, content)

        if not (2 <= len(name) <= 40):
            messages.error(request, 'Length should be between 2 and 40 characters.')
            return render(request, 'home.html')

        if not (2 <= len(email) <= 40):
            messages.error(request, 'Invalid Email entered.')
            return render(request, 'home.html')

        if len(number) < 10:  
            messages.error(request, 'Invalid Number entered.')
            return render(request, 'home.html')

        if len(content) > 400:
            messages.error(request, 'Maximum limit exceeded: 400 characters.')
            return render(request, 'home.html')

        # Save to database
        ins = models.Contact(name=name, email=email, number=number, content=content)
        ins.save()
        messages.success(request, 'Thank you for contacting me.')
        print("Message saved to DB successfully.")

    return render(request, 'home.html')

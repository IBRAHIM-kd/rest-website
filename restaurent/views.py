from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
        return render(request, 'restaurent/index.html')
		
def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['player.ibrahim00@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "cook/email.html", {'form': form})


def success(request):
    return render(request, 'restaurent/success.html')		




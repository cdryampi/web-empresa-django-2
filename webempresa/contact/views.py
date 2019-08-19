from django.shortcuts import render,HttpResponse, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email =request.POST.get('email','')
            content = request.POST.get('content','')
            # Suponemos que todo va bien enviamos el correo y lo redireccinamos.
            email = EmailMessage(
                    "La caffettiera: Nuevo mensaje de contacto",
                    "de {} <{}>\n\nEscribió \"{}\"".format(name,email,content),
                     "no-contestar@inbox.mailtrap.io",
                    ["cdryampi@gmail.com"],
                    reply_to=[email]
            )
            try:
                email.send()
                #Todo ha ido bien
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo no ha ido bien
                return redirect(reverse('contact')+"?fail")
            
    return render(request,"contact/contact.html",{'form':contact_form})
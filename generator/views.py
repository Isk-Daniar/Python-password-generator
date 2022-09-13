from django.shortcuts import render
import random
# Create your views

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special'):
        characters.extend(list('$¢€£¥₩₿₽₹¤₱₦ƒ₮৲৳₨௹฿៛₪₫₭₲₴₵≋﷼'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length',10))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def info(request):
    return render(request, 'generator/info.html')
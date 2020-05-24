from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')
def password(request):

    import string
    import random
    alp = string.ascii_lowercase


    length = request.GET.get('length')

    if request.GET.get('specials'):
        alp = alp + string.punctuation
    if request.GET.get('numbers'):
        alp = alp + string.digits
    if request.GET.get('uppercase'):
        alp = alp + string.ascii_uppercase

    thepassword = "".join(random.choices(alp, k=int(length)))


    return render(request, 'generator/password.html', {"pass": thepassword})
def about(request):
    return render(request, 'generator/about.html')
# Create your views here.

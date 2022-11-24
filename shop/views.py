from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume


def index_page(request):
    return render(request, 'shop/index.html')


def home_page(request):
    return render(request, 'shop/temp.html')


def my_block(request):
    data = Resume.objects.all()
    return render(request, 'shop/lenta.html', {"data": data})


def profile(request, id):
    data = Resume.objects.get(id=id)
    return render(request, 'shop/temp.html', {"data": data})


def shop_form(request):
    error = ''
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            print('keldi')
            form.save()
            return redirect('home')
        else:
            error = 'Запись было неверной'


    form = ResumeForm()
    data = {
        'form':form,
        'error':error,
    }
    return render(request, 'shop/shop_form.html', data)
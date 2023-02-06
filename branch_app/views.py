from django.shortcuts import render

from branch_app.models import Ernakulam, Trivandrum, Thrissur, Kollam, Kottayam


# Create your views here.
def ekm_branch(request):
    ekm = Ernakulam.objects.all()
    return render(request, 'ernakulam.html',{'ekm':ekm})


def tvm_branch(request):
    tvm = Trivandrum.objects.all()
    return render(request, 'trivandrum.html',{'tvm':tvm})


def klm_branch(request):
    klm = Kollam.objects.all()
    return render(request, 'kollam.html',{'klm':klm})


def ktm_branch(request):
    ktm = Kottayam.objects.all()
    return render(request, 'kottayam.html',{'ktm':ktm})


def tsr_branch(request):
    tsr = Thrissur.objects.all()
    return render(request, 'thrissur.html',{'tsr':tsr})

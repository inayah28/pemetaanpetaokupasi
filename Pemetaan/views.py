from django.shortcuts import render, redirect
from django.views import View
from Cekprofesi.models import Matkul
from Cekprofesi.models import Kursus
from Cekprofesi.models import Profesi
from Cekprofesi.models import ProfMatkul
from Cekprofesi.models import ProfKursus
from django.contrib.auth import authenticate,login,logout

def index(request):
    return render(request,'index.html')

def ProgramStudi(request):
    semester1 = Matkul.objects.filter(semester=1)
    semester2 = Matkul.objects.filter(semester=2)
    semester3 = Matkul.objects.filter(semester=3)
    semester4 = Matkul.objects.filter(semester=4)
    semester5 = Matkul.objects.filter(semester=5)
    semester6 = Matkul.objects.filter(semester=6)
    semester7 = Matkul.objects.filter(semester=7)
    semester8 = Matkul.objects.filter(semester=8)
    kursus1 = Kursus.objects.filter(semester=1)
    kursus2 = Kursus.objects.filter(semester=2)
    kursus3 = Kursus.objects.filter(semester=3)
    kursus4 = Kursus.objects.filter(semester=4)
    kursus5 = Kursus.objects.filter(semester=5)
    kursus6 = Kursus.objects.filter(semester=6)
    context = {
        'Semesters1': semester1,
        'Semesters2': semester2,
        'Semesters3': semester3,
        'Semesters4': semester4,
        'Semesters5': semester5,
        'Semesters6': semester6,
        'Semesters7': semester7,
        'Semesters8': semester8,
        'Kursusz1': kursus1,
        'Kursusz2': kursus2,
        'Kursusz3': kursus3,
        'Kursusz4': kursus4,
        'Kursusz5': kursus5,
        'Kursusz6': kursus6,
    }
    return render(request,'kursus.html',context)
def Profesi(request):
    return render(request,'profesi.html')

def Bantuan(request):
    return render(request, 'Bantuan.html')

   
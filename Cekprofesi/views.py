from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Matkul
from .models import Kursus
from .models import Profesi
from .models import ProfMatkul
from .models import ProfKursus
from django.http import Http404
import re

from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

#
def index(request):
    profesi = Profesi.objects.all()
    context = {
        'Profesis':profesi,
    }
    def jaccard_similarity(x, y):
        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        return intersection_cardinality/float(union_cardinality)
    if request.method == 'POST':
        nama_profesi = request.POST['name_profesi']
        profmatkul=ProfMatkul.objects.filter(profesi=nama_profesi)
        profkursus=ProfKursus.objects.filter(profesi=nama_profesi)
        context = {    
            'Profesis1':nama_profesi,
            'profmatkuls':profmatkul,
            'profkursuss':profkursus,
            'pesan': 'Dalam setiap profesi pastinya membutuhkan matakuliah umum selain dibidang TIK, karena setiap bidang pekerja haruslah mempunyai nilai nasionalisme, tidak hanya itu saja, dalam profesi bidang TIK ini juga bahasa asing sangat berpengaruh, dan juga matakuliah yang berhubungan dengan perhitungan',
        }
        if not profmatkul:
            data_profesi={}
            tb_profesi =  Profesi.objects.all()
            for p in tb_profesi:
                data_profesi.update({p.profesi: p.unitk})
                #print(data_profesi)
            data_matkul = {}
            for p1 in Matkul.objects.all():
                data_matkul.update({p1.matkul:p1.slbmatkul})
            data_kursus = {}
            for p2 in Kursus.objects.all():
                data_kursus.update({p2.kursus: p2.slbkursus})
            for profesi, unitk in data_profesi.items():
                if request.POST.get('name_profesi') == profesi:
                    #uniklist=[]
                    #uniklist.append(unitk)
                    #text = nltk.word_tokenize(unitk)
                
                    
                      
                    #print(stemmed_ft)
                    
                    #print(uniklist)
                    #tigram =  [b for l in uniklist for b in zip(l.split(" ")[:-2],l.split(" ")[1:-1],l.split(" ")[2:])]
                    #print(tigram)
                    def generate_ngrams(unitk, n):
                        # Convert to lowercases
                        unitk = unitk.lower()
                        
                        # Replace all none alphanumeric characters with spaces
                        unitk = re.sub(r'[^a-zA-Z0-9\s]', ' ', unitk)
                        
                        # Break sentence in the token, remove empty tokens
                        tokens = [token for token in unitk.split(" ") if token != ""]
                        
                        # Use the zip function to help us generate n-grams
                        # Concatentate the tokens into ngrams and return
                        ngrams = zip(*[tokens[i:] for i in range(n)])
                        return [" ".join(ngram) for ngram in ngrams]
                    trigram=generate_ngrams(unitk, n=3)
                    

            for matkul,slbmatkul in data_matkul.items():
                #uniklist1=[]
                #uniklist1.append(slbmatkul)
                #text = nltk.word_tokenize(slbmatkul)
               
                #trigram2 =  [b for l in uniklist1 for b in zip(l.split(" ")[:-2],l.split(" ")[1:-1],l.split(" ")[2:])]
                #print(bigrams2)
                trigram2 = generate_ngrams(slbmatkul, n=3)
                    
                hasil = jaccard_similarity(trigram, trigram2)
                hasil_percen = '{0:.0%}'.format(hasil)
                kata_sama = set.intersection(*[set(trigram), set(trigram2)])
                #hasilsama=re.sub(r'[^\w]', ' ', kata_sama)

                if hasil > 0:
                    #profesi_matkul.append(matkul)
                    print ('Hasil Similarity Profesi '+request.POST.get('name_profesi')+ ' dan matkul ' +matkul+ ' adalah ...')
                    print("#")
                    print("#")
                    print(trigram)
                    print(len(trigram))
                    print(trigram2)
                    print(len(trigram2))
                    print ('  ' +hasil_percen+ '\n')
                    print('daftar kata profesi '+request.POST.get('name_profesi') + '\n')
                    print(str (unitk)+ '\n\n')
                    print('daftar kata matakuliah '+matkul+ '\n')
                    print(str(slbmatkul)+ '\n\n')
                    print('kata sama'  + '\n')
                    print(kata_sama )
                    print(len(kata_sama))
                    #print(hasilsama)
                    insert_table = ProfMatkul(profesi=request.POST.get('name_profesi'),matkul=matkul, presentase=hasil_percen, katasama=kata_sama)
                    insert_table.save()

            for kursus,slbkursus in data_kursus.items():
                #uniklist2=[]
                #uniklist2.append(slbkursus)
                #text = nltk.word_tokenize(slbmatkul)
                
                    #print(uniklist)
                #trigram2 =  [b for l in uniklist2 for b in zip(l.split(" ")[:-2],l.split(" ")[1:-1],l.split(" ")[2:])]
                trigram3 = generate_ngrams(slbkursus, n=3)
                hasil = jaccard_similarity(trigram, trigram3)
                hasil_percen = '{0:.0%}'.format(hasil)
                kata_sama = set.intersection(*[set(trigram), set(trigram3)])

                
                if hasil > 0:
                    #profesi_matkul.append(matkul)
                    print ('Hasil Similarity Profesi '+request.POST.get('name_profesi')+ ' dan matkul ' +matkul+ ' adalah ...')
                    print("#")
                    print("#")
                   
                    print ('  ' +hasil_percen+ '\n')
                    print('daftar kata profesi '+request.POST.get('name_profesi') + '\n')
                    print(str (unitk)+ '\n\n')
                    print('daftar kata matakuliah '+matkul+ '\n')
                    print(str(slbkursus)+ '\n\n')
                    print('kata sama'  + '\n')
                    print(kata_sama )


                    insert_table = ProfKursus(profesi=request.POST.get('name_profesi'),kursus=kursus, presentase=hasil_percen, katasama=kata_sama)
                    insert_table.save()
                # else:
                #     print('tidak ada kursus')
                    # a = {
                    #     'pesan':'tidak ada',
                    # }
                    

            profmatkul=ProfMatkul.objects.filter(profesi=nama_profesi)
            profkursus=ProfKursus.objects.filter(profesi=nama_profesi)
            context = {
                'profmatkuls':profmatkul,
                'Profesis1':nama_profesi,
                'profkursuss':profkursus,
                'pesan': 'Dalam setiap profesi pastinya membutuhkan matakuliah umum selain dibidang TIK, karena setiap bidang pekerja haruslah mempunyai nilai nasionalisme, tidak hanya itu saja, dalam profesi bidang TIK ini juga bahasa asing sangat berpengaruh, dan juga matakuliah yang berhubungan dengan perhitungan',
        
            }
                
            return render(request, 'sistem/index.html', context)
        
        else:
       
            profmatkul=ProfMatkul.objects.filter(profesi=nama_profesi)
            profkursus=ProfKursus.objects.filter(profesi=nama_profesi)
            context = {
      
               'profmatkuls':profmatkul,
               'profesi':nama_profesi,
               'Profesis1':nama_profesi,
               'profkursuss':profkursus,
               'pesan': 'Dalam setiap profesi pastinya membutuhkan matakuliah umum selain dibidang TIK, karena setiap bidang pekerja haruslah mempunyai nilai nasionalisme, tidak hanya itu saja, dalam profesi bidang TIK ini juga bahasa asing sangat berpengaruh, dan juga matakuliah yang berhubungan dengan perhitungan',
       
            }
            return render(request, 'sistem/index.html', context)
    return render(request, 'sistem/index.html', context)

# def Login(request):
#     user =  None
#     if request.method =="POST":
#         username_login=request.POST['username']
#         password_login=request.POST['password']
#         # print(username)
#         # print(password)
#         # menegecek apakah user dan pass ada
#         user = authenticate(request, username=username_login, password=password_login)
#         if user is not None:
#             login(request, user)
#             print(user)
#             return redirect('/Django/Jurusan')
#         else:
#             return redirect('/Django/login')
#     return render(request,'sistem/login.html')

#      Create your views here.
# def HapusData(request, delete_id):
#     Matkul.objects.filter(id=delete_id).delete()
#     return redirect('Django:jurusan')
# # Create your views here.
# def EditData(request, edit_id):
#     Matkul_edit = Matkul.objects.get(id=edit_id)
#     data = {
#         'matkul': Matkul_edit.matkul,
#         'semester': Matkul_edit.semester,
#         'slbmatkul': Matkul_edit.slbmatkul,
#         'ubah':'Update',
#     }
#     if request.method=='POST':
#         Matkul.objects.get(id=edit_id).update()
#     # Matkul_form = MatkulForm(request.POST or None, initail=data, instance=Matkul_edit)
#     # if request.method == 'POST':
#     #     if Matkul_form.is_valid():
#     #         Matkul_form.save()
        
#     #     return redirect('Django:tambah')
#     # context = {
#     #     "Matkul_edit":Matkul_edit,
#     # }
#     return render(request, 'sistem/tambah.html', data)
    
# def TambahData(request):
#     # Matkul_form = MatkulForm(request.POST or None)
#     # if request.method == 'POST':
#     #     if Matkul_form.is_valid():
#     #         Matkul_form.save()
        
#     #     return redirect('Django:jurusan')
#     if request.method=='POST':
#         Matkul.objects.create(
#             matkul = request.POST['matakuliah'],
#             semester = request.POST['semester'],
#             slbmatkul = request.POST['slbmatkul'],
#             )
#         return redirect('/Django/jurusan')
#     # context = {
#     #     "Matkul_form":Matkul_form,
#     # }
#     return render (request, 'sistem/tambah.html')
# def Jurusan(request):
#     return render(request,'sistem/Jurusan.html')
# def JurusanKursus(request):
#     if request.method=="POST":
#         if request.POST['logout'] =="Submit":
#             logout(request)
#         return redirect('index')
#     kursus = Kursus.objects.all()
#     context = {
#         'Kursuss':kursus,
#     }
#     return render(request, 'sistem/Jurusan-Kursus.html',context)
# def JurusanMatkul(request):
#     if request.method=="POST":
#         if request.POST['logout'] =="Submit":
#             logout(request)
#         return redirect('index')
#     matakuliah = Matkul.objects.all()
#     context = {
#         'Matkuls':matakuliah,
#     }
#     return render(request, 'sistem/Jurusan-Matkul.html',context)

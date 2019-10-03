from django.contrib import admin
# Register your models here.
from .models import Matkul
from .models import Profesi
from .models import Kursus
from .models import ProfMatkul
from .models import ProfKursus
# class MatkulAdmin(admin.ModelAdmin):
#     list_display = ('matkul','semester')
#admin.site.register(Matkul, MatkulAdmin);
admin.site.register(Matkul);
admin.site.register(Profesi);
admin.site.register(Kursus);
admin.site.register(ProfMatkul);
admin.site.register(ProfKursus);


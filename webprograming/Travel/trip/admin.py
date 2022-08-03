from django.contrib import admin
from trip.models import Upload, Detail

# Register your models here.

class DetailInline(admin.StackedInline):
    model = Detail
    extra = 3


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    inlines = (DetailInline,)
    list_display = ('id', 'title', 'start_dt', 'end_dt')
    
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'place','lat','log')
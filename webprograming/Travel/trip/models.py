from django.db import models
from django.forms import CharField
from django.urls import reverse

# 여행 일정 등록
class Upload(models.Model):
    title = models.CharField('TITLE',max_length=30)
    start_dt = models.DateField('START_DATE')
    end_dt = models.DateField('END_DATE')
    
    class Meta:
        ordering = ('title',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail_detail", args=(self.id,))
    
# 여행 상세 등록
class Detail(models.Model):
    trip_list = models.ForeignKey(Upload,on_delete=models.CASCADE)
    time = models.CharField('TIME', max_length=50)
    place = models.CharField('PLACE', max_length=100)
    lat = models.DecimalField('Latitude', max_digits = 30, decimal_places = 20)
    log = models.DecimalField('longitude', max_digits = 30, decimal_places = 20)
    
    class Meta:
        ordering = ('time',)
        
    def __str__(self):
        return self.place
    
    def get_absolute_url(self):
        return reverse("trip_detail_detail", args=(self.id,))
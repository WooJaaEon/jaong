from django.shortcuts import render
from django.views.generic import ListView, DetailView
from trip.models import Upload, Detail


# Create your views here.
class UploadLV(ListView):
    model = Upload
    template_name = 'upload_list.html'
    context_object_name = 'uploads'
    paginate_by = 10

def main(request):
    uploads = Upload.objects #모델로부터 객체의 목록을 전달, 쿼리셋
    return render(request, 'upload_list.html', {'uploads': uploads})  
    
class DetailDV(DetailView):
    model = Detail
    
  
from django.urls import path
from trip import views

urlpatterns = [
    #/trip
    path('',views.UploadLV.as_view(), name = 'upload_list'),
    # /trip/detail
    path('detail/<int:pk>',views.DetailDV.as_view(), name = 'detail_detail'),
]
from django.conf.urls import url
from management.mahasiswa import views
from django.urls import path, include


app_name = "management.mahasiswa"

urlpatterns = [
    url (r'^$', views.ListMahasiswaView.as_view(), name='view'),
    # url('', views.ListMahasiswaView.as_view(), name='view'),
]
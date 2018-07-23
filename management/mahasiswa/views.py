from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Mahasiswa
from management.mahasiswa.forms import MahasiswaForm


class ListMahasiswaView(View):
    def get(self, request):

        form = MahasiswaForm(request.POST or None)
        template = 'management/mahasiswa/index.html'
        mahasiswa = Mahasiswa.objects.all()
        data = {
            'mahasiswa' : mahasiswa,
            'form' : form
        }
        return render(request, template, data)

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Warga, Pengaduan
# Create your views here.
class WargaListView(ListView):
    model = Warga

class WargaDetailView(ListView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan
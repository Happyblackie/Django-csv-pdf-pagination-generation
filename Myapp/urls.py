from django.urls import path
from .import views

urlpatterns = [
       path('index/',views.index,name='index'),
       path('textfile',views.TextFile,name='textfile'),
       path('csvfile',views.CsvFile,name='csvfile'),
       path('pdffile',views.PdfFile,name='pdffile'),

       path('paginate/',views.Paginate,name='paginate'),
]
   
 
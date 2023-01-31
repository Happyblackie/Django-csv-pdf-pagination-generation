from django.shortcuts import render
from django.http import HttpResponse

#csv
from .models import Test
import  csv


#pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#pagination
from django.core.paginator import Paginator



def index(request):
    return render(request,'index.html')

def Paginate(request):
    a = Test.objects.all()
    #set up pagination
    p = Paginator(Test.objects.all(),1)
    page =  request.GET.get('page')
    b = p.get_page(page)

    return render(request,'pagination.html',{'a':a, 'b':b})






def TextFile(request):

 # return HttpResponse('fo') 
    response = HttpResponse(content_type = 'text/plain')
    response['Content-Disposition'] = 'attachment; filename = aaa.txt'

    #lines = ['My name is Happy \n',
            #'i love Jesus \n',
            #'forgive my sins Jesus \n']
      
    #designate/get dat from database table
    x = Test.objects.all()

    #create blank list to hold the data from database
    lines = []

    #loop thriugh the table
    for y in x:
        #lines.append(f'{y} \n')  #this gives only names, but you can get all data by:

        lines.append(f' {y.name} \n {y.passion} \n {y.citizenship} \n\n\n')

    
    response.writelines(lines)
    return response





def CsvFile(request):

 # return HttpResponse('fo') 
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename = bbb.csv'

    # part B ii     create a csv writer
    writer = csv.writer(response)
  
    #designate/get dat from database table
    x = Test.objects.all()

    #add a cloumn heading to the csv file
    writer.writerow(['name, passion','citizenship'])

    #loop thriugh the table
    for y in x:
        #lines.append(f'{y} \n')  #this gives only names, but you can get all data by:

        writer.writerow([y.name, y.passion, y.citizenship])  # part B iiI


    return response


def PdfFile(request):
    #create ByteStream buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf,pagesize=letter, bottomup=0)
    #create a text object
    textobj = c.beginText()
    textobj.setTextOrigin(inch ,inch)
    textobj.setFont("Helvetica", 14)

    #Add some manual lines of text to test first
    ''' lines = ['My name is Happy ',
            'i love Jesus ',
            'forgive my sins Jesus '] '''
    
      #designate/get dat from database table
    x = Test.objects.all()
    
    #create blank list to hold the data from database
    lines = []

    for y in x:
        lines.append(y.name)
        lines.append(y.passion)
        lines.append(y.citizenship)
        lines.append(" ")
    #Loop
    for line in lines:
        textobj.textLine(line)

    #finish up
    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    #Return something
    return FileResponse(buf,as_attachment=True, filename='cc.pdf')





from django.shortcuts import render, redirect  
from .forms import CustomerForm  
from .models import  Customer  ,Company
from django.http  import HttpResponse
from .functions import quitar_espacios,valida_tiempo
from datetime import datetime, time
# Create your views here.  
def addnew(request):  
    error = ''
    if request.method == "POST":  
        form = CustomerForm(request.POST)
        company_data = quitar_espacios(request.POST["company"])
        company_querie = Company.objects.filter(name=company_data).first()
        if company_querie is None:
            Company.objects.create(name=company_data)
            Company.save()
        if company_querie is  None:
            company = Company.objects.create(name=company_data)
            company.save()

        time_attention =  datetime.strptime(request.POST["time_attention"] , '%H:%M') 
        final_attention_time = datetime.strptime(request.POST["final_attention_time"] , '%H:%M') 
        if final_attention_time < time_attention:
               error = 'La hora final de atencion no puede ser menor a la hora inicial de atencion...'
       
               return render(request,'index.html',{'form':form , 'errors':error})  
        try:
            date_time_obj = datetime. strptime(request.POST["date_of_request"] , '%Y-%m-%d')
            if date_time_obj > datetime.now():
                error = 'La fecha de solicitud no puede ser mayor a la fecha actual , gracias...'
               
                return render(request,'index.html',{'form':form , 'errors':error})  
        except:
            error = 'El formato de fecha del campo Date of request no es el adecuado recuerde yyyy-mm-dd...'
            
            return render(request,'index.html',{'form':form , 'errors':error})  


        request.POST._mutable = True
        request.POST["company"] = Company.objects.filter(name=company_data).first().id
        if form.is_valid():  
            try:  
                error = 'Registro exitoso'
                form.save()  
                return redirect('/')  
            except:  
                pass 
        else:
            error = 'El formato de fecha es incorrecto , recuerde el formato es aaaa-mm-dd'
    else:  
        form = CustomerForm()  
    return render(request,'index.html',{'form':form , 'errors':error})  
def index(request):  
    Customers = Customer.objects.all()  
    return render(request,"show.html",{'Customers':Customers})  
def edit(request, id):
    form = CustomerForm()    
    Customers = Customer.objects.get(id=id)  
    return render(request,'edit.html', {'Customer':Customers , 'form':form})  
def update(request, id):
    
    Customers = Customer.objects.get(id=id)  
    form = CustomerForm(request.POST, instance = Customers)  
    company_data = quitar_espacios(request.POST["company"])
    company_querie = Company.objects.filter(name=company_data).first()
    if company_querie is None:
        company = Company.objects.create(name=company_data)
        company.save()
        company_querie = Company.objects.filter(name=company_data).first()

    #time_attention =  datetime.strptime(request.POST["time_attention"] , '%H:%M') 
    #final_attention_time = datetime.strptime(request.POST["final_attention_time"] , '%H:%M') 
    tiempo = valida_tiempo(request.POST["time_attention"],request.POST["final_attention_time"],request.POST["date_of_request"])
    #if final_attention_time < time_attention:
    #        error = 'La hora final de atencion no puede ser menor a la hora inicial de atencion...'
    #        return render(request, 'edit.html', {'Customer': Customers,'errors':error , "form":form}) 

    if tiempo is not None:
        return render(request, 'edit.html', {'Customer': Customers,'errors':tiempo , "form":form}) 
    #try:
    #    date_time_obj = datetime. strptime(request.POST["date_of_request"] , '%Y-%m-%d')
    #    if date_time_obj > datetime.now():
    #        error = 'La fecha de solicitud no puede ser mayor a la fecha actual , gracias...'
    #        return render(request, 'edit.html', {'Customer': Customers,'errors':error , "form":form})  
    #except:
    #    error = 'El formato de fecha del campo Date of request no es el adecuado recuerde yyyy-mm-dd...'
    #    return render(request, 'edit.html', {'Customer': Customers,'errors':error , "form":form})  



    request.POST._mutable = True
    request.POST["company"] = company_querie.id
    error = ''
    form = CustomerForm(request.POST, instance = Customers)  
    if form.is_valid():  
        print("llegue")
        form.save()  
        return redirect("/") 
    else:
        form = CustomerForm()
        error ='Datos de actualizacion incompletos'
    return render(request, 'edit.html', {'Customer': Customers,'errors':error , "form":form})  
def destroy(request, id):  
    Customers = Customer.objects.get(id=id)  
    Customers.delete()  
    return redirect("/")  

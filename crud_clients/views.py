from django.shortcuts import render, redirect  
from .forms import CustomerForm  
from .models import  Customer  ,Company
from .functions import quitar_espacios,valida_tiempo

def addnew(request):  
    error = ''
    form = CustomerForm()
    if request.method == "POST":  
        company_data = quitar_espacios(request.POST["company"])
        company_querie = Company.objects.filter(name=company_data).first()
        if company_querie is None:
            data_querie = Company.objects.create(name=company_data)
            data_querie.save()
        tiempo = valida_tiempo(request.POST["time_attention"],request.POST["final_attention_time"],request.POST["date_of_request"])
        if tiempo is not None:
            return render(request,'index.html',{'form':form , 'errors':tiempo})
        request.POST._mutable = True
        request.POST["company"] = Company.objects.filter(name=company_data).first().id
        form = CustomerForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
        else:
            error = 'El formato de fecha es incorrecto , recuerde el formato es aaaa-mm-dd'

    return render(request,'index.html',{'form':CustomerForm() , 'errors':error}) 


def index(request):  
    Customers = Customer.objects.all()  
    return render(request,"show.html",{'Customers':Customers}) 


def edit(request, id):
    form = CustomerForm()    
    Customers = Customer.objects.get(id=id)  
    return render(request,'edit.html', {'Customer':Customers , 'form':form})


def update(request, id):
    error_validation = ""
    Customers = Customer.objects.get(id=id)  
    form = CustomerForm(request.POST, instance = Customers)  
    company_data = quitar_espacios(request.POST["company"])
    company_querie = Company.objects.filter(name=company_data).first()
    if company_querie is None:
        company = Company.objects.create(name=company_data)
        company.save()
        company_querie = Company.objects.filter(name=company_data).first()

    for llave, valor in request.POST.items():
        if valor == '':
            error_validation += "has ingresado uno de los campos del formulario ,  vacio favor verifique los campos y diligenciarlos nuevamente"
            break

    if error_validation != "":
        return render(request, 'edit.html', {'Customer': Customers,'errors':error_validation , "form":form})    

    tiempo = valida_tiempo(request.POST["time_attention"],request.POST["final_attention_time"],request.POST["date_of_request"])
    if tiempo is not None:
        return render(request, 'edit.html', {'Customer': Customers,'errors':tiempo , "form":form}) 

    request.POST._mutable = True
    request.POST["company"] = company_querie.id
    error = ''
    form = CustomerForm(request.POST, instance = Customers)  
    if form.is_valid():  
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

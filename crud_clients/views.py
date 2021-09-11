from django.shortcuts import render, redirect  
from .forms import CustomerForm  
from .models import  Customer  ,Company
from django.http  import HttpResponse
# Create your views here.  
def addnew(request):  
    error = ''
    if request.method == "POST":  
        form = CustomerForm(request.POST)
        company_data = request.POST["company"]
        company_data = company_data.strip().upper()
        company_querie = Company.objects.filter(name=company_data).first()
        if company_querie is  None:
            Company.objects.create(name=company_data)
            Company.save()
        if form.is_valid():  
            try:  
                error = 'Registro exitoso'
                form.save()  
                return redirect('/')  
            except:  
                pass 
        else:
            print(form.errors)
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
    print(request.POST)  
    error = ''
    Customers = Customer.objects.get(id=id)  
    form = CustomerForm(request.POST, instance = Customers)  
    if form.is_valid():  
        form.save()  
        return redirect("/") 
    else:
        print(form.errors)
        error ='Datos de actualizacion incompletos'
    return render(request, 'edit.html', {'Customer': Customers,'errors':error})  
def destroy(request, id):  
    Customers = Customer.objects.get(id=id)  
    Customers.delete()  
    return redirect("/")  

from django.shortcuts import render, redirect  
from .forms import CustomerForm  
from .models import Customer  
from django.http  import HttpResponse
# Create your views here.  
def addnew(request):  
    error = ''
    if request.method == "POST":  
        form = CustomerForm(request.POST)  
        print(request.POST["time_attention"])
        if form.is_valid():  
            try:  
                error = 'Registro exitoso'
                form.save()  
                return redirect('/')  
            except:  
                pass 
        else:
            error = 'El formato de fecha es incorrecto , recuerde el formato es aaaa-mm-dd'
            print(form.errors)
    else:  
        form = CustomerForm()  
    return render(request,'index.html',{'form':form , 'errors':error})  
def index(request):  
    Customers = Customer.objects.all()  
    return render(request,"show.html",{'Customers':Customers})  
def edit(request, id):  
    Customers = Customer.objects.get(id=id)  
    return render(request,'edit.html', {'Customer':Customers})  
def update(request, id):  
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

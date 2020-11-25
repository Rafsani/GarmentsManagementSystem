from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Employee,Products,Garment,Order,Department,Deparment_Admin

# Create your views here.
def home(request):
    return render(request,'HomePage.html')

def admin_login(request):
    if request.method != 'POST':
        return render(request,'login.html')
    else:
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        user_ref = authenticate(username=user_name,password=pass_word)
        if user_ref:
            if user_ref.is_active and user_ref.is_staff and not user_ref.is_superuser:
                login(request, user_ref)
                return redirect('/dashboard/')
            else:
                return HttpResponse("<h1> You are not authorized to view Dashboard</h1>")
        else:
            return HttpResponse("login failed")


@login_required(login_url='/login/')
def admin_logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def dashboard(request):
    return render(request,'dashboard.html')


@login_required(login_url='/login/')
def AddEmployee(request):
    if request.method !="POST":
        depts = Department.objects.all()
        return render(request,'AddEmployee.html',{'depts':depts})
    else:
        name = request.POST["name"]
        department = Department.objects.get(pk = request.POST["department"])
        Id = request.POST["EmpId"]
        salary = request.POST["salary"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        status = request.POST["status"]
        employee = Employee()
        employee.Name = name
        employee.EmployeeID = int(Id)
        employee.department = department
        employee.salary = salary
        employee.Phone = phone
        employee.address = address
        employee.status = status
        employee.save()

        return redirect('/employees/')

@login_required(login_url='/login/')
def ShowEmployees(request):
    if request.method != "POST":
        list = Employee.objects.all()
        return render(request,'ShowEmployees.html',{'list' : list})
    else:
        data = request.POST.get('searchname',False)
        if data == False:
            data = int(request.POST["searchid"],10)
            list = Employee.objects.filter(pk=data)
            return render(request, 'ShowEmployees.html', {'list': list})
        else:
            list = Employee.objects.filter(Name=data)
            return render(request, 'ShowEmployees.html', {'list': list})

@login_required(login_url='/login/')
def EditEmployee(request,pk):
    if request.method != "POST":
        data = Employee.objects.get(pk=pk)
        return render(request,'EditEmployee.html',{'data':data})
    else:
        name = request.POST["name"]
        department = request.POST["department"]
        salary = request.POST["salary"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        status = request.POST["status"]

        employee = Employee.objects.get(pk=pk)
        employee.Name = name
        employee.department = department
        employee.salary = salary
        employee.Phone = phone
        employee.address = address
        employee.status = status
        employee.save()
        return redirect('GarmentsManagementApp:ShowEmployee')

@login_required(login_url='/login/')
def deleteEmployee(request,pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('GarmentsManagementApp:ShowEmployee')

@login_required(login_url='/login/')
def AddProduct(request):
    if request.method !="POST":
        garments = Garment.objects.all()
        return render(request,'Addproduct.html',{'garments':garments})
    else:
        garments = Garment.objects.get(pk = request.POST["Garment"])
        p = Products()
        p.Name = request.POST["name"]
        p.garment = garments
        p.price = request.POST["price"]
        p.description = request.POST["description"]
        p.save()
        return redirect('/ShowProducts/')

@login_required(login_url='/login/')
def ShowProducts(request):
    list = Products.objects.all()
    return render(request,'ShowProducts.html',{'list' : list})

@login_required(login_url='/login/')
def editProduct(request,pk):
    if request.method != "POST":
        data = Products.objects.get(pk=pk)
        return render(request,'EditProduct.html',{'data':data})
    else:
        name = request.POST["name"]
        description = request.POST["description"]
        price = request.POST["price"]

        p = Products.objects.get(pk=pk)
        p.Name = name
        p.price = price
        p.description = description
        p.save()
        return redirect('GarmentsManagementApp:ShowProducts')

@login_required(login_url='/login/')
def deleteProduct(request,pk):
    prd = Products.objects.get(pk=pk)
    prd.delete()
    return redirect('GarmentsManagementApp:ShowProducts')


@login_required(login_url='/login/')
def AddGarment(request):
    if request.method !="POST":
        return render(request,'AddGarment.html')
    else:
        name = request.POST["name"]
        type = request.POST["type"]
        G = Garment()
        G.name = name
        G.type = type
        G.save()
        return redirect('GarmentsManagementApp:ShowGarments')

@login_required(login_url='/login/')
def ShowGarments(request):
    list = Garment.objects.all()
    return render(request,'ShowGarments.html',{'list' : list})

@login_required(login_url='/login/')
def EditGarment(request,pk):
    if request.method != "POST":
        data = Garment.objects.get(pk=pk)
        return render(request,'EditGarment.html',{'data':data})
    else:
        name = request.POST["name"]
        type = request.POST["type"]
        Gr = Garment.objects.get(pk=pk)
        Gr.name = name
        Gr.type = type
        Gr.save()
        return redirect('GarmentsManagementApp:ShowGarments')

@login_required(login_url='/login/')
def deleteGarment(request,pk):
    prd = Garment.objects.get(pk=pk)
    prd.delete()
    return redirect('GarmentsManagementApp:ShowGarments')

@login_required(login_url='/login/')
def createOrder(request):
    if request.method !="POST":
        list = Products.objects.all()
        return render(request,'createOrder.html',{'list':list})
    else:
        r = int(request.POST["product"],10)
        cust_name = request.POST["customer_name"]
        phn = request.POST["customer_phn"]
        product = Products.objects.get(pk=r)
        qty = int(request.POST["quantity"],10)
        O = Order()
        O.CustomerName = cust_name
        O.CustomerPhn = phn
        O.product = product
        O.quantity = qty
        O.TotalPrice = qty*product.price
        O.save()
        return redirect('GarmentsManagementApp:ShowOrders')

@login_required(login_url='/login/')
def ShowOrders(request):
    list = Order.objects.all()
    return render(request, 'ShowOrders.html', {'list': list})

@login_required(login_url='/login/')
def deleteOrder(request,pk):
    Order.objects.get(pk=pk).delete()
    return redirect('GarmentsManagementApp:ShowOrders')
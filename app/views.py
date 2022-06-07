from django.shortcuts import redirect, render
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
@login_required(login_url='/login')
def alltodo(request):
    if request.method=="POST":
         description = request.POST['description']
         start = request.POST['start']
         finish = request.POST['finish']
         Todo.objects.create(description=description,start=start,finish=finish,user=request.user)
         return redirect('/')
    print(request.user)
    todos = Todo.objects.filter(user=request.user).all()
    return render(request,'index.html',{'todos':todos})
@login_required(login_url='/login')
def deletetodo(request,id):
    Todo.objects.filter(id=id).delete()
    return redirect('/')
@login_required(login_url='/login')
def edittodo(request,id):
     if request.method=="POST":
               description = request.POST['description']
               start = request.POST['start']
               finish = request.POST['finish']
               Todo.objects.filter(id=id).update(description=description,start=start,finish=finish,user=request.user)
               return redirect('/')
     todo = Todo.objects.get(id=id)
     return render(request,'edit.html',{'todo':todo})
@login_required(login_url='/login')
def donetodo(request,id):
    stat =Todo.objects.get(id=id)
    stat.status = not(stat.status)
    stat.save()
    return redirect('/') 
def registerPage(request):
    if request.user.is_authenticated:
           return redirect('/')
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
           messages.error(request, 'This username has already been taken')
           return redirect('/register')
        if password !=password2:
           messages.error(request, 'Passwords are not match!')
           return redirect('/register')
        else:
           User.objects.create_user(username=username,password=password)
        return redirect('/login')
    return render(request,'register.html')     
def loginPage(request):
    if request.user.is_authenticated:
       return redirect('/')
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or password wrong')
            return redirect('/register')
    return render(request,'login.html')    
def logout_view(request):
    logout(request)
    return redirect('/login')    
      
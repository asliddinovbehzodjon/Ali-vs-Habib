from django.shortcuts import redirect, render
from .models import Todo
# Create your views here.
def alltodo(request):
    if request.method=="POST":
         description = request.POST['description']
         start = request.POST['start']
         finish = request.POST['finish']
         Todo.objects.create(description=description,start=start,finish=finish)
         return redirect('/')
          
    todos = Todo.objects.all()
    return render(request,'index.html',{'todos':todos})
def deletetodo(request,id):
    Todo.objects.filter(id=id).delete()
    return redirect('/')
def edittodo(request,id):
     if request.method=="POST":
               description = request.POST['description']
               start = request.POST['start']
               finish = request.POST['finish']
               Todo.objects.filter(id=id).update(description=description,start=start,finish=finish)
               return redirect('/')
     todo = Todo.objects.get(id=id)
     return render(request,'edit.html',{'todo':todo})
def donetodo(request,id):
    stat =Todo.objects.get(id=id)
    stat.status = not(stat.status)
    stat.save()
    return redirect('/') 
     
    
      
from django.shortcuts import render,redirect
from todoapp.models import todoR
from django.http import HttpResponse

# Create your views here.
def home(request):
    record=todoR.objects.all()
    r={"record":record}
    return render(request,"index.html",r)

def savedata(request):
    if request.method=="POST":
        title=request.POST.get("title")
        dis=request.POST.get("disc")
        mydata=todoR(title=title,disc=dis)
        mydata.save()
        return redirect("home")
    
def deleteRecordf(request,did):
    dele=todoR.objects.get(id=did)
    dele.delete()
    return redirect("home")

def undotodo(request):
    return HttpResponse("working on it................................!")

def donetodo(request, id):
    todo = todoR.objects.get(id = id)
    todo.title = True
    todo.save()

    # return HttpResponse("todod done")
    return redirect("home")
def updatetodo(request,upid):
    mydata=todoR.objects.get(id=upid)
    return render(request,"update.html",{"re":mydata})

    
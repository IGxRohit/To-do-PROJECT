
from django.urls import path
from todoapp import views

urlpatterns = [
    path("",views.home, name="home"),
    path("savedata",views.savedata),
    path("deleteRecord/<int:did>",views.deleteRecordf),
    path("undotodo",views.undotodo),
    path("donetodo/<int:id>",views.donetodo),
    path("updateRecord/<int:upid>",views.updatetodo),

  
]

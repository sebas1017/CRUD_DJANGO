from django.urls import path  
from .views  import index,addnew,edit,update,destroy
urlpatterns = [  
    path('',index),  
    path('addnew',addnew),  
    path('edit/<int:id>', edit),  
    path('update/<int:id>', update),  
    path('delete/<int:id>', destroy),  
]  

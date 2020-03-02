from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('delete/<int:idd>',views.delete,name='delete'),
    path('update/<int:idd>',views.update,name='update'),
    path('uncomplite/<int:idd>',views.uncomplite,name='uncomplite'),
    path('complite/<int:idd>',views.complite,name='complite'),
]

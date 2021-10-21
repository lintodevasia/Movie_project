from .import views
from django.urls import path
app_name = 'movieapp'
urlpatterns = [

    path('',views.home,name='home'),
    path('movie/<int:movie_id>/',views.details,name='detail'),
    path('add',views.addi,name='add'),
    path('update/<int:id>/',views.update,name='update'),
path('delete/<int:id>/',views.delete,name='delete')
]

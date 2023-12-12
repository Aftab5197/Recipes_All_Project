from django.urls import path

from recepieapp import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('add',views.add,name='add'),
    path('delete/<int:id>/',views.delete_recepie,name='delete_recepie'),
    path('update/<int:id>/',views.update_recepie,name='update_recepie'),
    path('search',views.searchbar,name='searchbar')
]
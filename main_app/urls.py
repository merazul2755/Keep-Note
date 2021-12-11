from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('add_note', views.add_note, name='add_name'),
    path('delete/<id>/', views.delete, name='delete'),
    path('edit_note/<int:id>/', views.edit_note, name='edit_note'),
    path('update_data/<int:id>/', views.update_data, name='update_data'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
    

  
]

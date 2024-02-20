from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('detail/<int:pk>/',views.record_detail,name='record'),
    path('delete/<int:pk>/',views.delete_record,name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update/<int:pk>/',views.update_record,name='update_record'),
]

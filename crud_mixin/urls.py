
from django.contrib import admin
from django.urls import path
from api.views import StudentList,StudentCreate,StudentRetrive,StudentUpdate1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',StudentCreate.as_view()),
    path('list/',StudentList.as_view()),
    path('retrive/<int:pk>/',StudentRetrive.as_view()),
    path('update/<int:pk>/',StudentUpdate1.as_view()),
]
